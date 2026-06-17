import tkinter as tk
from dashboard_dto import DashboardDatenDTO

class DashboardGUIView:
    """
    Stellt die Dashboard-Daten in einer grafischen Benutzeroberfläche dar.
    """

    def zeige_dashboard(
        self,
        daten: DashboardDatenDTO
    ) -> None:

        fenster = tk.Tk()
        fenster.title("Studien-Dashboard")
        fenster.geometry("400x250")

        titel = tk.Label(
            fenster,
            text="🎓 STUDIEN-DASHBOARD 🎓",
            font=("Arial", 14, "bold")
        )
        titel.pack(pady=10)

        tk.Label(
            fenster,
            text=f"Aktuelles Semester: {daten.aktuelles_semester}"
        ).pack(pady=5)

        tk.Label(
            fenster,
            text=f"ECTS-Stand: {daten.ects_stand} / 180"
        ).pack(pady=5)

        tk.Label(
            fenster,
            text=f"Notendurchschnitt: {daten.notendurchschnitt:.2f}"
        ).pack(pady=5)

        tk.Label(
            fenster,
            text=f"Zielschnitt: {daten.zielschnitt:.2f}"
        ).pack(pady=5)

        fenster.mainloop()
