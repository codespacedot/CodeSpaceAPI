from deta import Deta
from decouple import config

DB = Deta(config('DATABASE_KEY'))
SUBJECTS = DB.Base('subject')
LABS = DB.Base('lab')


def get_subject(code: str):
    return SUBJECTS.get(key=code)


def get_subjects(year: str = None):
    if not year:
        return next(SUBJECTS.fetch())
    return next(SUBJECTS.fetch({'year': year}))


def get_labs(year: str = None):
    if not year:
        return next(LABS.fetch())
    return next(LABS.fetch({'year': year}))
