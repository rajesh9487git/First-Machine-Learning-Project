# First-Machine-Learning-Project

Software requirements:

1. Github account
2. Heroku account
3. Git cli
4. Visual studio code

Create conda env

conda create -p venv python==3.7 -y

To activate the env use below command

conda activate venv/

Then create requirements.txt file, then install the libraries using this file

pip install -r requirements.txt

To setup CI/CD pipeline in heroku we need below 3 information

1. HEROKU_EMAIL = rajesh9487@gmail.com
2. HEROKU_API_KEY = 58ec41d6-b180-4a79-8d1a-9d871dd1bcdc
3. HEROKU_APP_NAME = first-machine-learning-project

BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .
Note: Image name for docker must be lowercase

To list docker image

docker images
Run docker image

docker run -p 5000:5000 -e PORT=5000 f8c749e73678
To check running container in docker

docker ps
Tos stop docker conatiner

docker stop <container_id>
python setup.py install

Install ipykernel

pip install ipykernel
Data Drift: When your datset stats gets change we call it as data drift

Write a function to get training file path from artifact dir


