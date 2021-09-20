import sys
sys.path.append(".")
import pandas as pd
import requests
import json
import plotly
import plotly.express as px

def load_data(user_id, exercise=None):

    url = f"https://training.daily-code.de/evaluation/get_exercise_history/1"
    if exercise != None:
        url = f"https://training.daily-code.de/evaluation/get_exercise_history/{user_id}?exercise_name={exercise}"

    print(url)
    # print(f"https://training.daily-code.de/evaluation/get_exercise_history/{user_id}?exercise_name={exercise}")
    res = requests.get(url)
    # print(res.text)


    if res.status_code != 200:
        return f"error status_code = {res.status_code}"

    data = format_data(res.text)

    print(res.text)

    df = pd.json_normalize(data['exercises'])

    return df


def format_data(data_in):
    data_out = {"exercises":[]}
    data_in = json.loads(data_in)
    for entry in data_in:
        for exercise in data_in[entry]:
            data_out["exercises"].append(exercise)
    
    return data_out


def plot(df):
    # px.
    plot_data = px.scatter(data_frame=df, x="date", y="weight", hover_name="name", hover_data=['sets', 'reps', 'weight'], color="reps")
    return plot_data
    # return json.dumps(plot_data, cls=plotly.utils.PlotlyJSONEncoder)

if __name__ == '__main__':
    df = load_data(1, "kreuzheben")

    print(df)

    data = plot(df)
    data.show()

