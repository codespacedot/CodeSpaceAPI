"""Pydantic schemas for Academics API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from typing import List
from pydantic import BaseModel


class Subject(BaseModel):
    """Used inside semester."""
    key: str
    name: str
    abbreviation: str


class Lab(BaseModel):
    """Used inside semester."""
    key: str
    name: str
    abbreviation: str


class Semester(BaseModel):
    """Used inside year."""
    SUBJECTS: List[Subject]
    LABS: List[Lab]


class Year(BaseModel):
    """Year data."""
    ODD_SEMESTER: Semester
    EVEN_SEMESTER: Semester


class Resource(BaseModel):
    """Used Resource category."""
    title: str
    url: str


class Resources(BaseModel):
    """Resources of a subject."""
    LIBRARY: List[Resource]
    EXAM: List[Resource]
