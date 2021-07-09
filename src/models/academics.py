from pydantic import BaseModel
from typing import List


class Subject(BaseModel):
    key: str
    name: str


class Lab(BaseModel):
    key: str
    name: str
    abbreviation: str


class Semester(BaseModel):
    SUBJECTS: List[Subject]
    LABS: List[Lab]


class Year(BaseModel):
    ODD_SEMESTER: Semester
    EVEN_SEMESTER: Semester
