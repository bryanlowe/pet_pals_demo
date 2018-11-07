function buildPlot() {
    /* data route */
  let url = "/api/pals";
    // @TODO: Build your plot here
  d3.json(url).then(function(response) {
    console.log(response);
    let data = [response];
    let layout = {
      title: "Pet Pals",
      xaxis: {
        title: "Pet Type"
      },
      yaxis: {
        title: "Number of Pets"
      }
    };

    Plotly.plot("plot", data, layout);
  });
}

buildPlot();
