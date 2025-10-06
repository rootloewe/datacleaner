import logging
import numpy as np
import sweetviz as sv
from ydata_profiling import ProfileReport 
from pathlib import Path

np.VisibleDeprecationWarning = np.exceptions.VisibleDeprecationWarning

class Report:
    """
    Diese Klasse erstellt html Profile der Daten.

    Methoden
    -------
    create_data_profile(self, original=False, cleaned=False) -> None
    create_data_report(self, original=False, cleaned=False) -> None
    """
    logger = logging.getLogger()


    def __init__(self, input_path, cleaner):
        self.df_original = cleaner.df_original 
        self.df = cleaner.get_df_cleanded()
        

    def create_data_profile(self, original=False, cleaned=False) -> None:
        """
        Erstellt Datenprofil-Reports für originale und bereinigte DataFrames.

        Für jedes gegebene DataFrame (original und/oder bereinigt) wird ein Profilreport mit Metainformationen wie Titel, Beschreibung, Autor
        und Copyright-Daten erzeugt und als HTML-Datei gespeichert. Die Pfade und Reporttitel unterscheiden sich entsprechend dem Datenzustand.

        Parameter:
        -----------
        original : bool
            Wenn True, wird ein Profilreport des originalen (ungefilterten) DataFrames erstellt und gespeichert.

        cleaned : bool
            Wenn True, wird ein Profilreport des bereinigten (gefilterten) DataFrames erstellt und gespeichert.

        Log:
        -----
        Beim erfolgreichen Erstellen der Reports werden Info-Nachrichten im Logger abgelegt.
        """
        report_path = Path("../report/report_profile_original.html")
        if original and not report_path.is_file():
            profile = ProfileReport(self.df_original, title = "My Data Profile of original File",
                                    dataset= {
                                        "description": "This is a data profile of the eCommerce Fake WebShop - Original Uncleaned",
                                        "author": "Armin",
                                        "copyright_holder": "Me",
                                        "copyright_year": 2025,
                                        "url": ""
                                    })
            profile.to_file(str(report_path))
            self.logger.info("Daten Profil der original Daten erstellt.")


        if cleaned:
            profile = ProfileReport(self.df, title = "My Data Profile of cleaned DataFrame",
                                    dataset= {
                                        "description": "This is a data profile of the eCommerce Fake WebShop - Cleaned Data",
                                        "author": "Armin",
                                        "copyright_holder": "Me",
                                        "copyright_year": 2025,
                                        "url": ""
                                    })
            profile.to_file("../report/report_profile_cleaned.html")
            self.logger.info("Daten Profil der bereinigten Daten erstellt.")


    def create_data_report(self, original=False, cleaned=False) -> None:
        """
        Erstellt Datenberichte mit Sweetviz für originale und bereinigte DataFrames.

        Parameter:
        ----------
        original : bool, optional
            Falls True, wird ein Bericht für das originale DataFrame (self.df_original) erstellt und als HTML gespeichert.
            Standardwert ist False.

        cleaned : bool, optional
            Falls True, wird ein Bericht für das bereinigte DataFrame (self.df) erstellt und als HTML gespeichert.
            Standardwert ist False.

        Funktion:
        ---------
        Je nachdem, welcher Parameter True ist, wird der jeweilige Bericht mit sv.analyze erzeugt, als HTML-Datei gespeichert
        und eine Log-Info mit dem Ergebnis ausgegeben.

        Beispiel:
        ---------
        create_data_report(original=True, cleaned=False)

        Log:
        -----
        Beim erfolgreichen Erstellen der Reports werden Info-Nachrichten im Logger abgelegt.
        """
        report_path = Path("../report/report_original_sv.html")
        if original and not report_path.is_file():
            report = sv.analyze([self.df_original, "My Data Profile of original DataFrame"])
            report.show_html(str(report_path), open_browser=False)
            self.logger.info("Daten Report SV der original Daten erstellt.")


        if cleaned:
            report = sv.analyze([self.df, "My Data Profile of cleanded DataFrame"])
            report.show_html("../report/report_cleaned_sv.html", open_browser=False)
            self.logger.info("Daten Report SV der bereinigten Daten erstellt.")

        