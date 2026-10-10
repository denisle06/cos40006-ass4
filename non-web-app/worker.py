"""Non-web application run by uvicorn.

uvicorn is used purely as a process runner: the ASGI lifespan events start and
stop a background job. The app never serves web pages or API responses.
"""
import asyncio
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger("worker")

INTERVAL_SECONDS = 5


async def job():
    """Background job: compute the running sum of 1..n and log it."""
    total = 0
    n = 0
    while True:
        n += 1
        total += n
        log.info("Job tick %d: sum of 1..%d = %d", n, n, total)
        await asyncio.sleep(INTERVAL_SECONDS)


async def app(scope, receive, send):
    if scope["type"] != "lifespan":
        # Not a web app: refuse any HTTP/WebSocket traffic.
        raise RuntimeError("This application does not serve web requests")

    task = None
    while True:
        message = await receive()
        if message["type"] == "lifespan.startup":
            log.info("Worker started")
            task = asyncio.create_task(job())
            await send({"type": "lifespan.startup.complete"})
        elif message["type"] == "lifespan.shutdown":
            task.cancel()
            log.info("Worker stopped")
            await send({"type": "lifespan.shutdown.complete"})
            return
