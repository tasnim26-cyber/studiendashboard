from dataclasses import dataclass
from Domain.pruefungsleistung import Pruefungsleistung

@dataclass
class Modul:
    """
    Repräsentiert ein einzelnes Studienmodul mit Namen,
    ECTS-Punkten und der dazugehörigen Prüfungsleistung.
    """
    name: str
    ects: int
    pruefungsleistung: Pruefungsleistung | None = None

    def note(self) -> float | None:
        """Liefert die Note der Prüfungsleistung."""
        if (
            self.pruefungsleistung is not None
            and self.pruefungsleistung.ist_bewertet()
        ):
            return self.pruefungsleistung.note
        return None

    def ist_erfolgreich_abgeschlossen(self) -> bool:
        """Prüft, ob das Modul bestanden wurde."""
        return (
            self.pruefungsleistung is not None
            and self.pruefungsleistung.ist_bestanden()
        )