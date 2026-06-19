"""
Model Loader - Loads your trained ML model
"""
import joblib
import numpy as np
import os

class ModelLoader:
    def __init__(self):
        self.model = None
        self.encoder = None
        self.symptom_columns = None
        self.load_models()
    
    def load_models(self):
        """Load trained model files"""
        model_path = 'models/disease_model.pkl'
        encoder_path = 'models/disease_encoder.pkl'
        symptoms_path = 'models/symptom_columns.pkl'
        
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found at {model_path}")
        
        self.model = joblib.load(model_path)
        self.encoder = joblib.load(encoder_path)
        self.symptom_columns = joblib.load(symptoms_path)
        
        print(f"✅ Model loaded: {len(self.encoder.classes_)} diseases, {len(self.symptom_columns)} symptoms")
    
    def predict(self, symptom_list):
        """Predict disease from list of symptoms"""
        if not symptom_list:
            return []
        
        # Create binary vector
        symptom_vector = []
        for col in self.symptom_columns:
            if col in symptom_list:
                symptom_vector.append(1)
            else:
                symptom_vector.append(0)
        
        # Predict
        symptom_vector = np.array(symptom_vector).reshape(1, -1)
        probabilities = self.model.predict_proba(symptom_vector)[0]
        
        # Get top 5 predictions
        top_indices = np.argsort(probabilities)[-5:][::-1]
        
        predictions = []
        for idx in top_indices:
            confidence = probabilities[idx] * 100
            if confidence > 1:
                predictions.append({
                    'disease': self.encoder.inverse_transform([idx])[0],
                    'confidence': round(confidence, 2)
                })
        
        return predictions
    
    def get_all_symptoms(self):
        """Return all symptom names"""
        return self.symptom_columns
    
    def get_all_diseases(self):
        """Return all disease names"""
        return self.encoder.classes_.tolist()

# Singleton instance
model_loader = ModelLoader()