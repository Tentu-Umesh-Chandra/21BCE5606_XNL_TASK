import pandas as pd
from sklearn.ensemble import IsolationForest

class FraudDetection:
    def __init__(self):
        self.model = IsolationForest(contamination=0.01)

    def train_model(self, data):
        features = data[['amount', 'transaction_type', 'account_age']]
        self.model.fit(features)

    def detect_fraud(self, transactions):
        features = transactions[['amount', 'transaction_type', 'account_age']]
        predictions = self.model.predict(features)
        transactions['is_fraud'] = predictions == -1
        return transactions
