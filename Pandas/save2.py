import pandas as pd
import json

data = {
    "student1": [1, "Rohit", 25, "Delhi"],
    "student2": [2, "Indroit", 25, "Habra"],
    "student3": [3, "Rakesh", 25, "Guma"],
    "student4": [4, "Abinash", 25, "Bira"],
    "student5": [5, "kakhat", 25, "Barasat"],
}

# Define column headers
columns = ["ID", "Name", "Age", "City"]

# Convert to dictionary with field names
formatted_data = {
    key: dict(zip(columns, value))
    for key, value in data.items()
}

# Save to JSON file
with open("data2.json", "w") as f:
    json.dump(formatted_data, f, indent=4)
