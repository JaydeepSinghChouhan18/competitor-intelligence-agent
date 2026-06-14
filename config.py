from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = "llama-3.3-70b-versatile"

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

CHROMA_DB_PATH = "chroma_db"

SCREENSHOT_DIR = "screenshots"

SNAPSHOT_DIR = "snapshots"

REPORT_DIR = "reports"