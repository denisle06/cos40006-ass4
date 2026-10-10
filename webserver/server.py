from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"Hello, World!"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    # Bind to 0.0.0.0 so the server is reachable from outside the container
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
