"""Test script for the invitation generator."""

import os

# Main file content
from task_00_intro import generate_invitations

# Read the template from a file, relative to this script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(current_dir, 'template.txt')
with open(template_path, 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference",
        "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop",
        "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit",
        "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)
