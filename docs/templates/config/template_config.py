# config/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ==== PATHS ====
DATA_DIR = "data/"
LOGS_DIR = "logs/"
OUTPUT_DIR = "outputs/"

# ==== PARAMETERS ====
DEFAULT_INPUT_FILE = os.getenv("DEFAULT_INPUT_FILE", "input.csv")
USE_CACHE = os.getenv("USE_CACHE", "True") == "True"
VERBOSE_MODE = os.getenv("VERBOSE_MODE", "False") == "True"

# ==== SECRETS ====
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DROPBOX_TOKEN = os.getenv("DROPBOX_TOKEN")