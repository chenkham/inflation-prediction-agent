import tkinter as tk
from tkinter import messagebox
import joblib

# Import your exact OOP classes from your python_engine folder
from python_engine.preprocessing import InflationDataPreprocesssor
from python_engine.model_interfrence import InflationPredictorEngine

class InflationAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Macroeconomic Inflation Predictor")
        self.root.geometry("450x520")
        self.root.configure(bg="#f5f6fa") # Clean light gray background

        # 1. Initialize core ML pipeline using your exact logic
        try:
            model = joblib.load("models/xgb_inflation_model.pkl")
            year_scaler = joblib.load("models/year_scaler.pkl")
            feature_scaler = joblib.load("models/feature_scaler.pkl")
            
            preprocessor = InflationDataPreprocesssor(year_scaler, feature_scaler)
            self.inference_engine = InflationPredictorEngine(model, preprocessor)
        except Exception as e:
            messagebox.showerror("System Error", f"Failed to load engine components: {str(e)}")
            self.root.destroy()

        # 2. UI Layout - Title Banner
        title_lbl = tk.Label(root, text="Inflation Forecasting System", font=("Arial", 14, "bold"), bg="#1a73e8", fg="white", pady=12)
        title_lbl.pack(fill=tk.X)

        # 3. Dynamic Entry Fields Creation
        self.labels_text = ["Target Year (e.g., 2026):", "Target Month (1-12):", "WPI Index:", "Global Oil Price (USD):", "USD to INR Rate:", "IIP Index:"]
        self.entries = {}

        # Loop to automatically draw entry fields cleanly
        for text in self.labels_text:
            frame = tk.Frame(root, bg="#f5f6fa", pady=6)
            frame.pack(fill=tk.X, padx=25)
            
            lbl = tk.Label(frame, text=text, font=("Arial", 10), bg="#f5f6fa", width=22, anchor="w")
            lbl.pack(side=tk.LEFT)
            
            entry = tk.Entry(frame, font=("Arial", 10), width=18, bd=1, relief="solid")
            entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)
            self.entries[text] = entry

        # 4. Interactive Forecast Calculation Button
        self.predict_btn = tk.Button(root, text="Run XGBoost Forecast", font=("Arial", 11, "bold"), bg="#2ecc71", fg="white", activebackground="#27ae60", activeforeground="white", cursor="hand2", padx=10, pady=5, command=self.calculate_prediction)
        self.predict_btn.pack(pady=25)

        # 5. Output Visual Results Window Display Banner
        self.result_lbl = tk.Label(root, text="Predicted Inflation: -- %", font=("Arial", 15, "bold"), bg="#f5f6fa", fg="#2c3e50")
        self.result_lbl.pack()

    def calculate_prediction(self):
        try:
            # Gather inputs typing strings from form text input boxes maps
            yr = float(self.entries["Target Year (e.g., 2026):"].get())
            mo = float(self.entries["Target Month (1-12):"].get())
            wpi = float(self.entries["WPI Index:"].get())
            oil = float(self.entries["Global Oil Price (USD):"].get())
            inr = float(self.entries["USD to INR Rate:"].get())
            iip = float(self.entries["IIP Index:"].get())

            # Direct input routing straight to your architecture engine methods instance
            prediction_output = self.inference_engine.execute_inference(
                year=yr, month=mo, wpi=wpi, oil=oil, inr=inr, iip=iip
            )
            
            # Update output graphic results text banner elements dynamically 
            self.result_lbl.config(text=f"Predicted Inflation: {prediction_output:.4f}%", fg="#1a73e8")

        except ValueError:
            messagebox.showwarning("Input Validation Error", "Invalid input detected. Please ensure all values entered are real numbers.")
        except Exception as runtime_error:
            messagebox.showerror("Pipeline Execution Failure", f"Error during model pipeline processing:\n{str(runtime_error)}")

if __name__ == "__main__":
    main_window = tk.Tk()
    app = InflationAppGUI(main_window)
    main_window.mainloop()
