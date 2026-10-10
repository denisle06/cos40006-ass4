const http = require("http");

const PORT = process.env.PORT || 3000;

const page = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>New Web App</title>
</head>
<body>
  <h1>Hello from the Node.js web app!</h1>
  <p>Running inside a Docker container.</p>
  <p>Server time: <span id="time">loading...</span></p>
  <script>
    fetch("/api/time")
      .then((r) => r.json())
      .then((d) => { document.getElementById("time").textContent = d.time; });
  </script>
</body>
</html>`;

const server = http.createServer((req, res) => {
  if (req.url === "/api/time") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ time: new Date().toISOString() }));
  } else if (req.url === "/") {
    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    res.end(page);
  } else {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Not found");
  }
});

server.listen(PORT, "0.0.0.0", () => {
  console.log(`Web app listening on port ${PORT}`);
});
