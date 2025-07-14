#!/usr/bin/node
const header = document.getElementById("toggle_header");
header.addEventListener("click", function() {
	const red = document.getElementById("red")
	if (header.classList.contains("red")) {
		header.classList.remove("red");
		header.classList.add("green");
	} else {
		header.classList.remove("green");
		header.classList.add("red");
	}
});