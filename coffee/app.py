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

total_import_query = "select sum(\"1990\") as \"1990\",sum(\"1991\") as \"1991\",sum(\"1992\") as \"1992\",sum(\"1993\") as \"1993\",sum(\"1994\") as \"1994\",sum(\"1995\") as \"1995\" ,sum(\"1996\") as \"1996\" ,sum(\"1997\") as \"1997\" ,sum(\"1998\") as \"1998\" ,sum(\"1999\") as \"1999\",sum(\"2000\") as \"2000\",sum(\"2001\") as \"2001\",sum(\"2002\") as \"2002\",sum(\"2003\") as \"2003\",sum(\"2004\") as \"2004\",sum(\"2005\") as \"2005\",sum(\"2006\") as \"2006\",sum(\"2007\") as \"2007\",sum(\"2008\") as \"2008\",sum(\"2009\") as \"2009\",sum(\"2010\") as \"2010\",sum(\"2011\") as \"2011\",sum(\"2012\") as \"2012\",sum(\"2013\") as \"2013\",sum(\"2014\") as \"2014\",sum(\"2015\") as \"2015\",sum(\"2016\") as \"2016\",sum(\"2017\") as \"2017\",sum(\"2018\") as \"2018\",sum(\"2019\") as \"2019\" from imports"

total_export_query = "select sum(\"1990\") as \"1990\",sum(\"1991\") as \"1991\",sum(\"1992\") as \"1992\",sum(\"1993\") as \"1993\",sum(\"1994\") as \"1994\",sum(\"1995\") as \"1995\" ,sum(\"1996\") as \"1996\" ,sum(\"1997\") as \"1997\" ,sum(\"1998\") as \"1998\" ,sum(\"1999\") as \"1999\",sum(\"2000\") as \"2000\",sum(\"2001\") as \"2001\",sum(\"2002\") as \"2002\",sum(\"2003\") as \"2003\",sum(\"2004\") as \"2004\",sum(\"2005\") as \"2005\",sum(\"2006\") as \"2006\",sum(\"2007\") as \"2007\",sum(\"2008\") as \"2008\",sum(\"2009\") as \"2009\",sum(\"2010\") as \"2010\",sum(\"2011\") as \"2011\",sum(\"2012\") as \"2012\",sum(\"2013\") as \"2013\",sum(\"2014\") as \"2014\",sum(\"2015\") as \"2015\",sum(\"2016\") as \"2016\",sum(\"2017\") as \"2017\",sum(\"2018\") as \"2018\",sum(\"2019\") as \"2019\" from exports"

total_retail_query = "select sum(\"1990\") * 100 as \"1990\",sum(\"1991\") * 100 as \"1991\",sum(\"1992\") * 100 as \"1992\",sum(\"1993\") * 100 as \"1993\",sum(\"1994\") * 100 as \"1994\",sum(\"1995\") * 100 as \"1995\" ,sum(\"1996\") * 100 as \"1996\" ,sum(\"1997\") * 100 as \"1997\" ,sum(\"1998\") * 100 as \"1998\" ,sum(\"1999\") * 100 as \"1999\",sum(\"2000\") * 100 as \"2000\",sum(\"2001\") * 100 as \"2001\",sum(\"2002\") * 100 as \"2002\",sum(\"2003\") * 100 as \"2003\",sum(\"2004\") * 100 as \"2004\",sum(\"2005\") * 100 as \"2005\",sum(\"2006\") * 100 as \"2006\",sum(\"2007\") * 100 as \"2007\",sum(\"2008\") * 100 as \"2008\",sum(\"2009\") * 100 as \"2009\",sum(\"2010\") * 100 as \"2010\",sum(\"2011\") * 100 as \"2011\",sum(\"2012\") * 100 as \"2012\",sum(\"2013\") * 100 as \"2013\",sum(\"2014\") * 100 as \"2014\",sum(\"2015\") * 100 as \"2015\",sum(\"2016\") * 100 as \"2016\",sum(\"2017\") * 100 as \"2017\",sum(\"2018\") * 100 as \"2018\",sum(\"2019\") * 100 as \"2019\" from retail_prices"

total_growers_query = "select sum(\"1990\") as \"1990\",sum(\"1991\") as \"1991\",sum(\"1992\") as \"1992\",sum(\"1993\") as \"1993\",sum(\"1994\") as \"1994\",sum(\"1995\") as \"1995\" ,sum(\"1996\") as \"1996\" ,sum(\"1997\") as \"1997\" ,sum(\"1998\") as \"1998\" ,sum(\"1999\") as \"1999\",sum(\"2000\") as \"2000\",sum(\"2001\") as \"2001\",sum(\"2002\") as \"2002\",sum(\"2003\") as \"2003\",sum(\"2004\") as \"2004\",sum(\"2005\") as \"2005\",sum(\"2006\") as \"2006\",sum(\"2007\") as \"2007\",sum(\"2008\") as \"2008\",sum(\"2009\") as \"2009\",sum(\"2010\") as \"2010\",sum(\"2011\") as \"2011\",sum(\"2012\") as \"2012\",sum(\"2013\") as \"2013\",sum(\"2014\") as \"2014\",sum(\"2015\") as \"2015\",sum(\"2016\") as \"2016\",sum(\"2017\") as \"2017\",sum(\"2018\") as \"2018\",sum(\"2019\") as \"2019\" from prices_paid_to_growers"

imports_data = pd.read_sql("SELECT * FROM imports", conn)
exports_data = pd.read_sql("SELECT * FROM exports", conn)
prices_paid_to_growers_data = pd.read_sql("SELECT * FROM prices_paid_to_growers", conn)
retail_prices_data = pd.read_sql("SELECT * FROM retail_prices", conn)
total_imports_data = pd.read_sql(total_import_query, conn)
total_exports_data = pd.read_sql(total_export_query, conn)
total_retail_data = pd.read_sql(total_retail_query, conn)
total_growers_data = pd.read_sql(total_growers_query, conn)

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

@app.route("/api/v1.0/all_in_one")
def all_in_one():
    return render_template("all_in_one.html")

@app.route("/api/v1.0/total_imports_exports")
def total_imports_exports():
    return render_template("total_imports_exports.html")

@app.route("/api/v1.0/total_exports_growers")
def total_exports_growers():
    return render_template("total_exports_growers.html")

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

@app.route("/api/v1.0/data/total_imports")
def total_imports():
    return jsonify(total_imports_data.to_dict(orient="records"))

@app.route("/api/v1.0/data/total_exports")
def total_exports():
    return jsonify(total_exports_data.to_dict(orient="records"))

@app.route("/api/v1.0/data/total_retail")
def total_retail():
    return jsonify(total_retail_data.to_dict(orient="records"))

@app.route("/api/v1.0/data/total_growers")
def total_growers():
    return jsonify(total_growers_data.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
