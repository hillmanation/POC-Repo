import docker
import argparse
import subprocess
import sys
from datetime import datetime


# TODO: Add method for local OS checking and handling for syntax sanitizing
def check_for_docker():  # Check if Docker is installed and running/enabled
    try:
        # Check if docker is installed first
        subprocess.run(["docker", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Check if it is running
        subprocess.run(["docker", "info"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Initialize a Docker client for image checking
        client = docker.from_env()
        return client
    except subprocess.CalledProcessError:
        print("Docker is either not installed or not running, exiting...")
        sys.exit(1)


def check_and_pull_images(image_names):  # Check if the requested Docker image is available, and if not pull it
    for image_name in image_names:
        try:
            client.images.get(image_name)  # Check the local image repo for the image
        except docker.errors.ImageNotFound:
            print(f"Docker image '{image_name}' not found locally. Pulling from Docker Hub...")
            try:
                # Pull from Docker Hub
                client.images.pull(image_name)
                print(f"Successfully pulled '{image_name}' from Docker Hub, moving on...")
            except docker.errors.APIerror as e:
                print(f"Error pulling image '{image_name}': {str(e)}")
                sys.exit(1)


# Start requested container instance
def start_container(image_name, instance_name=image_name, headless: bool = False, remove_on_stop: bool = False, command_args):
    try:
        download_client = self.client.containers.run(
            image_name,  # Docker Image name
            detach=headless,  # Run in detached mode
            name=instance_name,  # Name of Container instance
            volumes={self.volume_mapping: {"bind": "/mnt", "mode": "rw"}},  # Local volume mapping (if that is needed for the image)
            remove=remove_on_stop,  # Remove after container process stops
            command=command_args  # Pass any in-line command line arguments to the docker image
        )
        print(
            f"Started container '{instance_name}' @ {datetime.now().strftime('%H:%M:%S')} with ID: "
            f"{download_client.id}")
        return instance_name  # Return for tracking
    except docker.errors.APIError as e:
        print(f"Error starting container '{instance_name}': {str(e)}")
        return None


def main():  # TODO: Add console/log output to inform user of container spin up stated and status
  # Declare in scope variables (These can be configured with arguments too)
  desired_image = "example/docker-image"

  # Check that Docker is available locally
  check_for_docker()

  # Check for the requested image
  check_and_pull_images(desired_image)

  # Next we want to run the docker image, I'm hard coding the arguments here but they can be done as arguments on this script with argparser
  start_container(desired_image, "docker_run.py", False, False, '--verbose --example-int-input 67')

  
