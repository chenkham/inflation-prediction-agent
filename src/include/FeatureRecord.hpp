#ifndef FEATURE_RECORD_HPP
#define FEATURE_RECORD_HPP

class FeatureRecord{
    private:
        int year;
        int month;
        double wpi;
        double oilPriceUsd;
        double usdInrRate;
        double iipIndex;
        double predictedInflation;

    public:
    //setting the getters and setters for the feature record class
        FeatureRecord(int year, int month, double wpi, double oilPriceUsd, double usdInrRate, double iipIndex);
        int getYear() const;
        int getMonth() const;
        double getWpi() const;
        double getOilPriceUsd() const;
        double getUsdInrRate() const;
        double getIipIndex() const;
        
        void setPredictedInflation(double prediction);
        double getPredictedInflation() const;

};
#endif//featureRecord.hpp