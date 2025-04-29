# test_model.py
import joblib

# Charger le modèle
model = joblib.load('model.pkl')

# Exemple : prédire le prix pour une surface de 45 m²
surface = 45
prediction = model.predict([[surface]])

print(f"Surface : {surface} m²")
print(f"Prix estimé : {prediction[0]:,.2f} €")
