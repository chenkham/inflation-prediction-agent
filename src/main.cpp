#include "include/DatabaseManager.hpp"
#include "include/FeatureRecord.hpp"
#include "include/ModelBridge.hpp"
#include "include/MYSQLManager.hpp"

#include <iostream>
#include <memory>

FeatureRecord::FeatureRecord(int year, int month, double wpi, double oilPriceUsd, double usdInrRate, double iipIndex)
    : year(year), month(month), oilPriceUsd(oilPriceUsd), usdInrRate(usdInrRate), iipIndex(iipIndex), predictedInflation(0.0) {}

    int FeatureRecord::getYear() const { return year; }
    int FeatureRecord::getMonth() const { return month; }
    double FeatureRecord::getWpi() const { return wpi; }
    double FeatureRecord::getOilPriceUsd() const { return oilPriceUsd; }
    double FeatureRecord::getUsdInrRate() const { return usdInrRate; }
    double FeatureRecord::getIipIndex() const { return iipIndex; }
    void FeatureRecord::setPredictedInflation(double prediction) { predictedInflation = prediction; }
    double FeatureRecord::getPredictedInflation() const { return predictedInflation; }

int main(int argc, char* argv[])
{
    std::cout<<"Starting Inflation Prediction System...\n";
    // Step 1: Create a feature record with sample data
    FeatureRecord record(2024, 6, 150.5, 70.25, 74.5, 120.0);
    // Step 2: Use ModelBridge to predict inflation
    ModelBridge modelBridge;
    try
    {
       double resultOutput = modelBridge.predictInflation(record);
       record.setPredictedInflation(resultOutput);
        std::cout << "================================================\n";
        std::cout << "PROCESSED MODEL PREDICTION: " << record.getPredictedInflation() << "%\n";
        std::cout << "================================================\n\n";

        // 3. Persist states directly to external engine via polymorphic interfaces
        std::unique_ptr<DatabaseManager> db = std::make_unique<MySQLManager>();
        if(db->connect("server=localhost;port=3306;uid=root;pwd=secret")) {
            db->logForecastRecord(record);
            db->disconnect();
        }
    }
    catch (const std::exception& error) {
        std::cerr << "Process runtime system execution failure: " << error.what() << "\n";
        return 1;
    }
    
    return 0;
}
