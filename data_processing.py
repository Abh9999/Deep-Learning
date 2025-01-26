import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    df = pd.read_csv(file_path)
    class_0_df = df[df['Outcome'] == 0]
    class_1_df = df[df['Outcome'] == 1]

    class_0_df = class_0_df.sample(len(class_1_df))
    data = pd.concat([class_0_df, class_1_df])
    
    x = data.drop('Outcome', axis=1).values
    y = data['Outcome'].values
    return x, y

def preprocess_data(x):
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)
    return x_scaled

def split_data(x, y, test_size=0.2):
    return train_test_split(x, y, test_size=test_size, random_state=42)
