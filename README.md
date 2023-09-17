# Scripts for Updating Docker Containers

This repository contains Pythons scripts that I have written in order to *automate* the process of updating the Docker containers that run in my self-hosted server. Detailed information about these Python scripts can be found in my [blog post](https://simeonat.github.io/year-archive/).


# Instructions

The Python scripts updates a given Docker container by:

1. Stopping and deleting the specified container
2. Deleting the image that the container was running
3. Pulls the image from the Docker Hub
4. Starts a new container from the image pulled in step (3)

Configuration settings for containers and images are saved in the `data/container.json` and `data/image.json` [data](https://github.com/SimeonAT/DockerUpdateScripts/tree/main/data), respectively.

Furthermore, these scripts are designed to run on the same machine in that will be running the specified the Docker containers. Although it is [possible to update the Docker containers of a remote machine](https://docs.docker.com/config/daemon/remote-access/), this is feature is not implemented in order to keep the scripts as straightforward as possible. 

However, I may implement this additional feature to these scripts in the future. 

## Setting up the Configurations

You will need to go into the [data](https://github.com/SimeonAT/DockerUpdateScripts/tree/main/data) directory and *modify* the JSON files with information about the images and containers that you will like the Python scripts to update.

### Images

The `image.json` [file](https://github.com/SimeonAT/DockerUpdateScripts/blob/main/data/image.json) should contain a mapping between the *name* of the image to update and the *tag* that corresponds to the specified version of the image to pull from the Docker Hub.

In order words, the format should look like as follows:
```json
{
  "image name": "image tag",
}
```

I have included the specific images that personally update as an example on how the JSON file should be formatted.
```json
{
  "vaultwarden/server": "latest",
  "gitea/gitea": "nightly"
}
```

### Containers

The `container.json` [file](https://github.com/SimeonAT/DockerUpdateScripts/blob/main/data/container.json) should map a specific image name to a JSON representing the settings the corresponding container should run. The file contains two examples in order to display what the configurations should look like.

Let us examine one of the examples I have placed in the file.
I personally use this configuration for the Vaultwarden Docker container that I run in my self-hosted server.

```json
{
  "vaultwarden/server": {
    "tag": "latest",
    "ports": {
      "80/tcp": [Insert port number]
    },
    "volumes": {
      "[path on your machine to store container data]": {"bind": "/data", "mode": "rw"}
    }
  },
}
```

The key is the *name* of the image: `vaultwarden/server`, and the value is the configurations for the container running this image.

The current supported configurations are as follows:
* The *tag* of the image to be used.
* A mapping of the *virtual ports* used by the containers to the *actual ports* to be used on the server.
* The configurations of the *actual volumes* to be used by the container, mapped to the *virtual volumes* in file system of the container.

These configurations will be passed to the Docker `container.run()` [function](https://github.com/SimeonAT/DockerUpdateScripts/blob/main/scripts/container.py#L18). The configurations that specify the `tag`, `ports`, and `volumes` for the container follows the format required by [function signature](https://docker-py.readthedocs.io/en/stable/containers.html#docker.models.containers.ContainerCollection.run) for `container.run()`.

## Running the Scripts

Once you have set up the configurations in the `container.json` and `image.json` files for the containers and images, respectively, you would like to update, you can now run `make main` in order to run automatically update your Docker containers.

### Running the Tests

If you would like to double check that your configurations are correct, you can run `make test` to run the test script. The test script will attempt to pull the Docker images and start each respective container. 

If the containers are successfully running, it will then delete the containers and the images it has downloaded. If there were any errors in the process, the test script will stop and print out an error message indicating the issue(s) that have occured.

Please note that the test script *assumes* that you are not currently running containers that you have defined in `container.json`. If this is not the case, then the test script will not function properly.
