# Datei festlegen
filename = 'main.les'

# Schritt 1: Datei öffnen und einlesen
try:
    with open(filename, 'r') as file:
        source_code = file.read()  # Gesamten Inhalt einlesen
except FileNotFoundError:
    print(f"Fehler: Die Datei {filename} wurde nicht gefunden.")
    exit(1)  # Beende das Programm mit einem Fehlerstatus

# Schritt 2: Ausgabe des gelesenen Codes
print("Eingelesener Code:")
print(source_code)
