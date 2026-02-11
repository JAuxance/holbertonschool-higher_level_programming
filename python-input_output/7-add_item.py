#!/usr/bin/python3
"""
Script that adds all command line arguments to a Python list,
and saves this list to a JSON file ('add_item.json').
Uses the functions save_to_json_file and load_from_json_file.
"""
import json
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json.file


def add_item(args=sys.argv[1:]):
    """
    Ajoute tous les arguments à une liste Python et les sauvegarde dans un fichier JSON.

    Args:
        args (list): Liste des arguments à ajouter (par défaut, ceux de la ligne de commande).

    Le fichier 'add_item.json' est créé s'il n'existe pas, ou mis à jour s'il existe déjà.
    """
    filename = "add_item.json"
    try:
        item = load_from_json_file(filename)
    except Exception:
        item = []

    item.extend(args)
    save_to_json_file(item, filename)
