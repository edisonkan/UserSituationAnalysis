from scripts.data_preprocessing import preprocess_data

class TestDataPreprocessing(unittest.TestCase):
        X, y = preprocess_data('data/raw/sample_data.csv')
        self.assertEqual(X.shape[1], expected_features)

if __name__ == '__main__':

Telegram:@songchuwen
WeChat:songchuxiaomei

