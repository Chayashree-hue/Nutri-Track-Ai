import mysql.connector
from flask import request
from flask import Flask
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="MySQL2505!)",
#   database="nutritrack"
#)

#cursor = db.cursor()
API_KEY = "8cb3003ec59e4f09885e5857a0800c18"

@app.route("/")
def home():
    return {"message": "Backend running!"}

@app.route("/recipes/<query>")
def get_recipes(query):

    url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&addRecipeNutrition=true&apiKey={API_KEY}"
    response = requests.get(url)

    data = response.json()

    return data
  #  @app.route("/saveMeal", methods=["POST"])
#    def save_meal():

    data = request.json

    query = """
    INSERT INTO meals(recipe_name, calories, protein, fat)
    VALUES(%s,%s,%s,%s)
    """

    values = (
        data["recipe_name"],
        data["calories"],
        data["protein"],
        data["fat"]
    )

    cursor.execute(query, values)

    db.commit()

    return {"message":"Meal saved!"}

if __name__ == "__main__":
    app.run(debug=True)