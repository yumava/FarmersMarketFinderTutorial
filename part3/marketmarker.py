from kivy_garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu
import os.path

class MarketMarker(MapMarkerPopup):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(BASE_DIR, "marker.png")
    source = "marker.png"
    market_data = []

    def on_release(self):
        # Open up the LocationPopupMenu
        menu = LocationPopupMenu(self.market_data)
        menu.size_hint = [.8, .6]
        menu.open()

