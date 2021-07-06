from fastapi import APIRouter, status
from src.core import academics as core

router = APIRouter(prefix='/academics', tags=['Academics'])


@router.get('/year/{year}', status_code=status.HTTP_200_OK)
def data_for_year(year: str):
    return core.get_data_for_year(year)
