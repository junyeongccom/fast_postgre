from uuid import UUID
from fastapi import HTTPException

class DeleteFpService:
    def __init__(self, db):
        self.db = db

    async def delete_fp(self, item_id: UUID) -> None:
        query = """
            DELETE FROM bs_template
            WHERE id = $1
        """
        result = await self.db.execute(query, item_id)
        if result == "DELETE 0":
            raise HTTPException(status_code=404, detail="Item not found")
