from flask import Flask, render_template, request
from analysis.PollutionAnalytics import GetDailyPollutionGraph, GetDataForTable

app = Flask(__name__)

# Routes
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/Datos", methods=['POST'])
def Datos():
    if request.method == 'POST':
        day = int(request.form['Day'])
        neighborhood = request.form['Neighbourhood']
        GetDailyPollutionGraph(day, neighborhood)
        data = GetDataForTable(day, neighborhood)
        return render_template('Datos.html', day=day, neighborhood=neighborhood, data=data)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)








