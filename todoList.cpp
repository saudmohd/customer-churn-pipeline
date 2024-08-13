#include <iostream>
#include <fstream>
#include <vector>
#include <string>

void showTasks(const std::vector<std::string>& tasks) {
    for (const auto& task : tasks) {
        std::cout << task << std::endl;
    }
}

int main() {
    std::vector<std::string> tasks;
    std::string fileName = "./txtfile.txt";

    // Open the file
    std::ifstream inputFile(fileName);
    if (!inputFile) {
        std::cerr << "Unable to open file: " << fileName << std::endl;
        return 1; // Exit the program with an error code
    }

    // Read the file line by line
    std::string line;
    while (std::getline(inputFile, line)) {
        tasks.push_back(line);
    }

    // Close the file
    inputFile.close();

    // Show the tasks
    showTasks(tasks);

    return 0; // Exit the program successfully
}
