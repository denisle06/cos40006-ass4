# Task 4: Deploy Containers Using Docker

## 1. Student Details

| Field | Value |
|---|---|
| Student ID | `[YOUR STUDENT ID]` |
| Full name | `[YOUR FULL NAME]` |

## 2. Unit Details

| Field | Value |
|---|---|
| Unit | SWE40006 Software Deployment and Evolution |
| Semester | `[SEMESTER / YEAR]` |
| Due date (for feedback) | `[DUE DATE]` |
| Submission date | `[SUBMISSION DATE]` |

## 3. Declaration of Task Level Attempted

I am attempting **Task 4.4 (High Distinction)**. This covers every sub-task from 4.1 to 4.4.

| Level | Sub-tasks | Section |
|---|---|---|
| 4.1 Pass | Create Docker account, install Docker client, deploy Hello-world | [Section 5](#5-task-41-pass) |
| 4.2 Credit | Deploy a Python app, add Python runtime, deploy hello-world web server, pull app to another Docker device | [Section 6](#6-task-42-credit) |
| 4.3 Distinction | Develop a new web app and deploy to a Docker installation | [Section 7](#7-task-43-distinction) |
| 4.4 HD | Develop a non-web-based app and deploy to Docker | [Section 8](#8-task-44-high-distinction) |

## 4. Public Verification Links

Source code and scripts are not included in this report. They are available at the links below.

| Item | Link |
|---|---|
| Source code (GitHub) | https://github.com/denisle06/cos40006-ass4 |
| Docker Hub profile | https://hub.docker.com/u/denisle1406 |
| Docker Hub repository (4.1 / 4.2 Python app) | `[LINK TO YOUR DOCKER HUB REPOSITORY]` |
| Docker Hub repository (4.2 web server) | https://hub.docker.com/r/denisle1406/swe40006-web |
| Docker Hub repository (4.3 Node.js web app) | https://hub.docker.com/r/denisle1406/swe40006-node |
| Docker Hub repository (4.4 CLI tool) | https://hub.docker.com/r/denisle1406/swe40006-cli |
| Publicly accessible IP / URL of a running deployment | `[PUBLIC IP OR URL, e.g. http://x.x.x.x:8000]` |

> **Note:** The Docker Hub links above work only if the repositories are set to public. Replace any link that does not match your own repository names.

### Repository structure

```
cos40006-ass4/
├── python/          Task 4.1 / 4.2: hello.py, Dockerfile, command.txt
├── webserver/       Task 4.2: Python hello-world web server
├── new-web-app/     Task 4.3: Node.js + JavaScript web app
├── non-web-app/     Task 4.4: Python command-line tool
└── REPORT.md        This report
```

Each folder has a `command.txt` that lists the exact commands used to build, run, push and pull that app.

---

## 5. Task 4.1 (Pass)

**Sub-tasks:** create a Docker account, install the Docker client, deploy Hello-world.

### 5.1 Create a Docker Hub account

I created a free account at https://hub.docker.com with the username `denisle1406`.

📸 **SCREENSHOT 1:** Docker Hub dashboard, signed in as `denisle1406`.
*Caption: Figure 1. Docker Hub account created.*

### 5.2 Install the Docker client

I installed Docker Desktop on Windows and checked the installation from the command prompt.

```
docker --version
docker run hello-world
```

📸 **SCREENSHOT 2:** Docker Desktop running, showing the engine status.
*Caption: Figure 2. Docker Desktop installed and running.*

📸 **SCREENSHOT 3:** Output of `docker --version`.
*Caption: Figure 3. Docker client version.*

### 5.3 Deploy Hello-world

The first test used the official `hello-world` image, which confirms Docker can pull an image and run a container.

📸 **SCREENSHOT 4:** Output of `docker run hello-world` ("Hello from Docker!").
*Caption: Figure 4. Official hello-world container running.*

### 5.4 Deploy my own Hello-world app

I wrote a small Python script and a Dockerfile in the `python/` folder.

**`python/hello.py`** prints `Hello, World!`.

**`python/Dockerfile`**

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY hello.py .
CMD ["python", "hello.py"]
```

| Instruction | Purpose |
|---|---|
| `FROM python:3.12-slim` | Starts from a small official image that includes the Python runtime. |
| `WORKDIR /app` | Sets the working directory inside the container. |
| `COPY hello.py .` | Copies the script into the image. |
| `CMD [...]` | Runs the script when the container starts. |

Commands used:

```
docker build -t hello-world-py .
docker run --rm hello-world-py
```

📸 **SCREENSHOT 5:** Output of `docker build -t hello-world-py .` (successful build).
*Caption: Figure 5. Building the hello-world Python image.*

📸 **SCREENSHOT 6:** Output of `docker run --rm hello-world-py` showing `Hello, World!`.
*Caption: Figure 6. Running the hello-world Python container.*

---

## 6. Task 4.2 (Credit)

**Sub-tasks:** deploy a Python app, add the Python runtime, deploy a hello-world web server, pull the app to another Docker device.

### 6.1 Deploy a Python app and add the Python runtime

The Python app from Section 5.4 is the Python app. The Python runtime is installed in the image by the `FROM python:3.12-slim` line of the Dockerfile. The host machine does not need Python installed.

📸 **SCREENSHOT 7:** Output of `docker images` listing `hello-world-py`.
*Caption: Figure 7. Local images, including the Python runtime base image and my app.*

### 6.2 Deploy a hello-world web server

I wrote a web server in `webserver/server.py` using only the Python standard library (`http.server`). It answers every request with `Hello, World!` on port 8000. It binds to `0.0.0.0` so that it can be reached from outside the container.

**`webserver/Dockerfile`**

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY server.py .
EXPOSE 8000
CMD ["python", "server.py"]
```

Commands used (from inside the `webserver` folder):

```
docker build -t denisle1406/swe40006-web:latest .
docker run --rm -p 8000:8000 denisle1406/swe40006-web:latest
```

The `-p 8000:8000` option maps port 8000 on the host to port 8000 in the container.

📸 **SCREENSHOT 8:** Output of the web server `docker build`.
*Caption: Figure 8. Building the web server image.*

📸 **SCREENSHOT 9:** Browser at `http://localhost:8000` showing `Hello, World!`, with the terminal visible if possible.
*Caption: Figure 9. Web server running locally in Docker.*

### 6.3 Push the image to Docker Hub

```
docker login
docker push denisle1406/swe40006-web:latest
```

📸 **SCREENSHOT 10:** Output of `docker push`.
*Caption: Figure 10. Pushing the web server image to Docker Hub.*

📸 **SCREENSHOT 11:** The Docker Hub repository page showing the pushed image and tag.
*Caption: Figure 11. Image visible on Docker Hub.*

### 6.4 Pull the app to another Docker device

"Pulling" an app means downloading the image from Docker Hub onto a different machine that has Docker installed. The second machine has none of my source code. It gets everything from the registry.

Second device used: `[DESCRIBE THE DEVICE, e.g. GitHub Codespaces / cloud VM / second PC / VirtualBox Ubuntu VM]`

Commands run on the second device:

```
docker pull denisle1406/swe40006-web:latest
docker run --rm -p 8000:8000 denisle1406/swe40006-web:latest
```

📸 **SCREENSHOT 12:** Terminal on the second device showing `docker pull` completing.
*Caption: Figure 12. Pulling the image on another Docker device.*

📸 **SCREENSHOT 13:** The web server running on the second device, with the browser showing `Hello, World!` at the public IP/URL.
*Caption: Figure 13. Web server running on the second device (public URL: `[PUBLIC IP OR URL]`).*

---

## 7. Task 4.3 (Distinction)

**Sub-tasks:** develop a new web app, deploy to a Docker installation.

### 7.1 The application

This is a new web app in the `new-web-app/` folder, written in **Node.js and JavaScript**. It uses only Node's built-in `http` module, so it needs no extra packages.

| Route | Response |
|---|---|
| `/` | An HTML page that calls the API below and shows the server time. |
| `/api/time` | JSON containing the current server time. |
| Any other path | 404 Not found. |

The app listens on port 3000 (changeable with the `PORT` environment variable).

### 7.2 Dockerfile

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package.json .
COPY app.js .
EXPOSE 3000
CMD ["npm", "start"]
```

| Instruction | Purpose |
|---|---|
| `FROM node:20-alpine` | Adds the Node.js runtime on a small Alpine Linux base. |
| `COPY package.json .` and `COPY app.js .` | Copies the app into the image. |
| `EXPOSE 3000` | Documents the port the app uses. |
| `CMD ["npm", "start"]` | Starts the app with `node app.js`. |

### 7.3 Build, run and deploy

From inside the `new-web-app` folder:

```
docker build -t denisle1406/swe40006-node:latest .
docker run --rm -p 3000:3000 denisle1406/swe40006-node:latest
docker login
docker push denisle1406/swe40006-node:latest
```

📸 **SCREENSHOT 14:** Output of `docker build` for the Node.js app.
*Caption: Figure 14. Building the Node.js web app image.*

📸 **SCREENSHOT 15:** Browser at `http://localhost:3000` showing the web page.
*Caption: Figure 15. Node.js web app running locally in Docker.*

📸 **SCREENSHOT 16:** Browser at `http://localhost:3000/api/time` showing the JSON response.
*Caption: Figure 16. API endpoint returning JSON.*

📸 **SCREENSHOT 17:** Output of `docker push` and/or the Docker Hub repository page.
*Caption: Figure 17. Node.js image pushed to Docker Hub.*

### 7.4 Deploy to another Docker installation

Deployment target: `[DESCRIBE, e.g. cloud VM / Codespaces / second PC]`

```
docker pull denisle1406/swe40006-node:latest
docker run --rm -p 3000:3000 denisle1406/swe40006-node:latest
```

📸 **SCREENSHOT 18:** `docker pull` and `docker run` on the target machine.
*Caption: Figure 18. Deploying the Node.js app to another Docker installation.*

📸 **SCREENSHOT 19:** Browser showing the app on the public IP/URL.
*Caption: Figure 19. Node.js app reachable at `[PUBLIC IP OR URL]`.*

---

## 8. Task 4.4 (High Distinction)

**Sub-tasks:** develop a non-web-based app, deploy to Docker.

### 8.1 The application

This is a **command-line text statistics tool** written in Python (`non-web-app/textstats.py`). It uses only the standard library and has no network interface. It reports characters, words, lines and the most common words.

| Option | Meaning |
|---|---|
| `--text "..."` | Analyse the text given on the command line. |
| `--file path` | Analyse a text file. |
| `--top N` | Number of common words to show (default 3). |
| piped input | If neither `--text` nor `--file` is given, text is read from standard input. |

If the file cannot be read, the tool prints a clear error message and exits with code 1.

### 8.2 Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY textstats.py .
ENTRYPOINT ["python", "textstats.py"]
```

`ENTRYPOINT` is used instead of `CMD` so that any arguments placed after the image name are passed straight to the tool, like a normal command.

### 8.3 Build and run

From inside the `non-web-app` folder:

```
docker build -t denisle1406/swe40006-cli:latest .
docker run --rm denisle1406/swe40006-cli:latest --text "the cat saw the dog and the dog saw the cat"
docker run --rm denisle1406/swe40006-cli:latest --help
```

📸 **SCREENSHOT 20:** Output of `docker build` for the CLI tool.
*Caption: Figure 20. Building the CLI tool image.*

📸 **SCREENSHOT 21:** Output of the `--text` run showing the statistics.
*Caption: Figure 21. CLI tool running in Docker with text input.*

📸 **SCREENSHOT 22:** Output of the `--help` run.
*Caption: Figure 22. CLI tool help text.*

### 8.4 Analyse a file with a volume mount

A volume (`-v`) shares a folder on the host with the container. The container can then read a file from my machine without the file being copied into the image.

```
docker run --rm -v "%cd%":/data denisle1406/swe40006-cli:latest --file /data/sample.txt --top 5
```

(`%cd%` is the Windows `cmd` form of "current folder". In PowerShell use `${PWD}`.)

📸 **SCREENSHOT 23:** Output of the volume-mounted file run.
*Caption: Figure 23. CLI tool reading a host file through a Docker volume.*

### 8.5 Push, pull and run on another Docker installation

```
docker login
docker push denisle1406/swe40006-cli:latest
docker pull denisle1406/swe40006-cli:latest
docker run --rm denisle1406/swe40006-cli:latest --text "hello from another device"
```

📸 **SCREENSHOT 24:** `docker push` output, or the Docker Hub repository page.
*Caption: Figure 24. CLI tool image on Docker Hub.*

📸 **SCREENSHOT 25:** `docker pull` and `docker run` on the second device.
*Caption: Figure 25. CLI tool pulled and run on another Docker device.*

---

## 9. Errors Encountered and How I Fixed Them

### 9.1 `tag does not exist` when pushing to Docker Hub

**Error**

```
C:\...\Assignment4>docker push denisle1406/swe40006:latest
The push refers to repository [docker.io/denisle1406/swe40006]
tag does not exist: denisle1406/swe40006:latest
```

I got the same error for the tags `tagname` and `hello`.

**Investigation**

The build output ended with `naming to docker.io/library/hello-world-py:latest`. So the local image was called `hello-world-py`, not `denisle1406/swe40006`. `docker push` can only upload an image that already exists locally under exactly that name and tag. A tag is not created just by naming it in a push command.

**Fix**

Either tag the existing image, or build with the full Docker Hub name from the start:

```
docker tag hello-world-py denisle1406/swe40006:latest
docker images
docker push denisle1406/swe40006:latest
```

For the later images I built directly with the Docker Hub name (`docker build -t denisle1406/swe40006-web:latest .`), so the error did not happen again. Running `docker images` before each push confirms the name and tag exist.

📸 **SCREENSHOT 26:** The `tag does not exist` error in the terminal.
*Caption: Figure 26. Push error caused by a missing local tag.*

📸 **SCREENSHOT 27:** `docker tag` and `docker images` showing the new tag, followed by a successful `docker push`.
*Caption: Figure 27. Error resolved by tagging the image before pushing.*

### 9.2 Play with Docker is no longer available

**Problem:** I planned to use Play with Docker (https://labs.play-with-docker.com) as the second Docker device, but the service has been stopped.

**Fix:** I used `[WHICH ALTERNATIVE YOU USED, e.g. GitHub Codespaces / cloud VM / second PC]` instead. Any machine with Docker installed can pull the image from Docker Hub, so the result is the same.

### 9.3 Other issues

`[ADD ANY OTHER ERRORS YOU MEET, e.g. port already in use, docker login failure, firewall blocking the port. For each one, give: the error text, why it happened, and how you fixed it.]`

📸 **SCREENSHOT 28 (optional):** Any other error you met, and its fix.
*Caption: Figure 28. `[DESCRIBE]`.*

---

## 10. Summary

| Task | Requirement | Status | Evidence |
|---|---|---|---|
| 4.1 | Docker account | Done | Figure 1 |
| 4.1 | Docker client installed | Done | Figures 2 to 3 |
| 4.1 | Hello-world deployed | Done | Figures 4 to 6 |
| 4.2 | Python app with runtime | Done | Figures 5 to 7 |
| 4.2 | Hello-world web server | Done | Figures 8 to 11 |
| 4.2 | Pulled to another device | `[Confirm]` | Figures 12 to 13 |
| 4.3 | New web app (Node.js) | Done | Figures 14 to 19 |
| 4.4 | Non-web app (CLI tool) | Done | Figures 20 to 25 |

All source code is at https://github.com/denisle06/cos40006-ass4. The Docker commands for each task are in that folder's `command.txt`.
