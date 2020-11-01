## Sending and Reading Messages from Apache Kafka

This repository is a simple application that connect to Apache Kafka, create a topic, send and read messages.

---

### 1. Dependencies

#### 1.1. Python

[Download and install the python](https://www.python.org/downloads/).

#### 1.2. Docker Desktop

You would require you to install Docker Desktop to create containers for individual microservices. Refer the following links for instructions

- [macOS](https://docs.docker.com/docker-for-mac/install/),
- [Windows 10 64-bit: Pro, Enterprise, or Education](https://docs.docker.com/docker-for-windows/install/),
- [Windows 10 64-bit Home](https://docs.docker.com/toolbox/toolbox_install_windows/).
- You can find installation instructions for other operating systems at: https://docs.docker.com/install/

---

### 2. Instructions

To run any project code, youu will have to set up a virtual environment with project dependencies. All of following instructions are to be completed via a terminal/command line prompt.

#### 2.1. Install Python Dependencies

This project has a only dependency. It is setting in 'requirements.txt' file. To install dependency use follow command:

```bash
pip install r- requirements.txt
```

#### 2.2. Start Kafka (run on Docker)

Into 'scripts' folder run:

```bash
brew install hadolint
```

or

```bash
docker-componse up -d
```

#### 2.3. Running Python Application

This is simplest part of this tutorial. Run command bellow

```bash
python app.py
```

If you did all correctly, you get output similarly to image below.
<img src="">
