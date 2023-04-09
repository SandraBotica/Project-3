async function getPlotData() 
{
    let chartdata;
    let chartdata2;

    // make API call to get the top 5 import
    const response = await fetch('/api/v1.0/data/top_5_import');
    chartdata = await response.json();

    const response2 = await fetch('/api/v1.0/data/top_5_export');
    chartdata2 = await response2.json();
    
    // set trace1
    var trace1 = 
    {
        x: chartdata.map(d => d.Country),
        y: chartdata.map(d => d.total_imported),
        type: 'bar',
        name: 'Top 5 Import by Country'
    }

    var trace2 = 
    {
        x: chartdata2.map(d => d.Country),
        y: chartdata2.map(d => d.total_exported),
        type: 'bar',
        name: 'Top 5 Export by Country'
    }

    var data = [trace1, trace2];

    const layout = {
        title: 'Top 5 Import & Export by Country (1990 - 2019)',
        xaxis: { title: 'Year' },
        yaxis: { title: 'Thousands 60kg bags' }
    };

    Plotly.newPlot('top_5_import_export', data, layout);
}
getPlotData();