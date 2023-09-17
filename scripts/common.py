import docker
import os
import json

IMAGES_PATH = os.path.join(os.curdir, 'data', 'image.json')
CONTAINERS_PATH = os.path.join(os.curdir, 'data', 'container.json')

def read_json(json_path):
  with open(json_path, 'r') as json_file:
    return json.loads(
      json_file.read()
    )

def connect():
  client = docker.from_env()
  print('Connected to client')
  return client

"""
  Container names will have the same name
  as the Image they are running, but with all
  instance of "/" replaced with "-" to meet
  Docker container naming requirements.
"""
def get_container_name(image_name):
  return image_name.replace('/', '-')

"""
  If a tag for a Docker image is not "latest" and
  not explicitly specified, Docker will attempt
  to pull the "latest" version of the image and
  run a new container from "latest" instead.
"""
def get_running_name(image_name, tag):
  if tag != 'latest':
    return image_name + f':{tag}'
  else:
    return image_name