from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('iris_model.pkl',"rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)

    output = round(prediction[0],2)
    return render_template('index.html',prediction_text="iris: ".format(output))

if __name__ == '__main__':
    app.run(PORT=5000,debug=True)

