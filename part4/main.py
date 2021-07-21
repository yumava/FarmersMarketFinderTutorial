from kivymd.app import MDApp
from farmersmapview import FarmersMapView
import sqlite3
from searchpopupmenu import SearchPopupMenu
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "markets.db")

class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        self.theme_cls.primary_palette = 'BlueGray'
        # Initialize GPS

        # Connect to database
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

        # Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()

MainApp().run()
