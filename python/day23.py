from xgboost import XGBClassifier
from sklearn.model_selection import RandomizedSearchCV

# Define model and parameters
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
param_dist = {
    'n_estimators': [100, 200, 300, 400, 500],
    'max_depth': [3, 5, 7, 9],
    'learning_rate': [0.01, 0.1, 0.2]
}

# Randomized search
random_search = RandomizedSearchCV(model, param_distributions=param_dist, 
                                   scoring='accuracy', n_iter=10, cv=3, random_state=42)

# Sample data
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

random_search.fit(X, y)
print("Best parameters:", random_search.best_params_)
print("Best accuracy:", random_search.best_score_)
