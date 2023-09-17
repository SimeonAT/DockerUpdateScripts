from common import *

class Service:

  def __init__(self, client, image_path, container_path):
    self.client = client
    self.images = read_json(image_path)
    self.containers = read_json(container_path)
    return

  def _get_image_tag(self, image_name):
    return self.images[image_name]

  def images_exist(self):
    for image in self.images:
      tag = self._get_image_tag(image)
      name = f'{image}:{tag}'
      self.client.images.get(name)

      print(f'TEST: Image {name} has already been pulled')
    return

  def containers_running(self):
    for image_name in self.containers:
      name = get_container_name(image_name)

      container = self.client.containers.get(name)
      assert(container.status == 'running')

      print(f'TEST: Container {name} is running')
    return

  def containers_deleted(self):
    for image_name in self.containers:
      name = get_container_name(image_name)
      assert([] == self.client.containers.list(
        filters={"name": name}
      ))

      print(f'TEST: Container {name} is not present')
    return

  def images_deleted(self):
    for name in self.images:
      assert([] == self.client.images.list(name=name))

      print(f'TEST: Image {name} is not present')
    return
