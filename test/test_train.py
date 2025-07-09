from train import model
from sklearn.datasets import load_iris

def test_model_prediction():
    iris = load_iris()
    X = iris.data
    y_pred = model.predict(X)
    assert len(y_pred) == len(X)
