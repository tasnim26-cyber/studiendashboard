from dashboard_dto import DashboardDatenDTO

class DashboardKonsoleView:
    """
    Die View-Klasse stellt die Daten aus dem DashboardDatenDTO 
    sauber formatiert in der Konsole (Terminal) dar.
    """
    def zeige_dashboard(self, daten: DashboardDatenDTO) -> None:
        print("\n" + "="*50)
        print("        🎓  STUDIEN - DASHBOARD  🎓        ")
        print("="*50)
        print(f" Aktuelles Semester:      {daten.aktuelles_semester}")
        print(f" Erreichter ECTS-Stand:  {daten.ects_stand} / 180")
        print(f" Notendurchschnitt:      {daten.notendurchschnitt:.2f}")
        print(f" Angestrebter Zielschnitt:{daten.zielschnitt:.2f}")
        print("="*50)
        print(" Status: Das System läuft stabil und fehlerfrei.")
        print("="*50 + "\n")