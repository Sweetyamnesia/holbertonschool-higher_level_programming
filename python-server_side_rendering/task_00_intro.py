#!/usr/bin/python3

def generate_invitations(template, attendees):
	if not isinstance(template, str):
		print("Template must be a string")
	if not (isinstance(attendees, list) and all(isinstance(a, dict) for a in attendees)):
		print("Attendees must be a a list of dictionaries")
	if not template:
		print("Template is empty, no output files generated.")
	if not attendees:
		print("No data provided, no output files generated.")
	
