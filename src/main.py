# main.py
from lexer import Lexer
from parser import Parser

filename = 'main.les'

try:
    with open(filename, 'r') as file:
        source_code = file.read()
except FileNotFoundError:
    print(f"Fehler: Die Datei {filename} wurde nicht gefunden.")
    exit(1)

lexer = Lexer(source_code)
parser = Parser(lexer)
ast = parser.parse()

# Ausgabe des AST
for node in ast:
    print(f'Parsed Return Node with value: {node.value}')
