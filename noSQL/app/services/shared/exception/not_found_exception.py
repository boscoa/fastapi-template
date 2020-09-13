from fastapi import HTTPException


class EntityNotFoundException(HTTPException):
    def __init__(self, entity_name: str, entity_id: str):
        super().__init__(404, f'The entity {entity_name} with id {entity_id} does not exist.')
