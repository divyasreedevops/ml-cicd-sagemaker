import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load data
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df = pd.read_csv(url)
X = df.drop('species', axis=1)
y = df['species']

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, 'model.joblib')

# Package for SageMaker
os.system('tar -czf model.tar.gz model.joblib')
