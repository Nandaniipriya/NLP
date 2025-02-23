'''
Question
You are working with the California housing dataset from Scikit-learn. Perform the following tasks:

Load the dataset and create a DataFrame with appropriate column names.
Perform data preprocessing:
Replace missing values with the median of the respective columns.
Scale numerical features using StandardScaler.
Perform feature selection:
Select the top 5 features based on their correlation with the target variable.
Train a RandomForestRegressor model using the top 5 features.
Evaluate the model using R² score and Mean Absolute Error (MAE) on the test set.
'''

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score, mean_absolute_error
import pandas as pd
import numpy as np

# 1. Load the California Housing dataset
data = fetch_california_housing(as_frame=True)
df = data.frame
X = df.drop(columns='MedHouseVal')  # Features
y = df['MedHouseVal']              # Target variable

# 2. Data Preprocessing
# Handle missing values by replacing with median
imputer = SimpleImputer(strategy='median')
X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# Scale numerical features
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_imputed), columns=X.columns)

# 3. Feature Selection
# Calculate correlations with the target
correlations = X_scaled.corrwith(y).abs()
top_features = correlations.sort_values(ascending=False).head(5).index
X_selected = X_scaled[top_features]

# 4. Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# Train the Random Forest Regressor
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# 5. Model Evaluation
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"Top 5 Features: {list(top_features)}")
print(f"R² Score: {r2:.4f}")
print(f"Mean Absolute Error: {mae:.4f}")
