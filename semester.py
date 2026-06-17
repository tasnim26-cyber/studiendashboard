from dataclasses import dataclass, field
from Domain.Modul import Modul

@dataclass
class Semester:
    """
    Repräsentiert ein Semester.
    """
    nummer: int
    module: list[Modul] = field(default_factory=list)

    def fuege_modul_hinzu(self, modul: Modul) -> None:
        self.module.append(modul)