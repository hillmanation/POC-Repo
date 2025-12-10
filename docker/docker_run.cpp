#include <cstdlib> // For system()
#include <iostream>
#include <string>

// This is a stub example that needs built out
int main() {
    std::string command = "docker run hello-world"; // Example Docker command
    int result = std::system(command.c_str());

    if (result == 0) {
        std::cout << "Docker command executed successfully." << std::endl;
    } else {
        std::cerr << "Error executing Docker command." << std::endl;
    }
  
    return 0;
}
