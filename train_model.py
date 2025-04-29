import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Récupération des surfaces et des prix depuis la table produit_produit
cursor.execute("SELECT surface, prix FROM produit_produit WHERE surface IS NOT NULL AND prix IS NOT NULL")
data = cursor.fetchall()
conn.close()

# Vérification qu'on a bien des données
if len(data) < 2:
    raise ValueError("Pas assez de données pour entraîner un modèle.")

# Séparation des colonnes en X et y
X = np.array([row[0] for row in data]).reshape(-1, 1)
y = np.array([row[1] for row in data])

# Normalisation des données
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Création du modèle
model = LinearRegression()

# Validation croisée uniquement si assez d'échantillons
n_samples = len(X_train)
n_splits = min(5, n_samples)

if n_splits >= 2:
    scores = cross_val_score(model, X_train, y_train, cv=n_splits, scoring='r2')
    print(f"Scores de validation croisée (cv={n_splits}) : {scores}")
    print(f"Score moyen de validation croisée : {np.mean(scores):.4f}")
else:
    print("Pas assez d'échantillons pour faire une validation croisée.")

# Entraînement du modèle
model.fit(X_train, y_train)

# Évaluation sur l'ensemble de test
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


# Sauvegarde du modèle et du scaler
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("Modèle sauvegardé dans model.pkl")
print("Scaler sauvegardé dans scaler.pkl")
