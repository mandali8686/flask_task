from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

joblib.dump(model, 'iris_model.pkl')


