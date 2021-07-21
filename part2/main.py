from kivymd.app import MDApp
from farmersmapview import FarmersMapView
import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "markets.db")

class MainApp(MDApp):
    connection = None
    cursor = None

    def on_start(self):
        # Initialize GPS

        # Connect to database
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

        # Instantiate SearchPopupMenu

MainApp().run()
