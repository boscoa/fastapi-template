from typing import List

from fastapi import APIRouter, Depends

from middleware import get_db
from models import Bar, BarContract
from foo import bar_service

router = APIRouter()


@router.get(FOO_ROUTES, response_model=List[Bar])
async def list_bar(db=Depends(get_db)):
    return await bar_service.list_bar(db)


@router.get(FOO_ROUTE, response_model=BarContract)
async def get(bar_id: str, db=Depends(get_db)):
    return await bar_service.get_bar(db, bar_id)


@router.post(FOO_ROUTES)
async def create_bar(bar: BarContract, db=Depends(get_db)):
    return await bar_service.create_bar(db, bar)


@router.put(FOO_ROUTE, response_model=BarContract)
async def update_bar(bar_id: str, bar: BarContract, db=Depends(get_db)):
    return await bar_service.update_bar(db, bar_id, bar)


@router.patch(FOO_ROUTE, response_model=BarContract)
async def patch_bar(bar_id: str, bar: BarContract, db=Depends(get_db)):
    pass
