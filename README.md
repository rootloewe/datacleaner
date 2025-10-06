# DataCleaner - CSV Data Cleaning Utility
Dieses Python-Projekt stellt eine Klasse `DataCleaner` bereit, die CSV-Daten lädt, bereinigt und speichert. Die Daten werden mit pandas verarbeitet und wichtige Schritte mit Logging protokolliert.

## Funktionen
- CSV-Dateien laden
- Entfernen von Zeilen mit fehlenden Werten (NaN)
- Bereinigte Daten als CSV speichern
- Protokollierung der Schritte über Python Logging

## Installation
Stelle sicher, dass Python 3 und pandas installiert sind:
!pip install pandas


## Methoden
-------
load_data(filepath: str) -> pd.DataFrame
    Lädt CSV-Daten.
drop_empty_rows(df: pd.DataFrame) -> None
    Entfernt Zeilen mit leeren Werten.
drop_duplicates(df: pd.DataFrame) -> None
    Entfernt doppelte vollständige Zeilen aus den Daten.
Data_type_correction(self) -> None
    Wandelt Daten in Zahlen um
save_data(df: pd.DataFrame, filepath: str) -> None
    Speichert Daten in eine CSV-Datei.
"""

## Hinweis
Die Adressen in der my_data.csv wurden mit der Python Bibliothek faker erstellt. Damit sind Rückschlüsse auf Personen unmöglich.

## Lizenz
GNU GENERAL PUBLIC LICENSE