from dataclasses import dataclass

@dataclass
class DashboardDatenDTO:

    aktuelles_semester: int
    ects_stand: int
    notendurchschnitt: float
    zielschnitt: float