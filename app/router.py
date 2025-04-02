import customtkinter as ctk
from app.views.strategy_builder import StrategyBuilder
from app.views.contract_manager import ContractManager
from app.views.deployment_status import DeploymentStatus
from app.views.profit_tracker import ProfitTracker
from app.views.arbitrage_opportunities import ArbitrageOpportunities
from app.views.settings import Settings

class AppRouter(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.sidebar = ctk.CTkFrame(self, width=200)
        self.sidebar.pack(side="left", fill="y")

        self.content = ctk.CTkFrame(self)
        self.content.pack(side="right", fill="both", expand=True)

        self.tabs = {
            "Strategy Builder": StrategyBuilder,
            "Contract Manager": ContractManager,
            "Deployment Status": DeploymentStatus,
            "Profit Tracker": ProfitTracker,
            "Arbitrage Opportunities": ArbitrageOpportunities,
            "Settings": Settings
        }

        for name in self.tabs:
            btn = ctk.CTkButton(self.sidebar, text=name, command=lambda n=name: self.load_tab(n))
            btn.pack(pady=5, padx=10, fill="x")

        self.active_tab = None
        self.load_tab("Strategy Builder")

    def load_tab(self, name):
        if self.active_tab:
            self.active_tab.pack_forget()
            self.active_tab.destroy()
        self.active_tab = self.tabs[name](self.content)
        self.active_tab.pack(fill="both", expand=True)
