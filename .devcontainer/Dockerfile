# Base Image
FROM python:3.12.4-bookworm

# If the steps of a `Dockerfile` use files that are different from the `context` file, COPY the
# file of each step separately; and RUN the file immediately after COPY
WORKDIR /app

COPY /.devcontainer/requirements.txt /app
RUN apt update && apt -q -y upgrade && apt -y install sudo && sudo apt -y install graphviz && \
	pip install --upgrade pip && \
    pip install --requirement /app/requirements.txt --no-cache-dir

# Port
EXPOSE 8050

# ENTRYPOINT
ENTRYPOINT ["bash"]
