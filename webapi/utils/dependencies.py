from webapi.db.config import async_session
from webapi.db.dals.category_dal import CategoryDAL


# async def get_book_dal():
#     async with async_session() as session:
#         async with session.begin():
#             yield CategoryDAL(session)


class DALGetter:
    def __init__(self, dal_cls):
        self.dal_cls = dal_cls

    async def __call__(self):
        async with async_session() as session:
            async with session.begin():
                print(self.dal_cls)
                yield self.dal_cls(session)
