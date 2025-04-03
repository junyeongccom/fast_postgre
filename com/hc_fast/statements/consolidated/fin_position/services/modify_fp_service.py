from uuid import UUID
from fastapi import HTTPException

class ModifyFpService:
    def __init__(self, db):
        self.db = db

    async def modify_fp(self, item_id: UUID, name: str, indent: int) -> None:
        query = """
            UPDATE bs_template
            SET name = $1, indent = $2, updated_at = now()
            WHERE id = $3
        """
        result = await self.db.execute(query, name, indent, item_id)
        if result == "UPDATE 0":
            raise HTTPException(status_code=404, detail="Item not found")
