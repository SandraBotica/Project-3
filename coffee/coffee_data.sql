
CREATE TABLE "coffee_data" (
    "Id" INT   NOT NULL,
    "Country" VARCHAR(50)   NOT NULL,
    "Year" INT   NOT NULL,
    "Import_Volume" FLOAT(30)   NULL,
    "Export_Volume" FLOAT(30)   NULL,
    "Growers_Price" FlOAT(20)   NULL,
    "Retail_Price" FLOAT(20)   NULL
);

select * from coffee_data;