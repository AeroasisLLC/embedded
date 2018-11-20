#!/bin/sh
# This is a comment!

apt-get update && apt-get upgrade


#install Git
sudo apt-get install git

# install virtualenv wrapper
echo Installing Virtual Environment
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/.cache/pip
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
# source profile
source ~/.profile
# create virtual environment
mkvirtualenv aeroasis -p python3

# move to virtualenv
source /usr/local/bin/virtualenvwrapper.sh
source ~/.profile
workon aeroasis

# upgrade pip
pip install --upgrade pip

# install packages using pip
echo Installing python packages..
pip install numpy  # install numpy
pip install schedule
pip install AWSIoTPythonSDK
apt-get install rpi.gpio
pip install configparser
pip install -U platformio
pip install schedule
pip install pyserial
pip install requests

# clone git repo
echo Cloning Git Repo...
cd ~
git clone https://github.com/AeroasisLLC/main_software.git
