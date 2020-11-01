## Utilizing the scrape_and_render example from class:

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
# exercise had me create this scrape_mars python file
import scrape_mars

# create instance of flask app
app = Flask(__name__)

# Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars"
mongo = PyMongo(app)

# Home Route
@app.route('/')
def index():

    mars_info = mongo.db.mars_info.find()
    return render_template('index.html', mars_info=mars_info)

# Scrape Route
@app.route('/scrape')
def scrape():

    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.scrape()
    print(mars_data)
    mars_info.update({}, mars_data, upsert=True)

     # Redirect once completed.
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)