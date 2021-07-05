from deta import Deta
from decouple import config

DB = Deta(config('DATABASE_KEY'))
SUBJECTS = DB.Base('subject')
LABS = DB.Base('lab')


def get_subject(code: str):
    return SUBJECTS.get(key=code)


def get_subjects(year: int = -1):
    if year == 0:
        return []
    if year == -1:
        return next(SUBJECTS.fetch())
    return next(SUBJECTS.fetch({'year': year}))


def get_labs(year: int = -1):
    if year == 0:
        return []
    if year == -1:
        return next(LABS.fetch())
    return next(LABS.fetch({'year': year}))
