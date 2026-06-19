import sys
import joblib
from python_engine.preprocessing import InflationDataPreprocesssor
from python_engine.model_interfrence import InflationPredictorEngine

def main():
    if len(sys.argv) < 7:
        print("CRITICAL: Incomplete system arguments passed from caller pipeline.", file=sys.stderr)
        sys.exit(1)
    
    try:
        #load models
        model = joblib.load("models/xgb_inflation_model.pkl")
        year_scaler = joblib.load("models/year_scaler.pkl")
        feature_scaler = joblib.load("models/feature_scaler.pkl")
         
        #initialize preprocessor and inference engine
        preprocessor = InflationDataPreprocesssor(year_scaler, feature_scaler)
        inference_engine = InflationPredictorEngine(model, preprocessor)

        #parse input features
        prediction = inference_engine.execute_inference(
            year=float(sys.argv[1]), month=float(sys.argv[2]), wpi=float(sys.argv[3]),
            oil=float(sys.argv[4]), inr=float(sys.argv[5]), iip=float(sys.argv[6])
        )
        print(f"{prediction:.4f}")

    except Exception as error:
        print(f"FATAL ERROR: Python Inference Layer Error -> {str(error)}", file=sys.stderr)
        sys.exit(1)
    
if __name__ == "__main__":
    main()