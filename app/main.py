import customtkinter as ctk
from app.router import AppRouter

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Contract Arbitrage Dashboard")
        self.geometry("1200x800")

        self.router = AppRouter(self)
        self.router.pack(fill="both", expand=True)

def run_app():
    app = MainApp()
    app.mainloop()
