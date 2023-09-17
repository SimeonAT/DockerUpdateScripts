from common import *

class Service:

  def __init__(self, client, json_path):
    self.client = client
    self.containers = read_json(json_path)
    return

  def run(self):
    for image_name in self.containers:
      settings = self.containers[image_name]
      volumes = settings['volumes']
      ports = settings['ports']
      tag = settings['tag']

      running_name = get_running_name(image_name, tag)
      self.client.containers.run(
        name=get_container_name(image_name),
        image=running_name,
        ports=ports,
        volumes=volumes,
        detach=True
      )

      print(f'Container for {running_name} is now running')
    return

  def delete(self):
    for container in self.client.containers.list():
      container.stop()
      print(f'Stopping {container.name}')

      container.remove()
      print(f'Deleted {container.name}')
    return