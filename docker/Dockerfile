FROM ubuntu:20.04
WORKDIR /discord_bot

# Install python3.9
RUN apt update && \
    apt -y install software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt update && \
    apt -y install python3.9

# Set default python3.9
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

# Install ssh, git, pip, venv, sshpass, nano
RUN apt update && \
    apt-get -y install git openssh-client python3-pip python3.9-dev python3.9-venv sshpass openssh-server nano tmux &&\
    pip install -U black

# Install ping
RUN apt-get update && apt-get install -y iputils-ping

# Create virtual environments
ADD ./requirements.txt /discord_bot/
RUN python3 -m venv /discord_bot/vir_env
RUN . /discord_bot/vir_env/bin/activate && pip3 install -r /discord_bot/requirements.txt

WORKDIR /discord_bot/PIF_discord_bot