#!/usr/bin/node
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then(response => response.json())
  .then(data => {
    const name = data.name;
    document.getElementById("character").textContent = name;
  })
  .catch(error => console.error("Error:", error));
