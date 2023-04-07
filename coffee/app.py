from flask import Flask, render_template, jsonify

import pandas as pd

# import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask
from flask import Flask, jsonify

app = Flask(__name__)

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/coffee')
conn = engine.connect()

imports_data = pd.read_sql("SELECT * FROM imports", conn)
exports_data = pd.read_sql("SELECT * FROM exports", conn)
prices_paid_to_growers_data = pd.read_sql("SELECT * FROM prices_paid_to_growers", conn)
retail_prices_data = pd.read_sql("SELECT * FROM retail_prices", conn)

# print (imports)


@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    # return (
    #     f"Welcome to the Coffee API!<br/>"
    #     f"Available Routes:<br/>"
    #     f"/api/v1.0/imports<br/>"
    #     f"/api/v1.0/exports<br/>"
    #     f"/api/v1.0/prices_paid_to_growers<br/>"
    #     f"/api/v1.0/retail_prices<br/>"
    #     )
    return render_template("index.html")

@app.route("/api/v1.0/imports")
def imports():
    return render_template("imports.html")

@app.route("/api/v1.0/exports")
def exports():
    return render_template("exports.html")

@app.route("/api/v1.0/prices_paid_to_growers")
def prices_paid_to_growers():
    return render_template("prices_paid_to_growers.html")

@app.route("/api/v1.0/retail_prices")
def retail_prices():
    return render_template("retail_prices.html")


@app.route("/api/v1.0/data/imports")
def data_imports():
    return jsonify(imports_data.to_dict(orient="records"))

@app.route("/api/v1.0/data/exports")
def data_exports():
    return jsonify(exports_data.to_dict(orient="records"))

@app.route("/api/v1.0/data/prices_paid_to_growers")
def data_prices_paid_to_growers():
    return jsonify(prices_paid_to_growers_data.to_dict(orient="records"))

@app.route("/api/v1.0/data/retail_prices")
def data_retail_prices():
    return jsonify(retail_prices_data.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)
