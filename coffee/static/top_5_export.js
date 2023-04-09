async function getPlotData() 
{
    let chartdata;

    // make API call to get the top 5 export
    const response = await fetch('/api/v1.0/data/top_5_export');
    chartdata = await response.json();
    
    // set trace1
    var trace1 = 
    {
        x: chartdata.map(d => d.Country),
        y: chartdata.map(d => d.total_exported),
        type: 'bar',
        name: 'Top 5 Export by Country'
    }

    var data = [trace1];

    const layout = {
        title: 'Top 5 Export by Country (1990 - 2019)',
        xaxis: { title: 'Year' },
        yaxis: { title: 'Thousands 60kg bags' }
    };

    Plotly.newPlot('top_5_export', data, layout);
}
getPlotData();