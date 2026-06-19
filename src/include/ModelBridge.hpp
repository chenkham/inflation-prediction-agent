#ifndef MODEL_BRIDGE_HPP
#define MODEL_BRIDGE_HPP

#include <iostream>
#include "FeatureRecord.hpp"
#include <string>
#include <memory>
#include <cstdio>

class ModelBridge {
public:
    double predictInflation(const FeatureRecord& record) {
        // Safely parse object parameters straight to clean system commands
        std::string command = "python3 predict.py " +
                              std::to_string(record.getYear()) + " " +
                              std::to_string(record.getMonth()) + " " +
                              std::to_string(record.getWpi()) + " " +
                              std::to_string(record.getOilPriceUsd()) + " " +
                              std::to_string(record.getUsdInrRate()) + " " +
                              std::to_string(record.getIipIndex());

        std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(command.c_str(), "r"), pclose);
        if (!pipe) {
            throw std::runtime_error("Fatal Error: Pipe execution failure inside C++ Subsystem.");
        }
        char buffer[128];
        std::string internalOutput = "";
        while (fgets(buffer, sizeof(buffer), pipe.get()) != nullptr) {
            internalOutput += buffer;
        }

        return std::stod(internalOutput);
    }
};

#endif