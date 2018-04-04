from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

import pandas as pd
df = pd.read_csv('../Data/recommender_data.csv')

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


@app.route('/beer', methods=['POST', 'GET'])
def dropdown_b():
    if request.method == 'POST':
        recommendations = recommender(request.form.get('beer_selection'))
        submitted = True
    else:
        recommendations = []
        submitted = False

    return render_template('beer.html', beers=beers_list, selected=request.form.get('beer_selection'), submitted=submitted, recommendations=recommendations)


@app.route('/whiskey', methods=['POST', 'GET'])
def dropdown_w():
    if request.method == 'POST':
        recommendations = recommender(request.form.get('whiskey_selection'))
        submitted = True
    else:
        recommendations = []
        submitted = False

    return render_template('whiskey.html', whiskeys=whiskey_list, selected=request.form.get('whiskey_selection'), submitted=submitted, recommendations=recommendations)



if __name__ == "__main__":
    app.run()

