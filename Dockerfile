FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-devel

RUN apt-get update

RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt install python3.7 -y
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
RUN update-alternatives --set python /usr/bin/python3.7

RUN apt-get -y install libcurl3-gnutls libgl1-mesa-glx libsm6 libxext6 ffmpeg sudo vim wget
RUN apt-get -y update
RUN add-apt-repository ppa:ubuntu-toolchain-r/test
#RUN apt-get -y update
#RUN apt-get -y install gcc-4.9
#RUN apt-get -y upgrade libstdc++6

RUN pip uninstall -y torch torchvision
RUN pip install torch==1.1.0 torchvision==0.3.0
RUN pip install pycocotools scipy==1.1.0 sklearn opencv-python easydict tensorboardX

RUN wget https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN apt-get -y update
RUN apt-get -y install blobfuse

RUN mkdir /mnt/resource/blobfusetmp -p
RUN mkdir /mnt/cvgroupsouthcentral
