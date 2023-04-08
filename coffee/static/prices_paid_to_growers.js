// Fetch the data from the Flask API
fetch('/api/v1.0/data/prices_paid_to_growers')
    .then(response => response.json())
    .then(data => {
        // Get the country names from the 'prices_paid_to_growers' table
        const countries = data.map(row => row.Country);

        // Populate the dropdown with the country names
        const countrySelect = document.getElementById('countrySelectGrowers');
        countries.forEach(country => {
            const option = document.createElement('option');
            option.value = country;
            option.text = country;
            countrySelect.add(option);
        });

        // Function to create the line plot for the selected country
        function createLinePlot(country) {
            const growersData = data.find(row => row.Country === country);

            // Filter out 'Id' and 'Country' keys and convert the remaining keys to numbers
            const years = Object.keys(growersData).filter(key => key !== 'Id' && key !== 'Country' && !isNaN(Number(key))).map(Number);

            // Extract the data for the selected country
            const growersValues = years.map(year => growersData[year]);

            // Create the line plot using Plotly
            const traceGrowers = { x: years, y: growersValues, mode: 'lines', name: 'Prices Paid to Growers' };
            const plotData = [traceGrowers];

            const layout = {
                title: `Prices Paid to Growers for ${country}`,
                xaxis: { title: 'Year' },
                yaxis: { title: 'US cents/lb' }
            };

            Plotly.newPlot('growersPlot', plotData, layout);
        }

        // Create the initial line plot for the first country in the dropdown
        createLinePlot(countries[0]);

        // Update the line plot when a different country is selected
        countrySelect.addEventListener('change', event => {
            createLinePlot(event.target.value);
        });
    });