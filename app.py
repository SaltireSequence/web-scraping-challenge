# import necessary libraries
from flask import Flask, render_template
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

conn = 'mongodb://localhost:27017/mars_app'
client = pymongo.MongoClient(conn)
db = client.mars_db
collection = db.mars_data_entries

@app.route("/")
def home():
    mars_data = client.db.mars.find_one()
    return  render_template('index.html', mars_data=mars_data)

@app.route("/scrape")
def scrape():
    db.collection.remove({})
    mars_data = scrape.scrape()
    db.collection.insert_one(mars_data)
    return  render_template('scrape.html')

if __name__ == "__main__":
    app.run(debug=True)
