"""Pydantic schemas for Academics API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '09/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from pydantic import BaseModel
from typing import List


class Subject(BaseModel):
    """To be used inside semester."""
    key: str
    name: str


class Lab(BaseModel):
    """To be used inside semester."""
    key: str
    name: str
    abbreviation: str


class Semester(BaseModel):
    """To be used inside year."""
    SUBJECTS: List[Subject]
    LABS: List[Lab]


class Year(BaseModel):
    """Year data"""
    ODD_SEMESTER: Semester
    EVEN_SEMESTER: Semester
