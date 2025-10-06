import pandas as pd
import logging
from decimal import Decimal


class DataCleaner:
    """
    Klasse zur Bereinigung von CSV-Daten.

    Methoden
    -------
    load_data(filepath: str) -> pd.DataFrame
        Lädt CSV-Daten.
    drop_empty_rows(df: pd.DataFrame) -> None
        Entfernt Zeilen mit leeren Werten.
    save_data(df: pd.DataFrame, filepath: str) -> None
        Speichert Daten in eine CSV-Datei.
    """
    logger = logging.getLogger()

    def __init__(self, input_file_path: str):
        self.df_original = self.load_data(input_file_path)      # original file
        self.df = self.load_data(input_file_path)               # Process file

        self.logger.info(f"Daten wurden aus {input_file_path} geladen")


    def load_data(self, input_filepath: str) -> pd.DataFrame:
        """
        Lädt eine CSV-Datei als DataFrame.

        Parameters:
            input_filepath (str): Pfad zur CSV-Datei.

        Returns:
            pd.DataFrame: Geladene Daten.
        """
        self.df = pd.read_csv(input_filepath)
        df = pd.read_csv(input_filepath)

        return df


    def clean_process(self, config: dict) -> None:
        """
        ruft die drop methoden auf

        Parameters:
            config dictionary

        Returns:
            None
        """
        if config['drop_na']:
            self.drop_empty_rows()
        
        if config['drop_duplicate']:
            self.drop_duplicates()

        if config['data_type_correlation']:
            self.Data_type_correction()


    def drop_empty_rows(self):
        """
        Entfernt alle Zeilen mit mindestens einem leeren Wert.

        Parameters:
            df (pd.DataFrame): Eingabedaten.

        Returns:
            None
        """
        before = self.df_original.shape[0]
        self.df = self.df.dropna(axis=0, how="all")  
        after = self.df.shape[0]
        self.logger.info(f"Entfernte leere Zeilen: {before - after}")
    

    def drop_duplicates(self):
        """
        Entfernt doppelte vollständige Zeilen aus den Daten und behällt die erste

        Parameters:
            df (pd.DataFrame): Eingabedaten.

        Returns:
            None
        """
        before = self.df_original.shape[0]
        self.df = self.df.drop_duplicates(keep="first")
        # enfernt Zeilen, die wie Header sind  
        # bereinigter df  =  df zeilenweise String liste nur wo         != [Order ID, Product Quality Ordered, Price Each, Order Date, Purchase Adress]
        self.df = self.df[~(self.df.astype(str).apply(lambda x: list(x) == [str(col) for col in self.df.columns], axis=1))]
        after = self.df.shape[0]
        self.logger.info(f"Entfernte doppelte vollständige Zeilen: {before - after}, Anzahl Duplikate: {self.df.duplicated().sum()}") 


    def Data_type_correction(self) -> None:
        """
        Wandelt alle Preise in Decimal um, vorher in Strings, um Rundungsfehler zu vermeiden

        Returns:
            None
        """
        self.convert_OrderID()
        self.convert_prices_to_decimal()


    def convert_OrderID(self) -> None:
        """
        Konvertiert die Spalte 'Order ID' im DataFrame in den Integer-Datentyp.

        Versucht, die Werte in der Spalte 'Order ID' mittels pd.to_numeric in numerische Werte umzuwandeln.
        Nicht-konvertierbare Werte werden zu NaN. Anschließend wird die Spalte in den Nullable Integer Typ 'Int64' 
        umgewandelt, der fehlende Werte unterstützt. 

        Falls eine Umwandlung nicht möglich ist, wird die Exception geloggt.

        Returns:
            None

        Raises:
            ValueError: Falls bei der Umwandlung ein Wertfehler auftritt.
            TypeError: Falls die Umwandlung nicht kompatibel mit dem Datentyp ist.
        """     
        try:
            self.df['Order ID'] = self.df['Order ID'].astype(str).str.strip()
            self.df['Order ID'] = self.df['Order ID'].astype(int)
        except (ValueError, TypeError) as e:
            self.logger.exception(f"Fehler beim Umwandeln der 'Order ID'-Spalte in Integer: {e}")
        else:
            self.logger.info(f"Orderd ID erfolgreich umgewandelt in: {self.df['Order ID'].dtype}")

 
    def convert_prices_to_decimal(self) -> None:
        """
        Wandelt alle Preise in Decimal um, vorher in Strings, um Rundungsfehler zu vermeiden

        Returns:
            None
        """
        try:
            self.df['Price Each'] = self.df['Price Each'].apply(lambda x: Decimal(str(x)))
            #self.df['Price Each'] = self.df['Price Each'].apply(lambda x: float(str(x)))
        except Exception:
            self.logger.exception("Die Preise konnten NICHT in Decimal umgewanldet werden.")
        else:
            self.logger.info(f"Alle Preise erfolgreich umgewandelt in: {type(self.df['Price Each'].iloc[0])}.") 


    def save_data(self, filepath: str) -> None:
        """
        Speichert DataFrame als CSV-Datei.

        Parameters:
            df (pd.DataFrame): Daten.
            filepath (str): Speicherpfad.

        Returns:
            None
        """
        self.df.to_csv(filepath, index=False)
        self.logger.info(f"Daten gespeichert unter {filepath}")

    
    def get_df_cleanded(self) -> pd.DataFrame:
        """
        Gibt das bereinigte DataFrame zurück.

        Returns:
            pandas.DataFrame: Das DataFrame mit bereinigten Daten.
        """
        return self.df

