from studiengang_repository import StudiengangRepository
from dashboard_service import DashboardService
from studiengang_controller import DashboardController
from dashboard_view import DashboardKonsoleView

class DashboardApp:
    """
    Die Hauptklasse bildet den Programmeinstieg (Application Layer).
    """
    def start(self) -> None:
        # Composition Root: Objekte erzeugen und verknüpfen
        repository = StudiengangRepository()
        service = DashboardService()
        controller = DashboardController(repository, service)
        view = DashboardKonsoleView()
        
        # Daten über Controller laden und an View übergeben
        daten = controller.lade_dashboard_daten()
        view.zeige_dashboard(daten)

if __name__ == "__main__":
    app = DashboardApp()
    app.start()