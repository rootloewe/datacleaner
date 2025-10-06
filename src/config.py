import logging.config
from pathlib import Path
import json
import os


os.chdir(str(Path(__file__).parent.resolve()))

input_path = Path("../data") / "input" / "my_data.csv"
output_path = Path("../data") / "output" / "my_data_cleaned.csv"
config_path = Path("../data") / "config" / "config.json"
logging_pfad = Path("../data") / "config" / "logging.ini"

logging.config.fileConfig(logging_pfad)


file = open(config_path, mode = "r", encoding= "UTF-8")
config = json.load(file)
file.close()

drop_na: bool = config["cleaning"]["drop_na"]
drop_duplicate: bool = config["cleaning"]["drop_duplicate"]
data_type_correlation: bool = config["cleaning"]["data_type_correlation"]

values = dict(drop_na=drop_na, drop_duplicate=drop_duplicate, data_type_correlation=data_type_correlation)

APP_TITLE = config["app"]["app_title"]
APP_VERSION = config["app"]["app_version"]