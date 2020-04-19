from bson import ObjectId
from fastapi import HTTPException

from app.models.bar import BarMongo, Bar, BarContract
from app.services.shared.exception.not_found_exception import EntityNotFoundException


async def get_bar(db, bar_id: str):
    doc = await db.bars.find_one({"_id": ObjectId(bar_id)})

    if not doc:
        raise EntityNotFoundException(BarMongo.__name__, bar_id)

    return BarMongo(**doc)


async def list_bar(db):
    return [BarMongo(**doc) for doc in await db.bars.find({}).to_list(length=100)]


async def create_bar(db, bar: BarContract):
    return Bar(**bar.dict(), bar_id=str((await db.bars.insert_one(bar.dict())).inserted_id))


async def delete_bar(db, bar_id: str):
    if not await db.bars.find_one({"_id": ObjectId(bar_id)}):
        raise EntityNotFoundException(BarMongo.__name__, bar_id)

    await db.bars.delete_one({"_id": ObjectId(bar_id)})


async def update_bar(db, bar_id: str, bar: BarContract):
    object_id = ObjectId(bar_id)
    doc = await db.bars.find_one({"_id": object_id})
    if not doc:
        raise EntityNotFoundException(BarMongo.__name__, bar_id)

    result = await db.bars.replace_one({"_id": object_id}, bar.dict())

    if not result.acknowledged:
        raise HTTPException(400)

    return Bar(**bar.dict(), bar_id=bar_id)
