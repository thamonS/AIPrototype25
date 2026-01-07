import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# 1. Load Data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Train Model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# 3. Save Model
with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)

print("✅ Model trained and saved as 'model.pkl'")