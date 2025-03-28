from fastapi import Response
from com.hc_fast.account.auth.user.api.user_factory import UserFactory
from com.hc_fast.account.auth.user.model.user_action import UserAction


class UserController:
    def __init__(self):
        pass

    async def create_new_user(self,response : Response ,**kwargs):
        return await UserFactory.create(UserAction.CREATE_NEW_USER, response = response, **kwargs)
    
    async def login(self,response : Response,**kwargs):
        return await UserFactory.create(UserAction.LOGIN,response = response, **kwargs)
    
    async def logout(self,**kwargs):
        return await UserFactory.create(UserAction.LOGOUT, **kwargs)