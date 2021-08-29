import asyncio
from webapi.db.config import engine, Base, async_session
from webapi.db.models import *
from webapi.setting import settings


async def init_admin():
    async with async_session() as session:
        async with session.begin():
            admin = User(
                username=settings.ADMIN_USERNAME,
                password_hash=User.get_password_hash(settings.ADMIN_PASSWORD),
                nickname=settings.ADMIN_NICKNAME,
                email=settings.ADMIN_EMAIL
            )
            session.add(admin)


async def init_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await init_admin()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_table())
