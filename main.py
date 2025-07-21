from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)  # ← Make sure this line has __name__ exactly

# Load your trained model
model== pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collecting form data from HTML
    age = float(request.form.get('age'))
    anaemia = float(request.form.get('anaemia'))
    creatinine_phosphokinase = float(request.form.get('creatinine_phosphokinase'))
    diabetes = float(request.form.get('diabetes'))
    ejection_fraction = float(request.form.get('ejection_fraction'))
    high_blood_pressure = float(request.form.get('high_blood_pressure'))
    platelets = float(request.form.get('platelets'))
    serum_creatinine = float(request.form.get('serum_creatinine'))
    serum_sodium = float(request.form.get('serum_sodium'))
    sex = float(request.form.get('sex'))
    smoking = float(request.form.get('smoking'))
    time = float(request.form.get('time'))

    # Prepare input for prediction
    features = np.array([[age, anaemia, creatinine_phosphokinase, diabetes,
                          ejection_fraction, high_blood_pressure, platelets,
                          serum_creatinine, serum_sodium, sex, smoking, time]])

    # Make prediction
    result = model.predict(features)

    if result[0] == 1:
        prediction = "High Risk of Death"
    else:
        prediction = "Low Risk of Death"

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
