import image
import container
import test
from common import *

"""
  End-to-end tests to determine whether the functionality of
  the Image and Container services are properly working.

  The tests assume that no Docker Images or Containers have been
  downloaded.
"""
if __name__ == '__main__':
  client = connect()
  image_service = image.Service(client, IMAGES_PATH)
  container_service = container.Service(client, CONTAINERS_PATH)
  test_service = test.Service(client, IMAGES_PATH, CONTAINERS_PATH)

  # Can the Docker Images be downloaded?
  image_service.download()
  test_service.images_exist()

  # Can we run the Docker Containers with our specified settings?
  container_service.run()
  test_service.containers_running()

  # Can we stop and delete the Docker Containers?
  container_service.delete()
  test_service.containers_deleted()

  # Can we delete the Docker Images?
  image_service.delete()
  test_service.images_deleted()