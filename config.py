from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# Project Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR / "assets"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)

# Database file paths
MENU_DB_PATH = DATA_DIR / "menu.json"
ORDERS_DB_PATH = DATA_DIR / "orders.json"
USERS_DB_PATH = DATA_DIR / "users.json"

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key_restaurant_ai")

# Restaurant Settings
CURRENCY = "$"
GST_RATE = 0.05  # 5% GST
RESTAURANT_NAME = "RestaurantAI"
RESTAURANT_TAGLINE = "Taste the Future of Dining"
