from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

import pandas as pd
df = pd.read_csv('recommender_data.csv')

beers_list = sorted(df[df['id'] == 'b']['name'].unique().tolist())
whiskey_list = sorted(df[df['id'] == 'w']['name'].unique().tolist())

def recommender(selection):
    x = df.loc[df['name'] == selection, 'id'].iloc[0]
    df_sorted = df.sort_values(selection, ascending=False)
    df_target = df_sorted[df_sorted['id'] != x]
    recommended_list = df_target["name"].unique()[:3]
    return recommended_list

# ------------------------------------------------------------------------------------------------------------------

@app.route('/', methods=['POST', 'GET'])
def home_page():
    return render_template('index.html')

@app.route('/whiskey_rec', methods=['POST', 'GET'])
def dropdown_b():
    selected = request.form.get('beer_selection')
    recommendations = [] if not selected else recommender(selected)

    return render_template(
        'whiskey_rec.html',
        beers=beers_list,
        selected=selected,
        submitted=bool(selected),
        recommendations=recommendations
    )

@app.route('/beer_rec', methods=['POST', 'GET'])
def dropdown_w():
    selected = request.form.get('whiskey_selection')
    recommendations = [] if not selected else recommender(selected)

    return render_template(
        'beer_rec.html',
        whiskeys=whiskey_list,
        selected=selected,
        submitted=bool(selected),
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run()