// datahandler.js

// Define the URL to retrieve Luke Skywalker's data
let request = "https://swapi.dev/api/people/1/";

// Fetch the data from the URL
fetch(request)
  .then(response => {
    return response.json();
  })
  .then(data => {
    let p = document.getElementById("text");
    // Display the retrieved data
    p.innerHTML = `Name: ${data.name}<br>Gender: ${data.gender}`;
    // p.innerHTML = JSON.stringify(data.gender);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
