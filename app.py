from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('knn.pkl', 'rb'))

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def Home():
    return render_template('audit.html')
@app.route('/predict', methods=['GET', 'POST'])
def Audit():
    return render_template('main.html')
@app.route('/riskpred', methods=['GET', 'POST'])
def About():
    if request.method == "POST":
        Sector_score = request.form['Sector_score']
        PARA_A = request.form['PARA_A']
        Risk_A = request.form['Risk_A']
        PARA_B = request.form['PARA_B']
        Risk_B = request.form['Risk_B']
        TOTAL = request.form['TOTAL']
        numbers = request.form['numbers']
        Money_Value = request.form['Money_Value']
        Score_MV = request.form['Score_MV']
        District_Loss = request.form['District_Loss']
        History = request.form['History']
        Score = request.form['Score']
        Inherent_Risk = request.form['Inherent_Risk']
        Audit_Risk = request.form['Audit_Risk']

        pred = [[float(Sector_score),float(0), float(PARA_A),float(0), float(Risk_A), float(PARA_B),float(0), float(Risk_B), float(TOTAL),
                 float(numbers),float(0),float(0), float(Money_Value), float(Score_MV),float(0), float(District_Loss),float(0),float(0),float(History),float(0),float(0), float(Score),
                 float(Inherent_Risk),float(0),float(0), float(Audit_Risk)]]

        output = model.predict(pred)
        return render_template('result.html', predict="The Predicted Risk value is: " + str(output[0]))

if __name__ == '__main__':
    app.run(debug=True)