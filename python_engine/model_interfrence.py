import pandas as pd
class InflationPredictorEngine:
    def __init__(self,model_trained, preprocessor):
        self.model = model_trained
        self.preprocessor= preprocessor
    
    def execute_inference(self,year,month,wpi,oil,inr,iip):
        #preprocess the data
        cyclical_month = self.preprocessor.cyclical_month(month)
        features_scaled = self.preprocessor.transform_features(year,wpi,oil,inr,iip)
        features_scaled.extend(cyclical_month)
        features_matrix = pd.DataFrame([features_scaled])
        # make prediction - convert to numpy array for XGBoost
        predicted_inflation = self.model.predict(features_matrix.values)[0]
        return float(predicted_inflation)