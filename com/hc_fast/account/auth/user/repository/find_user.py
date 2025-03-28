def get_check_user_id_stmt(user_id: str):
    print(f"🔍 사용자 ID 확인 쿼리 실행: user_id={user_id}")
    return """
        SELECT 1 FROM users
        WHERE user_id = $1
        LIMIT 1
    """, (user_id,)


def get_login_stmt(user_id: str, password: str):
    print(f"🔐 로그인 쿼리 실행: user_id={user_id}, password='***'")
    return """
        SELECT * FROM users
        WHERE user_id = $1 AND password = $2
        LIMIT 1
    """, (user_id, password)
