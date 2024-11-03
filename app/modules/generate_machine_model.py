import pandas as pd
from sklearn.linear_model import LinearRegression
from pathlib import Path

def generate_machine_model() -> LinearRegression:
    data_path = Path(__file__).parent.parent.parent / "data" / "pizzas.csv"
    
    data = pd.read_csv(data_path)
    
    x = data[["diametro"]]
    y = data[["preco"]]

    model = LinearRegression()
    model.fit(x, y)

    return model
