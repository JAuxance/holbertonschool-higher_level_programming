#!/usr/bin/python3
"""Generate invitation files from a text template and attendees data."""


def generate_invitations(template, attendees):
    """Generate one invitation file per attendee from the given template."""
    if not isinstance(template, str):
        print("Template must be a string.")
        return
    if not isinstance(attendees, list):
        print("Attendees must be a list.")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for info in attendees:
        if not isinstance(info, dict):
            print("Attendees must be a list of dictionaries.")
            return

    for i, info in enumerate(attendees, 1):
        if "name" not in info or not info["name"]:
            name = "N/A"
        else:
            name = info["name"]
        if "event_title" not in info or not info["event_title"]:
            event_title = "N/A"
        else:
            event_title = info["event_title"]
        if "event_date" not in info or not info["event_date"]:
            event_date = "N/A"
        else:
            event_date = info["event_date"]
        if "event_location" not in info or not info["event_location"]:
            event_location = "N/A"
        else:
            event_location = info["event_location"]

        personalized = template
        personalized = personalized.replace("{name}", name)
        personalized = personalized.replace("{event_title}", event_title)
        personalized = personalized.replace("{event_date}", event_date)
        personalized = personalized.replace(
            "{event_location}", event_location)
        filename = f"output_{i}.txt"
        with open(filename, "w") as file:
            file.write(personalized)
