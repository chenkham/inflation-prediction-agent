#ifndef DATABASE_MANAGER_HPP
#define DATABASE_MANAGER_HPP

#include "FeatureRecord.hpp"
#include <string>

class DatabaseManager {
public:
    virtual ~DatabaseManager() = default;
    virtual bool connect(const std::string& connectionStr) = 0;
    virtual bool logForecastRecord(const FeatureRecord& record) = 0;
    virtual void disconnect() = 0;
};

#endif//DATABASE_MANAGER_HPP