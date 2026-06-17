from datetime import date

from Domain.studiengang import Studiengang
from Domain.semester import Semester
from Domain.Modul import Modul
from Domain.pruefungsleistung import Pruefungsleistung

class StudiengangRepository:

    def hole_studiengang_daten(
        self
    ) -> Studiengang:

        studiengang = Studiengang(
            name="Wirtschaftsinformatik",
            zielschnitt=2.0
        )

        semester1 = Semester(
            nummer=1
        )

        semester1.fuege_modul_hinzu(
            Modul(
                name="Einführung in die Informatik",
                ects=5,
                pruefungsleistung=
                Pruefungsleistung(
                    datum=date(2025, 2, 1),
                    note=2.3
                )
            )
        )

        semester1.fuege_modul_hinzu(
            Modul(
                name="Mathematik",
                ects=5,
                pruefungsleistung=
                Pruefungsleistung(
                    datum=date(2025, 2, 15),
                    note=2.7
                )
            )
        )

        semester2 = Semester(
            nummer=2
        )

        semester2.fuege_modul_hinzu(
            Modul(
                name="Programmierung in Python",
                ects=5,
                pruefungsleistung=
                Pruefungsleistung(
                    datum=date(2025, 7, 1),
                    note=1.7
                )
            )
        )

        semester2.fuege_modul_hinzu(
            Modul(
                name="Datenbanken",
                ects=5,
                pruefungsleistung=
                Pruefungsleistung(
                    datum=date(2025, 7, 15),
                    note=2.0
                )
            )
        )

        semester3 = Semester(
            nummer=3
        )

        semester3.fuege_modul_hinzu(
            Modul(
                name="Software Engineering",
                ects=5
            )
        )

        studiengang.fuege_semester_hinzu(
            semester1
        )

        studiengang.fuege_semester_hinzu(
            semester2
        )

        studiengang.fuege_semester_hinzu(
            semester3
        )

        return studiengang