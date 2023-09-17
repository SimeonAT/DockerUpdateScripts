from common import *

class Service:

  def __init__(self, client, json_path):
    self.client = client
    self.images = read_json(json_path)
    return

  def download(self):
    for name in self.images:
      tag = self.images[name]
      self.client.images.pull(name, tag=tag)

      print(f'Successfully pulled {name}:{tag}')
    return

  def delete(self):
    for name in self.images:
      tag = self.images[name]
      tagged_name = f'{name}:{tag}'
      self.client.images.remove(tagged_name)

      print(f'Deleted {name}')
    return