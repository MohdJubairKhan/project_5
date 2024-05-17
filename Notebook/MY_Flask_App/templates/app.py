from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load(r'C:\Users\Hp\Desktop\Data_Science_Jupyter\Project_1_digi_crome_capstone\Notebook\MY_Flask_App\templates\Linear_Regression.pkl')


# Home route to serve the input form
@app.route('/')
def home():
    return render_template('Index.html')

# Prediction route to handle input data and return predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)