import image
import container
import test
from common import *

if __name__ == '__main__':
  client = connect()
  image_service = image.Service(client, IMAGES_PATH)
  container_service = container.Service(client, CONTAINERS_PATH)
  test_service = test.Service(client, IMAGES_PATH, CONTAINERS_PATH)

  try:
    test_service.images_exist()
    test_service.containers_running()

    container_service.delete()
    image_service.delete()
  except:
    print(
      'Images and Containers not present - no need for deletions'
    )

  image_service.download()
  container_service.run()