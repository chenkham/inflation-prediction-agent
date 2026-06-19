import numpy as np

class InflationDataPreprocesssor:
    def __init__(self, year_scaler, feature_scaler):
        self.year_scaler = year_scaler
        self.feature_scaler = feature_scaler
    
    def cyclical_month(self, month: float)->tuple:
        sin_vector = np.sin(2 * np.pi * month / 12)
        cos_vector = np.cos(2 * np.pi * month / 12)
        return sin_vector, cos_vector
    
    def transform_features (self, year:float, wpi: float, oil:float, inr:float, iip:float)->list:
        scaled_year = self.year_scaler.transform([[year]])[0][0]
        scaled_total = self.feature_scaler.transform([[wpi, oil, inr, iip]])[0]
        #unpack
        scaled_wpi, scaled_oil, scaled_inr, scaled_iip = scaled_total
        return [scaled_year, scaled_wpi, scaled_oil, scaled_inr, scaled_iip]