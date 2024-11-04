from flask import Flask, render_template, request
import joblib

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/predict_crop', methods=['POST'])
def predict_crop():
    if request.method == 'POST':
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        values = [[N, P, K, temperature, humidity, ph, rainfall]]

        model = joblib.load(open('crop_app','rb'))
        prediction = model.predict(values)
        crop = prediction[0]

        return render_template('predict.html', crop=crop)

if __name__ == '__main__':
    app.run(debug=True)
