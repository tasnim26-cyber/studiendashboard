from dataclasses import dataclass
from datetime import date

@dataclass
class Pruefungsleistung:
    """
    Repräsentiert die Prüfungsleistung eines Moduls.
    Enthält das Prüfungsdatum und die erzielte Note.
    """
    datum: date
    note: float | None = None  # None bedeutet, dass das Modul noch nicht bewertet wurde

    def ist_bewertet(self) -> bool:
        """Überprüft, ob bereits eine Benotung eingetragen wurde."""
        return self.note is not None

    def ist_bestanden(self) -> bool:
        """
        Prüft nach deutschen Hochschulrichtlinien, ob die Prüfung bestanden ist.
        Eine Note bis einschließlich 4.0 gilt als bestanden.
        """
        if self.note is None:
            return False
        return self.note <= 4.0

    def setze_note(self, neue_note: float) -> None:
        """Validiert den gültigen Wertebereich deutscher Hochschulnoten (1.0 bis 5.0)."""
        if not (1.0 <= neue_note <= 5.0):
            raise ValueError("Eine Note muss zwingend zwischen 1.0 und 5.0 liegen.")
        self.note = neue_note