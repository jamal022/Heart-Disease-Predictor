#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#Initialize the flask App
app = Flask(__name__,template_folder='template')
model = pickle.load(open('heart_disease.pickle', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if output ==1:
        return render_template('index.html', prediction_text=' High Risk of Heart Disease!')
    else:
        return render_template('index.html', prediction_text='Low Risk of Heart Disease!')

    

if __name__ == "__main__":
    app.run(debug=True)
