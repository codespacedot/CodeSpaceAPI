from deta import Deta
from decouple import config

DB = Deta(config('DATABASE_KEY'))
SUBJECTS = DB.Base('subject')
LABS = DB.Base('lab')

YEAR_MAP = {'second': 2, 'third': 3, 'final': 4}


def get_subject(code: str):
    return SUBJECTS.get(key=code)


def get_subjects(year: str = None):
    if not year:
        return next(SUBJECTS.fetch())
    try:
        return next(SUBJECTS.fetch({'year': YEAR_MAP[year]}))
    except KeyError:
        return


def get_labs(year: str = None):
    if not year:
        return next(LABS.fetch())
    try:
        return next(LABS.fetch({'year': YEAR_MAP[year]}))
    except KeyError:
        return
