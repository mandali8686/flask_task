from flask import Flask, jsonify, request
import pickle
import pandas as pd


app=Flask(__name__)

model = pickle.load(open('iris_model.pkl','rb'))


@app.route("/", methods =['GET','POST']) #http://www.google.com/

def home():
    if (request.method=='GET'):
        data="hello, world!"
        return jsonify({'data':data})


@app.route('/predict/')
def price_predict():
    
    sepal_length=request.args.get('Sepal length')
    sepal_width=request.args.get('Sepal width')
    petal_length=request.args.get('Petal length')
    petal_width=request.args.get('Petal width')
    #print('unplckle completed')
    #print(model)
    test_df=pd.DataFrame({'Sepal length':[sepal_length], 'Sepal width':[sepal_width], "Petal length":[petal_length],"Petal width": [petal_width]})
    pred=model.predict(test_df)
    return jsonify({"Iris":pred.tolist() })
    
if __name__ == '__main__':
    app.run(port=4000,debug=True)