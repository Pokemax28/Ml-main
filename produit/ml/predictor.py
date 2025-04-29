import joblib
import os

# Chargement du modèle
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(model_path)

# Fonction de prédiction
def predict_price(surface):
    surface = float(surface)
    return model.predict([[surface]])[0]
