from dashboard_service import DashboardService
from studiengang_repository import StudiengangRepository
from dashboard_dto import DashboardDatenDTO

class DashboardController:

    def __init__(
        self,
        repository: StudiengangRepository,
        service: DashboardService
    ):
        self._repository = repository
        self._service = service

    def lade_dashboard_daten(
        self
    ) -> DashboardDatenDTO:

        studiengang = (
            self._repository
            .hole_studiengang_daten()
        )

        return DashboardDatenDTO(
            aktuelles_semester=len(
                studiengang.semester
            ),
            ects_stand=self._service
                .berechne_gesamt_ects(
                    studiengang
                ),
            notendurchschnitt=self._service
                .berechne_notendurchschnitt(
                    studiengang
                ),
            zielschnitt=
                studiengang.zielschnitt
        )