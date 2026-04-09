import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
 
df = pd.read_csv("data_set.csv")

inputs = df[["study_hours", "attendance", "previous_marks"]]
outputs = df["final_marks"]

X_train, X_test, y_train, y_test = train_test_split(inputs, outputs, test_size=0.2)

# print("X_train:\n", X_train.head())
# print("X_test:\n", X_test.head())
# print("y_train:\n", y_train.head())
# print("y_test:\n", y_test.head())

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

test_array = pd.DataFrame([[5, 90, 80]], columns=["study_hours", "attendance", "previous_marks"])
# Predict
prediction = model.predict(test_array)

print("Predicted Marks:", prediction[0])