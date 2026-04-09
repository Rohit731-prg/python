import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

row_data = pd.read_csv("data_set2.csv")
data = pd.DataFrame(row_data)

data = data.drop("employee_name", axis=1)

# encode data into numeric values
data_encode = pd.get_dummies(data)

inputs = data_encode.drop("salary_lpa", axis=1)
outputs = data_encode["salary_lpa"]

X_train, X_test, y_train, y_test = train_test_split(inputs, outputs, test_size=0.2)

# Create model
model = LinearRegression()
model.fit(X_train, y_train)

input_data = pd.DataFrame(columns=inputs.columns)

# Add one row filled with 0
input_data.loc[0] = 0

# Fill required values
input_data = pd.DataFrame([{
    "experience_years": 3,
    "department_Engineering": 1,
    "position_Software Engineer": 1,
    "location_Kolkata": 1
}])

input_data = input_data.reindex(columns=inputs.columns, fill_value=0)

prediction = model.predict(input_data)
print("Predicted Salary (LPA):", prediction[0])