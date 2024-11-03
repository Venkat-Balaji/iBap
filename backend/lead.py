# backend/models/lead_qualification.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load sample data
leads_data = pd.read_csv('leads.csv')

# Define your ML model
def train_lead_qualification_model():
    model = RandomForestClassifier(n_estimators=100)
    X = leads_data.drop('qualified', axis=1)
    y = leads_data['qualified']
    model.fit(X, y)
    return model

# Function to qualify leads dynamically
def qualify_lead(new_lead_data):
    model = train_lead_qualification_model()
    return model.predict([new_lead_data])[0]
