-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "imports" (
    "Id" INT   NOT NULL,
    "Country" VARCHAR(50)   NOT NULL,
    "Year" INT   NOT NULL,
    "Import_Volume" FLOAT(30)    NULL
);

select * from imports;

CREATE TABLE "exports" (
    "Id" INT   NOT NULL,
    "Country" VARCHAR(50)   NOT NULL,
    "Year" INT   NOT NULL,
    "Export_Volume" FLOAT(30)    NULL
);

select * from exports;

CREATE TABLE "prices_paid_to_growers" (
    "Id" INT   NOT NULL,
    "Country" VARCHAR(50)   NOT NULL,
    "Year" INT   NOT NULL,
    "Growers_Price" FlOAT(20)    NULL
);

select * from prices_paid_to_growers;

CREATE TABLE "retail_prices" (
    "Id" INT   NOT NULL,
    "Country" VARCHAR(50)   NOT NULL,
    "Year" INT   NOT NULL,
    "Retail_Price" FLOAT(20)   NULL
);

select * from retail_prices;