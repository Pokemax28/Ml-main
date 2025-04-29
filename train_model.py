
# train_model.py
import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
import sqlite3

# Données d'exemple : surfaces (en m²) et prix (en €)
# Connexion à la base de données SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Récupération des surfaces depuis la table produits_produits
cursor.execute("SELECT surface FROM produit_produit")
surfaces = cursor.fetchall()
print(surfaces)

# Conversion des données en tableau numpy
X = np.array([s[0] for s in surfaces]).reshape(-1, 1)  # surface

cursor.execute("SELECT prix FROM produit_produit")
prix = cursor.fetchall()

y = np.array([p[0] for p in prix]).reshape(-1, 1)  # prix

print(prix)


conn.close()
# Création du modèle
model = LinearRegression()
model.fit(X, y)

# Sauvegarde du modèle
joblib.dump(model, 'model.pkl')

print("Modèle sauvegardé dans model.pkl")
