async function getPlotData() 
{
    let data1;
    let data2;
    
    var data1_x_data;
    var data1_y_data;
    var data2_x_data;
    var data2_y_data;

    // make 2 separate API calls to get the total exports and prices paid to growers
    const response1 = await fetch('/api/v1.0/data/total_retail');
    data1 = await response1.json();

    const response2 = await fetch('/api/v1.0/data/total_growers');
    data2 = await response2.json();
    
    // save the data accordingly to the two traces' axes
    data1_x_data = Object.keys(data1[0]);
    data1_y_data = Object.values(data1[0]);
    
    data2_x_data = Object.keys(data2[0]);
    data2_y_data = Object.values(data2[0]);

    // set trace1 and trace2
    var trace1 = 
    {
        x: data1_x_data,
        y: data1_y_data,
        mode: 'lines',
        name: 'Total Retail Prices'
    }

    var trace2 = 
    {
        x: data2_x_data,
        y: data2_y_data,
        mode: 'lines',
        name: 'Total Prices Paid to Growers'
    }

    var data = [trace1, trace2];

    const layout = {
        title: 'Total Retail Prices vs Prices Paid to Growers',
        xaxis: { title: 'Year' },
        yaxis: { title: 'US dollars/lb' }
    };

    Plotly.newPlot('export_growers', data, layout);
}
getPlotData();