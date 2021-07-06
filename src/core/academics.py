from . import db
from fastapi import HTTPException, status


def get_data_for_year(year: str):
    subjects = db.get_subjects(year=year)
    labs = db.get_labs(year=year)

    if not subjects or not labs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid year")

    data = {
        'ODD_SEMESTER': {
            'SUBJECTS': [],
            'LABS': []
        },
        'EVEN_SEMESTER': {
            'SUBJECTS': [],
            'LABS': []
        }
    }

    for subject in subjects:
        if subject['semester'] % 2:
            data['ODD_SEMESTER']['SUBJECTS'].append(subject)
        else:
            data['EVEN_SEMESTER']['SUBJECTS'].append(subject)

    for lab in labs:
        if lab['semester'] % 2:
            data['ODD_SEMESTER']['LABS'].append(lab)
        else:
            data['EVEN_SEMESTER']['LABS'].append(lab)

    return data
