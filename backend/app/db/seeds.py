
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

# from models.domain.users import User
from models.schemas.users import UserInCreate
from db.repositories.users import UsersRepository
from api.routes.authentication import register
from core.settings.app import AppSettings

from db.repositories.items import ItemsRepository

from models.schemas.items import ItemInCreate
from api.routes.items.items_resource import create_new_item 
from models.schemas.comments import CommentInCreate
from api.routes.comments import create_comment_for_item
from db.repositories.comments import CommentsRepository
import asyncpg

loop = asyncio.get_event_loop()
conn = loop.run_until_complete(asyncpg.connect("postgresql://postgres:@postgres-python:5432/anythink-market"))

for i in range(301,400):
    user_create = UserInCreate(username=f'user_{i}',email=f'user_{i}@test.com',password=f'user_{i}@123')
    user_repo = UsersRepository(conn)
    settings = AppSettings()
    new_user = loop.run_until_complete(register(user_create,user_repo,settings))
    item_create = ItemInCreate(title=f'Item_{i}',description=f'description_{i}',body=f'Body_{i}')
    
    items_repo = ItemsRepository(conn)
    new_item = loop.run_until_complete(create_new_item(item_create,new_user.user,items_repo))
    comment_create = CommentInCreate(body=f'Comment_{i}')
    comments_repo = CommentsRepository(conn)
    new_comment = loop.run_until_complete(create_comment_for_item(comment_create,new_item.item,new_user.user,comments_repo))


loop.close()


 
