__author__ = "Armin"
__version__ = "1.4.13"
__doc__ = """
Dieses Programm bereinigt eine bereitgestellte CSV-Datei. Die bereinigte Version liegt in data/output.

Sie können Informationen darüber, wie die Bereinigung erfolgen soll, über eine JSON-Datei einstellen.
"""
import logging
from datacleaner import DataCleaner
import config as cfg
from report import Report


logger = logging.getLogger(__name__)


def main():
    """
    Hauptfunktion zur Ausführung der Datenbereinigung.

    Parameters:
        None

    Returns:
        None
    """    
    cleaner = DataCleaner(cfg.input_path)
    cleaner.clean_process(cfg.values)
    cleaner.save_data(cfg.output_path)
    
    report = Report(cfg.input_path, cleaner)
    report.create_data_profile(True, True)
    report.create_data_report(True, True)
  


if __name__ == "__main__":
    logger.info(f"Anwendung {cfg.APP_TITLE} gestartet: {cfg.APP_VERSION}")
    main()
    logger.info(f"Anwendung {cfg.APP_TITLE} beendet: {cfg.APP_VERSION}")
