from typing import List
from uuid import UUID
from com.hc_fast.statements.consolidated.fin_position.model.fp_schema import FpSchema

class GetFpService:
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

def get_fp_service():
    return [
        {"id": 1, "name": "자산", "indent": 0},
        {"id": 2, "name": "유동자산", "indent": 1},
        {"id": 3, "name": "현금및현금성자산", "indent": 2},
        {"id": 4, "name": "단기금융상품", "indent": 2},
        {"id": 5, "name": "단기투자자산", "indent": 2},
        {"id": 6, "name": "매출채권", "indent": 2},
        {"id": 7, "name": "기타수취채권", "indent": 2},
        {"id": 8, "name": "기타금융자산", "indent": 2},
        {"id": 9, "name": "재고자산", "indent": 2},
        {"id": 10, "name": "당기법인세자산", "indent": 2},
        {"id": 11, "name": "매각예정자산", "indent": 2},
        {"id": 12, "name": "기타유동자산", "indent": 2},
        {"id": 13, "name": "비유동자산", "indent": 1},
        {"id": 14, "name": "관계기업 및 공동기업투자", "indent": 2},
        {"id": 15, "name": "장기투자자산", "indent": 2},
        {"id": 16, "name": "기타수취채권", "indent": 2},
        {"id": 17, "name": "기타금융자산", "indent": 2},
        {"id": 18, "name": "유형자산", "indent": 2},
        {"id": 19, "name": "사용권자산", "indent": 2},
        {"id": 20, "name": "무형자산", "indent": 2},
        {"id": 21, "name": "투자부동산", "indent": 2},
        {"id": 22, "name": "이연법인세자산", "indent": 2},
        {"id": 23, "name": "종업원급여자산", "indent": 2},
        {"id": 24, "name": "기타비유동자산", "indent": 2},
        {"id": 25, "name": "자산총계", "indent": 0}
    ]