// Fetch the data from the Flask API
fetch('/api/v1.0/data/retail_prices')
    .then(response => response.json())
    .then(data => {
        // Get the country names from the 'retail_prices' table
        const countries = data.map(row => row.Country);

        // Populate the dropdown with the country names
        const countrySelect = document.getElementById('countrySelectRetail');
        countries.forEach(country => {
            const option = document.createElement('option');
            option.value = country;
            option.text = country;
            countrySelect.add(option);
        });

        // Function to create the line plot for the selected country
        function createLinePlot(country) {
            const retailData = data.find(row => row.Country === country);

            // Filter out 'Id' and 'Country' keys and convert the remaining keys to numbers
            const years = Object.keys(retailData).filter(key => key !== 'Id' && key !== 'Country' && !isNaN(Number(key))).map(Number);

            // Extract the data for the selected country
            const retailValues = years.map(year => retailData[year]);

            // Create the line plot using Plotly
            const traceRetail = { x: years, y: retailValues, mode: 'lines', name: 'Retail Prices' };
            const plotData = [traceRetail];

            const layout = {
                title: `Retail Prices for ${country}`,
                xaxis: { title: 'Year' },
                yaxis: { title: 'US dollars/lb' }
            };

            Plotly.newPlot('retailPlot', plotData, layout);
        }

        // Create the initial line plot for the first country in the dropdown
        createLinePlot(countries[0]);

        // Update the line plot when a different country is selected
        countrySelect.addEventListener('change', event => {
            createLinePlot(event.target.value);
        });
    });