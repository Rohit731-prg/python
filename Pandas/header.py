import pandas as pd
import numpy as np

data = {
    "name": ["Rohit", "Saptorshi", "Souvik", "Rupom", "Choyan"],
    "marks": [56, 76, 78, 45, 86],
    "city": ["Delhi", "Habra", "Guma", "Bira", "Barasat"],
    "country": ["India", "India", "India", "India", "India"]
}

df = pd.DataFrame(data)
header = np.array(df.columns)
print(header)
