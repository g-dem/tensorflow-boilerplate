FROM tensorflow/tensorflow

ENV DEBIAN_FRONTEND noninteractive

RUN useradd -m vscode
ENV HOME /home/vscode

RUN apt-get update && \
    apt-get install -y \
    # git \
    # openssh-client \ 
    python3 python3-dev python3-pip \
    libxft-dev libfreetype6 libfreetype6-dev \
    python3-tk
    
RUN pip3 install matplotlib

COPY . /app