import altair as alt
import pandas as pd
from flask import Flask, render_template, request
mission_data = pd.read_excel('data.xlsx', sheet_name="Mission Costs")

app = Flask(__name__)
alt.renderers.enable('html')


@app.route('/')
def index():
    return render_template('template.html')


@app.route('/', methods=["POST"])
def my_link():
    destination = request.form['destination']
    print(mission_data[[destination, 'Fiscal Year']])
    chart = alt.Chart(mission_data[[destination, 'Fiscal Year']]).mark_point().encode(x='Fiscal Year')

    chart.save('templates/chart.html')
    return render_template('chart.html')


if __name__ == '__main__':
    app.run(debug=True)

