from .persistent import bar_repository
from ...models.bar import Bar, BarMongo, BarContract


def get_bar_from_mongo_bar(bar_mongo: BarMongo):
    return Bar(**bar_mongo.dict(), bar_id=str(bar_mongo.mongo_id))


async def get_bar(db, bar_id: str):
    return get_bar_from_mongo_bar(await bar_repository.get_bar(db, bar_id))


async def list_bar(db):
    return [get_bar_from_mongo_bar(doc) for doc in await bar_repository.list_bar(db)]


async def create_bar(db, bar: BarContract):
    return await bar_repository.create_bar(db, bar)


async def delete_bar(db, bar_id: str):
    await bar_repository.delete_bar(db, bar_id)


async def update_bar(db, bar_id: str, bar: BarContract):
    return await bar_repository.update_bar(db, bar_id, bar)
