#!/usr/bin/python3
import json
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json.file

def add_item(args=sys.argv[1:]):
    filename = "add_item.json"
    try:
        item = load_from_json_file(filename)
    except Exception:
        item = []
    
    item.extend(args)
    save_to_json_file(item, filename)
    