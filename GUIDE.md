# Task 4 Step-by-Step Guide

Follow the steps in order. Each 📸 marks a screenshot, numbered to match the figures in `REPORT.md`. Save them in the `photos/` folder as `fig01.png`, `fig02.png` and so on. That folder is in `.gitignore`, so the screenshots will not be pushed to GitHub.

Take screenshots with **Win + Shift + S**. Make sure the command you typed and its output are both visible.

Commands work in both Command Prompt and PowerShell unless a step says otherwise.

---

## Part A: Task 4.1 (Pass)

### Step 1. Docker Hub account

1. Sign in at https://hub.docker.com as `denisle1406`.
2. 📸 **Fig 1:** the Docker Hub home page with your username visible in the top right.

### Step 2. Start Docker Desktop

1. Open **Docker Desktop** from the Start menu and wait until the bottom-left status shows **Engine running**.
2. 📸 **Fig 2:** the Docker Desktop window showing *Engine running*.
3. Open a terminal and run:
   ```
   docker --version
   docker login
   ```
   `docker login` should end with `Login Succeeded`. If it opens a browser, approve the login there.
4. 📸 **Fig 3:** the `docker --version` output.

### Step 3. Official hello-world

```
docker run hello-world
```

📸 **Fig 4:** the output containing `Hello from Docker!`.

### Step 4. Your own Python hello-world

```
cd "C:\Swinburne Class\Software Deployment\Assignment4\python"
docker build -t hello-world-py .
docker run --rm hello-world-py
```

- 📸 **Fig 5:** the `docker build` output ending in `naming to docker.io/library/hello-world-py`.
- 📸 **Fig 6:** the `docker run` output showing `Hello, World!`.

---

## Part B: Task 4.2 (Credit)

### Step 5. Show the Python runtime image

```
docker images
```

📸 **Fig 7:** the list showing `hello-world-py`. The base image `python:3.12-slim` is the runtime that the `FROM` line installs.

### Step 6. Reproduce the push error (for Section 9.1)

Run this first. If the tag already exists from an earlier attempt, it gets deleted so that the error appears. An error here just means the tag wasn't there, which is fine.
```
docker rmi denisle1406/swe40006-python:latest
```

Now try to push before tagging:
```
docker push denisle1406/swe40006-python:latest
```

📸 **Fig 26:** the `tag does not exist` error.

### Step 7. Fix the error and push the Python app

```
docker tag hello-world-py denisle1406/swe40006-python:latest
docker images
docker push denisle1406/swe40006-python:latest
```

📸 **Fig 27:** `docker images` showing the new `denisle1406/swe40006-python` row, followed by the successful push.

### Step 8. Build and run the web server

```
cd "C:\Swinburne Class\Software Deployment\Assignment4\webserver"
docker build -t denisle1406/swe40006-web:latest .
docker run --rm -p 8000:8000 denisle1406/swe40006-web:latest
```

- 📸 **Fig 8:** the `docker build` output.
- Open http://localhost:8000 in a browser. It should show `Hello, World!`.
- 📸 **Fig 9:** the browser and the terminal side by side.
- Press **Ctrl + C** in the terminal to stop the server.

### Step 9. Push the web server

```
docker push denisle1406/swe40006-web:latest
```

- 📸 **Fig 10:** the push output. Scroll up so the Python push from Step 7 is visible too, or take one screenshot of each and place them together.
- Open https://hub.docker.com/r/denisle1406/swe40006-web. If it shows **Private**, change it to **Public** under *Settings*.
- 📸 **Fig 11:** the repository page showing the `latest` tag.

### Step 10. Pull on another device (you do this on the second device)

The second device needs Docker installed. No login is needed if the repositories are public.

```
docker pull denisle1406/swe40006-python:latest
docker run --rm denisle1406/swe40006-python:latest
docker pull denisle1406/swe40006-web:latest
docker run --rm -p 8000:8000 denisle1406/swe40006-web:latest
```

- 📸 **Fig 12:** the pulls completing and `Hello, World!` from the Python app.
- Open http://localhost:8000 on the second device.
- 📸 **Fig 13:** the browser showing `Hello, World!`.

The steps for 4.3 and 4.4 below also have second-device steps (Steps 13 and 17). You can do all the second-device work in one sitting at the end.

---

## Part C: Task 4.3 (Distinction)

### Step 11. Build and run the Node.js web app

```
cd "C:\Swinburne Class\Software Deployment\Assignment4\new-web-app"
docker build -t denisle1406/swe40006-node:latest .
docker run --rm -p 3000:3000 denisle1406/swe40006-node:latest
```

- 📸 **Fig 14:** the `docker build` output.
- 📸 **Fig 15:** the browser at http://localhost:3000. The page shows a heading and the server time.
- 📸 **Fig 16:** the browser at http://localhost:3000/api/time showing JSON.
- Press **Ctrl + C** to stop.

### Step 12. Push the Node.js app

```
docker push denisle1406/swe40006-node:latest
```

📸 **Fig 17:** the push output, or https://hub.docker.com/r/denisle1406/swe40006-node (make sure it is public).

### Step 13. Deploy on the second device

```
docker pull denisle1406/swe40006-node:latest
docker run --rm -p 3000:3000 denisle1406/swe40006-node:latest
```

- 📸 **Fig 18:** the pull and run in the terminal.
- 📸 **Fig 19:** the browser on that device at http://localhost:3000.

---

## Part D: Task 4.4 (High Distinction)

### Step 14. Build and run the CLI tool

```
cd "C:\Swinburne Class\Software Deployment\Assignment4\non-web-app"
docker build -t denisle1406/swe40006-cli:latest .
docker run --rm denisle1406/swe40006-cli:latest --text "the cat saw the dog and the dog saw the cat"
docker run --rm denisle1406/swe40006-cli:latest --help
```

- 📸 **Fig 20:** the `docker build` output.
- 📸 **Fig 21:** the `--text` output (characters, words, lines, most common words).
- 📸 **Fig 22:** the `--help` output.

### Step 15. Read a file through a volume mount

Run the command for your terminal from inside the `non-web-app` folder.

Command Prompt:
```
docker run --rm -v "%cd%":/data denisle1406/swe40006-cli:latest --file /data/sample.txt --top 5
```

PowerShell:
```
docker run --rm -v "${PWD}:/data" denisle1406/swe40006-cli:latest --file /data/sample.txt --top 5
```

📸 **Fig 23:** the output. It should show `the: 4` at the top.

### Step 16. Push the CLI tool

```
docker push denisle1406/swe40006-cli:latest
```

📸 **Fig 24:** the push output, or https://hub.docker.com/r/denisle1406/swe40006-cli (make sure it is public).

### Step 17. Run on the second device

```
docker pull denisle1406/swe40006-cli:latest
docker run --rm denisle1406/swe40006-cli:latest --text "hello from another device"
```

📸 **Fig 25:** the pull and the statistics output.

---

## Part E: Finish the report

1. In `REPORT.md`, fill in the placeholders in square brackets:
   - Student ID, full name, semester, due date, submission date (Sections 1 and 2).
   - `[DESCRIBE THE DEVICE ...]` in Section 6.4 and `[DESCRIBE THE SECOND DEVICE]` in Section 9.2, for example "a second laptop running Docker Desktop on Windows 11".
   - In the Section 10 summary table, change `[Confirm]` to `Done` once Step 10 works.
   - Section 9.3: add any other error you met (error text, cause, fix), or delete the section and Fig 28.
2. Replace each 📸 placeholder line with its screenshot. Keep the caption under the image.
3. Check that all four Docker Hub repositories are **Public** by opening each link in Section 4 in a private browser window.
4. Export the report to PDF (or Word) for submission.

### If something goes wrong

| Problem | Fix |
|---|---|
| `error during connect ... dockerDesktopLinuxEngine` | Docker Desktop is not running. Start it and wait for *Engine running*. |
| `denied: requested access to the resource is denied` on push | Run `docker login` again, and make sure the image name starts with `denisle1406/`. |
| `port is already allocated` | An earlier container is still running. Run `docker ps`, then `docker stop <container id>`. |
| Browser cannot reach `localhost:8000` or `localhost:3000` | Check you used `-p 8000:8000` / `-p 3000:3000` and that the container is still running. |
| Second device: `pull access denied` | The repository is private. Make it public on Docker Hub, or run `docker login` on that device. |

Any of these errors also counts as material for Section 9.3. Take a screenshot before you fix it.
