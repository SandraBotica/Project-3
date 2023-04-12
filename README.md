## Project Title

# Global Coffee Trade

## Project Description

# A data story about coffee exports, price paid to grower's, imports and retail prices from 1990-2019.

You are very welcome to have a look at our presentation slide deck for deeper insight into our story on Global Coffee Trade.

**Project3SlideDeck_CW_v2.pptx**

## Contributing Members 

Cindy Wong & Sandra Botica

Students @ UWA 6 month Data Analytics Bootcamp November 2022- June 2023

## Acknowledgments

**Data sourced from the International Coffee Organization.**

Historical Data on the Global Coffee Trade.
https://www.ico.org/new_historical.asp

 - Trade Statistics Data - Exports - Calendar Year (excel), Thousand 60kg bags.
 - Trade Statistics Data - Imports - Calendar Year (excel), Thousand 60kg bags.
 - Price Data - Prices to Growers - Annual Averages (excel), US cents/lb.
 - Price Data - Retail Prices - Annual Averages (excel), US dollars/lb.


 - Folder **original_resources** The 4 original excel files 
 - Folder **cleaned_resources** 4 files cleaned for the purpose of this project.

## Technologies used

 - Excel
 - Python notebook
 - Matplotlib
 - QuickDBD
 - PostgreSQL
 - pgAdmin4
 - Python Flask API (HTML/CSS/JavaScript)
 - Plotly


## Getting Started

 1. **<coffee_data.ipynb>** 

    Code that populates the **Resources** folder.

    This folder contains the csv's that feed our API endpoints and visualisations.

    **<coffee_data.ipynb>** has the code for summary statistics and plots.

    This notebook populates the **images** folder used for the slidedeck.

 2. **coffee** folder.

    Open <app.py> and run. 

    Copy the URL from your terminal and paste into browser. 

    Welcome to our **Coffee Data API**

      You will find the list of **Available Data API Endpoints** that populate our visualisations.

      You will find a list of 4 **Data Visualisations**.

      You will also find a list of 3 **Data Comparison** plots. 

 3. In the <coffee> folder you will find:

      An image of our database creation from QuickDBD.
      <ERD_image_coffee_database.png>

      The exported SQL from Quick DBD used in pgAdmin.
      <coffee_dataset.sql>

      **static** folder with JavaScript files.

      Inside **static** another folder called **styles** with the CSS file.

      **templates** folder with HTML files.

 4. The **data_exploration** folder includes files used when planning and exploring this dataset and story. Take for example original app.py and accessing the database using PyMongo.

 5. A report/writeup of this project can be found in the file <writeup.md>


## Contact
 - Feel free to contact Cindy or Sandra with any questions.
 - Cindy Wong cwsynyi88@gmail.com
 - Sandra Botica    smbotica@gmail.com