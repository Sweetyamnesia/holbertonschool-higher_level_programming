#!/usr/bin/node
const header = document.getElementById("toggle_header");
header.addEventListener("click", function() {
	const red = document.getElementById("red")
	if (document.getElementById("red")) {
		document.getElementById("red") = "green"
	} else {
		document.getElementById("red") = "red"
	}
});