from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score

class RecommendationModel:
    def __init__(self, input_dim):
        self.model.add(Dense(64, input_dim=input_dim, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    def train(self, X, y, epochs=10, batch_size=32):
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    def predict(self, X):
        return (self.model.predict(X) > 0.5).astype("int32")
    
    def evaluate(self, X, y):
        accuracy = accuracy_score(y, y_pred)
        return accuracy, recall

Telegram:@songchuwen
WeChat:songchuxiaomei

