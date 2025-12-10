using Docker.DotNet;
using System;
using System.Threading.Tasks;

// Very basic stub needs built out
public class DockerInteraction
{
    public static async Task Main(string[] args)
    {
        // Connect to the Docker daemon on Linux via Unix socket
        DockerClient client = new DockerClientConfiguration(
            new Uri("unix:///var/run/docker.sock"))
            .CreateClient();

        // Now you can interact with the Docker client
        // For example, list running containers:
        var containers = await client.Containers.ListContainersAsync(
            new Docker.DotNet.Models.ContainersListParameters() { Limit = 10 });

        foreach (var container in containers)
        {
            Console.WriteLine($"Container ID: {container.ID}, Name: {container.Names[0]}");
        }
    }
}
