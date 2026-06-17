from dataclasses import dataclass, field
from Domain.semester import Semester

@dataclass
class Studiengang:
    """
    Repräsentiert den Studiengang.
    """
    name: str
    zielschnitt: float
    semester: list[Semester] = field(default_factory=list)

    def fuege_semester_hinzu(
        self,
        neues_semester: Semester
    ) -> None:
        self.semester.append(neues_semester)