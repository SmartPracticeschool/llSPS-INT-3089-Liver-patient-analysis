import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from joblib import load

app = Flask(__name__)
model = pickle.load(open('decision.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[int(x) for x in request.form.values()]]
    print(x_test)
    #print(x_test.shape)
    sc = load('scalar.save')
    b=sc.transform(x_test)
    print(b)
    prediction = model.predict(b)
    print(x_test)
    print(prediction)
    output=prediction[0]
    if(output==0):
        y_pred="will not have liver disease."
    else:
        y_pred="will have liver disease."
    prediction_text=' The patient '+y_pred
    return render_template('index.html', y_pred1=prediction_text)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.y_pred([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
