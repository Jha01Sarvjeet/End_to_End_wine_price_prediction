# from flask import Flask,render_template,request
# import numpy as np
# import pandas as pd
# import os
# from src.wine_qulity_predction.pipeline.prediction_pipeline import PredictionPipeline

# app = Flask(__name__)
# @app.route('/',methods=['GET']) ## route to     display the home page
# def homepage():
#     return render_template('index.html')

# @app.route('/train',methods=['GET'])  # route to train the pipeline
# def training():
#     os.system("python main.py")
#     return "Training Successful!"


# @app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
# def index():
#     if request.method == 'POST':
#         try:
#             #  reading the inputs given by the user
#             fixed_acidity = float(request.form['fixed_acidity'])
#             volatile_acidity = float(request.form['volatile_acidity'])
#             citric_acid = float(request.form['citric_acid'])
#             residual_sugar = float(request.form['residual_sugar'])
#             chlorides = float(request.form['chlorides'])
#             free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
#             total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
#             density = float(request.form['density'])
#             pH = float(request.form['pH'])
#             sulphates = float(request.form['sulphates'])
#             alcohol = float(request.form['alcohol'])

#             data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide,
#                     total_sulfur_dioxide, density, pH, sulphates, alcohol]
#             data = np.array(data).reshape(1, 11)

#             obj = PredictionPipeline()
#             predict = obj.predict(data)

#             return render_template('result.html', predict=str(predict))

#         except Exception as e:
#             print('The Exception message is: ', e)
#             return 'something is wrong'

#     else:
#         return render_template('index.html')


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)


from flask import Flask, render_template, request
import numpy as np
import os
from src.wine_qulity_predction.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "<h1>✅ Model training completed. <a href='/'>Go back</a></h1>"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            input_values = [float(request.form[field]) for field in [
                'fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides',
                'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol'
            ]]
            data = np.array(input_values).reshape(1, -1)
            obj = PredictionPipeline()
            prediction = obj.predict(data)
            return render_template('result.html', predict=str(prediction))
        except Exception as e:
            return f"<h2>⚠️ Error occurred: {str(e)}</h2><a href='/'>Back to home</a>"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080)
