from core.configs import settings
from core.database import engine

async def create_tables()-> None:
    import models._all_models
    print('testeee')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
        print('tabela criada')

if __name__ == '__main__':
    import asyncio 
    asyncio.run(create_tables())