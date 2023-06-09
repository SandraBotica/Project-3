// Fetch the data from the Flask API
fetch('/api/v1.0/data/exports')
.then(response => response.json())
.then(data => {
    // Get the country names from the 'exports' table
    const countries = data.map(row => row.Country);

    // Populate the dropdown with the country names
    const countrySelect = document.getElementById('countrySelectExports');
    countries.forEach(country => {
        const option = document.createElement('option');
        option.value = country;
        option.text = country;
        countrySelect.add(option);
    });

    // Function to create the line plot for the selected country
    function createLinePlot(country) {
        const exportsData = data.find(row => row.Country === country);

        // Filter out 'Id' and 'Country' keys and convert the remaining keys to numbers
        const years = Object.keys(exportsData).filter(key => key !== 'Id' && key !== 'Country' && !isNaN(Number(key))).map(Number);

        // Extract the data for the selected country
        const exportsValues = years.map(year => exportsData[year]);

        // Create the line plot using Plotly
        const traceExports = { x: years, y: exportsValues, mode: 'lines', name: 'Exports' };
        const plotData = [traceExports];

        const layout = {
            title: `Coffee Exports for ${country}`,
            xaxis: { title: 'Year' },
            yaxis: { title: 'Thousands 60kg bags' }
        };

        Plotly.newPlot('exportsPlot', plotData, layout);
    }

    // Create the initial line plot for the first country in the dropdown
    createLinePlot(countries[0]);

    // Update the line plot when a different country is selected
    countrySelect.addEventListener('change', event => {
        createLinePlot(event.target.value);
    });
});