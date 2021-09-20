import sys 
sys.path.append(".")
from app import app
from app.evaluation.tasks import load_data

@app.route("/evaluation/{user_id}")
def evaluation(user_id: int):
    df = load_data(user_id)


