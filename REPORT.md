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

The full source code and scripts are on GitHub. Short Dockerfiles are included in this report because they are the main deployment artefacts.

| Item | Link |
|---|---|
| Source code (GitHub) | https://github.com/denisle06/cos40006-ass4 |
| Docker Hub profile | https://hub.docker.com/u/denisle1406 |
| Docker Hub repository (4.1 / 4.2 Python app) | https://hub.docker.com/r/denisle1406/swe40006 |
| Docker Hub repository (4.2 web server) | https://hub.docker.com/r/denisle1406/swe40006-web |
| Docker Hub repository (4.3 Node.js web app) | https://hub.docker.com/r/denisle1406/swe40006-node |
| Docker Hub repository (4.4 CLI tool) | https://hub.docker.com/r/denisle1406/swe40006-cli |
| Deployment to another device | All images are pushed to Docker Hub and pulled on a second Docker device (Sections 6.4, 7.4 and 8.5). |

> **Note:** Docker Hub links work only for public repositories. Figure 11 shows the account "Using 0 of 1 private repositories", which means `swe40006` is public.

### Repository structure

```
cos40006-ass4/
├── python/          Task 4.1 / 4.2: hello.py, Dockerfile, command.txt
├── webserver/       Task 4.2: Python hello-world web server
├── new-web-app/     Task 4.3: Node.js + JavaScript web app
├── non-web-app/     Task 4.4: Python command-line tool
├── photos/          Screenshots used in this report (not pushed to GitHub)
├── GUIDE.md         Step-by-step instructions and screenshot checklist
└── REPORT.md        This report
```

Each folder has a `command.txt` that lists the exact commands used to build, run, push and pull that app.

### Images built for this task

| Task | Local / Docker Hub image | Base image | Type |
|---|---|---|---|
| 4.1 / 4.2 | `hello-world-py` → `denisle1406/swe40006:latest` | `python:3.12-slim` | Console script |
| 4.2 | `denisle1406/swe40006-web:latest` | `python:3.12-slim` | Web server, port 8000 |
| 4.3 | `denisle1406/swe40006-node:latest` | `node:20-alpine` | Web app, port 3000 |
| 4.4 | `denisle1406/swe40006-cli:latest` | `python:3.12-slim` | Command-line tool |

---

## 5. Task 4.1 (Pass)

**Sub-tasks:** create a Docker account, install the Docker client, deploy Hello-world.

### 5.1 Create a Docker Hub account

I created a free account at https://hub.docker.com with the username `denisle1406`. The account is shown signed in at the top left of Figure 11.

![Docker Hub dashboard, signed in as denisle1406](photos/fig01.png)
*Figure 1. Docker Hub account created.*

### 5.2 Install the Docker client

I installed Docker Desktop on Windows. The build output in Figure 5 shows the builder `docker:desktop-linux`, which confirms that the Docker client is talking to the Docker Desktop engine.

```
docker --version
```

![Docker Desktop running, showing Engine running](photos/fig02.png)
*Figure 2. Docker Desktop installed and running.*

![Output of docker --version](photos/fig03.png)
*Figure 3. Docker client version.*

### 5.3 Deploy the official Hello-world

The first test used the official `hello-world` image. It confirms that Docker can pull an image from Docker Hub and run a container.

```
docker run hello-world
```

![Output of docker run hello-world ("Hello from Docker!")](photos/fig04.png)
*Figure 4. Official hello-world container running.*

### 5.4 Deploy my own Hello-world app

I wrote a one-line Python script and a Dockerfile in the `python/` folder.

![hello.py open in VS Code](photos/hello.png)
*Figure 4a. `hello.py` prints `Hello, World!`.*

![Python Dockerfile open in VS Code](photos/dockerfile-hello.png)
*Figure 4b. Dockerfile for the hello-world Python app.*

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
docker run hello-world-py
```

![docker build and docker run for hello-world-py](photos/docker-build-run.png)
*Figures 5 and 6. Building the `hello-world-py` image (9/9 steps, 18.2 s) and running it, which prints `Hello, World!`.*

What the build output shows:

- Docker downloaded the `python:3.12-slim` base image in four layers (the largest is 29.84 MB). This took most of the 18.2 s build time.
- My own Dockerfile added only two steps: `[2/3] WORKDIR /app` and `[3/3] COPY hello.py .`.
- The image was named `docker.io/library/hello-world-py:latest`. The `library/` prefix means the image has no Docker Hub username yet. This explains the push error in Section 9.1.

---

## 6. Task 4.2 (Credit)

**Sub-tasks:** deploy a Python app, add the Python runtime, deploy a hello-world web server, pull the app to another Docker device.

### 6.1 Deploy a Python app and add the Python runtime

The app from Section 5.4 is the Python app. The Python runtime comes from the `FROM python:3.12-slim` line of the Dockerfile. The host machine does not need Python installed: the container brings its own interpreter.

The `docker images` output lists `hello-world-py` at 177 MB. My script is only a few bytes, so almost all of that size is the Python runtime and the Debian base it runs on.

![Output of docker images listing hello-world-py](photos/fig07.png)
*Figure 7. Local images, including the Python app.*

### 6.2 Deploy a hello-world web server

I wrote a web server in `webserver/server.py` using only the Python standard library (`http.server`). It answers every GET request with `Hello, World!` on port 8000. It binds to `0.0.0.0` instead of `localhost`, because inside a container `localhost` would only accept connections from the container itself.

![server.py open in VS Code](photos/server.png)
*Figure 7a. `server.py`, the hello-world web server.*

![webserver Dockerfile open in VS Code](photos/dockerfile-server.png)
*Figure 7b. Dockerfile for the web server.*

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

`-p 8000:8000` maps port 8000 on the host to port 8000 in the container. `--rm` deletes the container when it stops, so stopped containers do not pile up.

![docker build and docker run for the web server](photos/build-and-run-python-web.png)
*Figure 8. Building and starting the web server image. The top of the terminal also shows the successful push of the Python app from Section 6.3.*

This build took only 3.1 s, compared with 18.2 s in Figure 5. Docker reused the `python:3.12-slim` layers it had already downloaded, and the `WORKDIR /app` step is marked `CACHED`. Only the new `COPY server.py .` layer had to be built.

![Browser at localhost:8000 showing Hello, World!](photos/running-python-web.png)
*Figure 9. The web server running in Docker, reached from the browser at `http://localhost:8000`.*

### 6.3 Push the images to Docker Hub

The Python app was built as `hello-world-py`, so it had to be tagged with my Docker Hub name before it could be pushed (see Section 9.1). The web server was built with its Docker Hub name, so it can be pushed directly.

```
docker login
docker tag hello-world-py denisle1406/swe40006:latest
docker push denisle1406/swe40006:latest
docker push denisle1406/swe40006-web:latest
```

The push of `denisle1406/swe40006:latest` uploaded 7 layers and ended with the digest `sha256:f0664deca1b9...` (Figures 8 and 27).

![Output of docker push denisle1406/swe40006-web:latest](photos/fig10.png)
*Figure 10. Pushing the web server image to Docker Hub.*

![Docker Hub repository page for denisle1406/swe40006](photos/on-docker-hub.png)
*Figure 11. The `denisle1406/swe40006` repository on Docker Hub with the `latest` tag.*

The Docker Hub page confirms:

| Field | Value |
|---|---|
| Repository | `denisle1406/swe40006` |
| Tag | `latest`, pushed by `denisle1406` |
| Platform | `linux/amd64` |
| Compressed size | 41.26 MB (177 MB once unpacked locally) |
| Pull command | `docker pull denisle1406/swe40006:latest` |

### 6.4 Pull the app to another Docker device

Pulling an app means downloading its image from Docker Hub onto a different machine that has Docker installed. The second machine has none of my source code. It gets everything from the registry.

Second device used: `[DESCRIBE THE DEVICE, e.g. a second laptop running Docker Desktop]`

Commands run on the second device:

```
docker pull denisle1406/swe40006:latest
docker run --rm denisle1406/swe40006:latest
docker pull denisle1406/swe40006-web:latest
docker run --rm -p 8000:8000 denisle1406/swe40006-web:latest
```

![Terminal on the second device showing docker pull completing and the Python app printing Hello, World!](photos/fig12.png)
*Figure 12. Pulling and running the images on another Docker device.*

![The web server running on the second device, with its browser showing Hello, World! at http://localhost:8000](photos/fig13.png)
*Figure 13. Web server running on the second device.*

---

## 7. Task 4.3 (Distinction)

**Sub-tasks:** develop a new web app, deploy to a Docker installation.

### 7.1 The application

This is a new web app in the `new-web-app/` folder, written in **Node.js and JavaScript**. It uses a different language and runtime from Task 4.2 to show that Docker deploys any stack the same way. It uses only Node's built-in `http` module, so it needs no `npm install`.

| Route | Response |
|---|---|
| `/` | An HTML page. Its script calls `/api/time` and shows the server time. |
| `/api/time` | JSON such as `{"time":"2026-10-26T09:30:00.000Z"}`. |
| Any other path | `404 Not found`. |

The app listens on `0.0.0.0` port 3000. The port can be changed with the `PORT` environment variable, for example `docker run -e PORT=8080 -p 8080:8080 ...`.

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
| `FROM node:20-alpine` | Adds the Node.js 20 runtime on a small Alpine Linux base. |
| `COPY package.json .` and `COPY app.js .` | Copies the app into the image. |
| `EXPOSE 3000` | Documents the port the app uses. |
| `CMD ["npm", "start"]` | Runs the `start` script in `package.json`, which is `node app.js`. |

### 7.3 Build, run and push

From inside the `new-web-app` folder:

```
docker build -t denisle1406/swe40006-node:latest .
docker run --rm -p 3000:3000 denisle1406/swe40006-node:latest
docker push denisle1406/swe40006-node:latest
```

![Output of docker build for the Node.js app](photos/fig14.png)
*Figure 14. Building the Node.js web app image.*

![Browser at http://localhost:3000 showing the heading and server time](photos/fig15.png)
*Figure 15. Node.js web app running locally in Docker.*

![Browser at http://localhost:3000/api/time showing the JSON response](photos/fig16.png)
*Figure 16. API endpoint returning JSON.*

![Output of docker push and/or the Docker Hub repository page](photos/fig17.png)
*Figure 17. Node.js image pushed to Docker Hub.*

### 7.4 Deploy to another Docker installation

Deployment target: the same second device as Section 6.4. The image is pulled from Docker Hub.

```
docker pull denisle1406/swe40006-node:latest
docker run --rm -p 3000:3000 denisle1406/swe40006-node:latest
```

![docker pull and docker run on the target machine](photos/fig18.png)
*Figure 18. Deploying the Node.js app to another Docker installation.*

![Browser on the second device showing the app at http://localhost:3000](photos/fig19.png)
*Figure 19. Node.js app running on the second device.*

---

## 8. Task 4.4 (High Distinction)

**Sub-tasks:** develop a non-web-based app, deploy to Docker.

### 8.1 The application

This is a **command-line text statistics tool** written in Python (`non-web-app/textstats.py`). It has no network interface and opens no ports. It reads some text, prints statistics, and exits. It uses only the standard library (`argparse`, `collections.Counter`).

| Option | Meaning |
|---|---|
| `--text "..."` | Analyse the text given on the command line. |
| `--file path` | Analyse a text file. |
| `--top N` | Number of most common words to show (default 3). |
| piped input | If neither `--text` nor `--file` is given, text is read from standard input. |

It reports the number of characters, words and lines, and the most common words. Words are lower-cased and stripped of punctuation before counting, so `The`, `the` and `the.` count as the same word. If the file cannot be read, the tool prints a clear error message and exits with code 1.

### 8.2 Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY textstats.py .
ENTRYPOINT ["python", "textstats.py"]
```

`ENTRYPOINT` is used instead of `CMD`. Any arguments placed after the image name in `docker run` are passed straight to the tool, so the container behaves like a normal command. With `CMD`, those arguments would replace the whole command instead.

### 8.3 Build and run

From inside the `non-web-app` folder:

```
docker build -t denisle1406/swe40006-cli:latest .
docker run --rm denisle1406/swe40006-cli:latest --text "the cat saw the dog and the dog saw the cat"
docker run --rm denisle1406/swe40006-cli:latest --help
```

Output of the `--text` run (Figure 21):

```
Characters: 43
Words:      11
Lines:      1
Most common words:
  the: 4
  cat: 2
  saw: 2
```

![Output of docker build for the CLI tool](photos/fig20.png)
*Figure 20. Building the CLI tool image.*

![Output of the --text run showing the statistics](photos/fig21.png)
*Figure 21. CLI tool running in Docker with text input.*

![Output of the --help run](photos/fig22.png)
*Figure 22. CLI tool help text.*

### 8.4 Analyse a file with a volume mount

A volume (`-v`) shares a folder on the host with the container. The container can then read a file from my machine without the file being copied into the image.

```
docker run --rm -v "%cd%":/data denisle1406/swe40006-cli:latest --file /data/sample.txt --top 5
```

(`%cd%` is the Windows `cmd` form of "current folder". In PowerShell use `"${PWD}:/data"`.)

`sample.txt` contains two lines, `the cat saw the dog.` and `The dog saw the cat!`. The result is 2 lines, 10 words, and `the: 4` at the top of the list (Figure 23), which shows that the upper-case `The` and the punctuation were handled.

![Output of the volume-mounted file run](photos/fig23.png)
*Figure 23. CLI tool reading a host file through a Docker volume.*

### 8.5 Push, pull and run on another Docker installation

On my machine:

```
docker push denisle1406/swe40006-cli:latest
```

On the second device:

```
docker pull denisle1406/swe40006-cli:latest
docker run --rm denisle1406/swe40006-cli:latest --text "hello from another device"
```

![docker push output, or the Docker Hub repository page](photos/fig24.png)
*Figure 24. CLI tool image on Docker Hub.*

![docker pull and docker run on the second device](photos/fig25.png)
*Figure 25. CLI tool pulled and run on another Docker device.*

---

## 9. Errors Encountered and How I Fixed Them

### 9.1 `tag does not exist` when pushing to Docker Hub

**Error**

```
C:\...\Assignment4>docker push denisle1406/swe40006:tagname
The push refers to repository [docker.io/denisle1406/swe40006]
tag does not exist: denisle1406/swe40006:tagname
```

I got the same error for the tags `hello` and `latest`.

**Investigation**

The build output in Figure 5 ended with `naming to docker.io/library/hello-world-py:latest`. So the only local image was called `hello-world-py`, not `denisle1406/swe40006`. `docker push` can only upload an image that already exists locally under exactly that name and tag. Naming a tag in a push command does not create it. I had copied `tagname` from the example command on the Docker Hub page (Figure 11), where it is only a placeholder.

**Fix**

I gave the existing image a second name with `docker tag`, checked it with `docker images`, and pushed again:

```
docker tag hello-world-py denisle1406/swe40006:latest
docker images
docker push denisle1406/swe40006:latest
```

![tag does not exist errors, then docker tag, docker images and a successful push](photos/push-to-dockerhub.png)
*Figures 26 and 27. Three failed pushes, then the fix: `docker tag`, `docker images`, and a successful `docker push`.*

`docker images` lists both names with the **same image ID** (`f0664deca1b9`) and size (177 MB). This shows that `docker tag` does not copy the image. It only adds another name that points to the same image.

For the later images I built directly with the Docker Hub name (`docker build -t denisle1406/swe40006-web:latest .`), so the error did not happen again (Figure 8).

### 9.2 `unknown command: docker docker`

**Error** (also visible in Figure 27)

```
C:\...\Assignment4>docker docker push denisle1406/swe40006:latest
docker: unknown command: docker docker
```

**Cause:** I typed `docker` twice. Docker read the second `docker` as a sub-command, which does not exist.

**Fix:** I ran the command again with one `docker`, and the push succeeded.

### 9.3 `docker build` printed its usage message

**Problem:** The top of Figure 5 shows `Usage: docker buildx build [OPTIONS] PATH | URL | -` from an earlier build attempt. Docker prints this when `docker build` is run without a build context.

**Cause:** The build context is the final `.` in `docker build -t hello-world-py .`. It tells Docker which folder to send to the builder and where to find the Dockerfile. Without it, Docker has nothing to build.

**Fix:** I added the `.` at the end of the command, and the build finished (9/9 steps).

### 9.4 Play with Docker is no longer available

**Problem:** I planned to use Play with Docker (https://labs.play-with-docker.com) as the second Docker device, but the service has been stopped.

**Fix:** I pushed every image to Docker Hub and pulled it on `[DESCRIBE THE SECOND DEVICE]` instead. Any machine with Docker installed can pull a public image from Docker Hub, so the result is the same: the second device runs the app without any of my source code.

### 9.5 Other issues

`[ADD ANY OTHER ERRORS YOU MEET, e.g. port already in use, docker login failure, firewall blocking the port. For each one, give: the error text, why it happened, and how you fixed it. Delete this section if there are none.]`

---

## 10. What I Learned

- **An image is a portable package of an app plus its runtime.** The host never needed Python or Node.js installed. The `FROM` line brings the runtime into the image.
- **Image names decide where a push goes.** A name without a username (`hello-world-py`) is local only. A name like `denisle1406/swe40006` maps to my Docker Hub repository. `docker tag` adds a name without copying the image.
- **Layers are cached and shared.** The second Python image built in 3.1 s instead of 18.2 s because the `python:3.12-slim` layers were already on the machine.
- **Containers have their own network.** A server must bind to `0.0.0.0`, and `-p host:container` must be used, before a browser on the host can reach it.
- **`CMD` and `ENTRYPOINT` serve different apps.** `CMD` suits servers that always start the same way. `ENTRYPOINT` suits command-line tools that take arguments.
- **Volumes let a container read host files** without rebuilding the image.

---

## 11. Summary

| Task | Requirement | Status | Evidence |
|---|---|---|---|
| 4.1 | Docker account | Done | Figures 1, 11 |
| 4.1 | Docker client installed | Done | Figures 2, 3, 5 |
| 4.1 | Hello-world deployed | Done | Figures 4, 4a, 4b, 5, 6 |
| 4.2 | Python app with runtime | Done | Figures 5, 6, 7, 27 |
| 4.2 | Python app pushed to Docker Hub | Done | Figures 11, 27 |
| 4.2 | Hello-world web server | Done | Figures 7a, 7b, 8, 9, 10 |
| 4.2 | Pulled to another device | Done | Figures 12, 13 |
| 4.3 | New web app (Node.js) | Done | Figures 14 to 19 |
| 4.4 | Non-web app (CLI tool) | Done | Figures 20 to 25 |

All source code is at https://github.com/denisle06/cos40006-ass4. The Docker commands for each task are in each folder's `command.txt`.
