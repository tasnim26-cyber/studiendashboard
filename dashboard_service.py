from Domain.studiengang import Studiengang

class DashboardService:
    """
    Enthält fachliche Berechnungen.
    """

    def berechne_gesamt_ects(
        self,
        studiengang: Studiengang
    ) -> int:

        return sum(
            modul.ects
            for semester in studiengang.semester
            for modul in semester.module
            if modul.ist_erfolgreich_abgeschlossen()
        )

    def berechne_notendurchschnitt(
        self,
        studiengang: Studiengang
    ) -> float:

        gewichtete_summe = 0.0
        gesamt_ects = 0

        for semester in studiengang.semester:
            for modul in semester.module:

                note = modul.note()

                if note is not None:

                    gewichtete_summe += (
                        note * modul.ects
                    )

                    gesamt_ects += modul.ects

        if gesamt_ects == 0:
            return 0.0

        return round(
            gewichtete_summe / gesamt_ects,
            2
        )