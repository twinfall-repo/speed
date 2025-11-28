# Use the official Ubuntu image as a base
FROM --platform=linux/amd64 ubuntu:latest

# Set the working directory
ARG USERNAME=user
ARG HOME_DIR=/home/${USERNAME}
ENV HOME=${HOME_DIR}
WORKDIR ${HOME}

# Set environment variables to prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install sudo
RUN sed -i 's/^# deb/deb/' /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get install -y \
    openmpi-bin openmpi-common libopenmpi-dev \
    libmetis5 libmetis-dev \
    wget git bash apt-utils build-essential gfortran bzip2 ca-certificates 
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Use bash shell instead
SHELL ["/bin/bash", "-c"]

# Create a non-root user and add to sudoers
RUN useradd -m -d ${HOME_DIR} ${USERNAME}
RUN echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN chown -R ${USERNAME}:${USERNAME} ${HOME_DIR}

# Switch to the non-root user
USER ${USERNAME}

# Clone the speed repo
WORKDIR ${HOME}
ENV SPEED_FOLDER=${HOME}/speed
RUN git clone https://bitbucket.org/ilmaz/speed.git ${SPEED_FOLDER}

# Fix the makefile of speed
WORKDIR ${SPEED_FOLDER}
RUN sed -i 's|^METIS_INCLUDE_FLAGS.*|METIS_INCLUDE_FLAGS = -I/usr/include|' Makefile
RUN sed -i 's|^METIS_LD_FLAGS.*|METIS_LD_FLAGS = -L/usr/lib/x86_64-linux-gnu -lmetis|' Makefile

# Run the make
RUN make
ENV PATH="${HOME}/speed:${PATH}"

# Download the test cases
WORKDIR ${HOME}
RUN git clone https://bitbucket.org/ilmaz/speed-tutorials.git

# Donwload the support scripts
WORKDIR ${HOME}
RUN git clone git@github.com:twinfall-repo/speed-repo.git