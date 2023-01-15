# CUDA Ubuntu
# https://gitlab.com/nvidia/cuda/blob/ubuntu16.04/9.0/base/Dockerfile

FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

# copy all files from the current directory to the container
COPY yolov7 /app

# install python3 and pip3
RUN apt-get update && apt-get install -y python3 python3-pip

# set the working directory to /app
WORKDIR /app
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Receive 
RUN python3 train.py --workers 8 --device 0 --batch-size 32 --data data/penguins.yaml --img 640 640 --cfg cfg/training/yolov7.yaml --weights yolov7_training.pt --name yolov7 --hyp data/hyp.scratch.p5.yaml
