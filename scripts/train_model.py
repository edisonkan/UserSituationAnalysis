import numpy as np
from models.recommendation_model import RecommendationModel

def main():
    data_path = 'data/processed/dataset.csv'
        print(f"Data file not found at {data_path}")
        return
    
    X, y = preprocess_data(data_path)
    model.train(X, y)
    
    accuracy, recall = model.evaluate(X, y)
    print(f"Model Recall: {recall}")
Telegram:@songchuwen
WeChat:songchuxiaomei


if __name__ == "__main__":
