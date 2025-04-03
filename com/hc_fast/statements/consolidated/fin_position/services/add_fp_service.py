# statements/consolidated/financial_position/service.py
from typing import List
from uuid import UUID
from com.hc_fast.statements.consolidated.fin_position.model.fp_schema import FpSchema

class AddFpService:
    def __init__(self, db):
        self.db = db

    async def add_fp(self, company_id: UUID, item: FpSchema) -> None:
        query = """
            INSERT INTO bs_template (id, company_id, name, indent)
            VALUES ($1, $2, $3, $4)
        """
        await self.db.execute(query, item.id, company_id, item.name, item.indent) 