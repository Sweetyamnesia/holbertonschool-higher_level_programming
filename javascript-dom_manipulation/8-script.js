#!/usr/bin/node
fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
  .then(response => response.json())
  .then(data => {
    const value = document.getElementById("hello");
	value.textContent = data.hello
  })
  .catch(error => console.error("Error:", error));
