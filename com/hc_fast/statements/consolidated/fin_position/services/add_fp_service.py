# statements/consolidated/financial_position/service.py
from typing import List
from uuid import UUID
from fastapi import HTTPException
from com.hc_fast.statements.consolidated.fin_position.model.fp_schema import FpSchema

class BSTemplateService:
    def __init__(self, db):
        self.db = db

    async def get_fp(self, company_id: UUID) -> List[FpSchema]:
        query = """
            SELECT id, name, indent 
            FROM bs_template
            WHERE company_id = $1
            ORDER BY id
        """
        records = await self.db.fetch(query, company_id)
        return [FpSchema(**record) for record in records]

    async def add_fp(self, company_id: UUID, item: FpSchema) -> None:
        query = """
            INSERT INTO bs_template (id, company_id, name, indent)
            VALUES ($1, $2, $3, $4)
        """
        await self.db.execute(query, item.id, company_id, item.name, item.indent)

    async def modify_fp(self, item_id: UUID, name: str, indent: int) -> None:
        query = """
            UPDATE bs_template
            SET name = $1, indent = $2, updated_at = now()
            WHERE id = $3
        """
        result = await self.db.execute(query, name, indent, item_id)
        if result == "UPDATE 0":
            raise HTTPException(status_code=404, detail="Item not found")

    async def delete_fp(self, item_id: UUID) -> None:
        query = """
            DELETE FROM bs_template
            WHERE id = $1
        """
        result = await self.db.execute(query, item_id)
        if result == "DELETE 0":
            raise HTTPException(status_code=404, detail="Item not found")