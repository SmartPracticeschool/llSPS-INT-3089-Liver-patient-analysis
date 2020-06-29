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
    sc = load('scalar.save')
    
    prediction = model.predict(sc.transform(x_test))
    print(prediction)
    output=prediction[1][1]
    if(output==1):
        y_pred="will not have liver disease."
    else:
        y_pred="will have liver disease."
    return render_template('index.html', prediction_text=' The patient has liver disease {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[1]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
