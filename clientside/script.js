var dataContainer = document.getElementById("data-container");
fetch('http://192.168.88.228/')
  .then(function(response) {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Request failed');
    }
  })
  .then(function(data) {
    // Update the content of the data container
    var data = JSON.stringify(data);
    var data = data.split('"')
    dataContainer.textContent = data
    document.getElementById("cas").innerHTML = data[3];
    document.getElementById("hladina").innerHTML = data[7];
  })
  .catch(function(error) {
    console.log(error);
  });