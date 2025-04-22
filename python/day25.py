'''
Question:

You are given the Boston housing dataset from sklearn. Write a Python script to:

1. Perform feature selection using recursive feature elimination (RFE) with cross-validation.


2. Use Ridge regression as the estimator for RFE.


3. Identify the top 5 most important features in predicting the target variable.


4. Output the names of these features and their corresponding ranks.


'''


# Answer:

from sklearn.datasets import load_boston
from sklearn.linear_model import Ridge
from sklearn.feature_selection import RFECV
from sklearn.model_selection import KFold
import pandas as pd

# Load the Boston housing dataset
boston = load_boston()
X, y = boston.data, boston.target
feature_names = boston.feature_names

# Initialize the Ridge regression model
ridge = Ridge(alpha=1.0)

# Define cross-validation strategy
cv = KFold(n_splits=5, shuffle=True, random_state=42)

# Perform Recursive Feature Elimination with Cross-Validation (RFECV)
rfe = RFECV(estimator=ridge, step=1, cv=cv, scoring='r2')
rfe.fit(X, y)

# Get feature rankings and selected features
feature_ranking = rfe.ranking_
selected_features = [feature_names[i] for i in range(len(feature_names)) if feature_ranking[i] == 1]

# Top 5 most important features
feature_importance = pd.DataFrame({
    'Feature': feature_names,
    'Rank': feature_ranking
}).sort_values(by='Rank')

print("Top 5 most important features:")
print(feature_importance[feature_importance['Rank'] == 1].head(5))

