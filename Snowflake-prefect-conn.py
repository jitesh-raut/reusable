from prefect_snowflake.database import SnowflakeConnector
from prefect import flow, task
from prefect_snowflake import SnowflakeConnector
import asyncio

@task
async def setup_table(block_name: str) -> None:
    with await SnowflakeConnector.load(block_name) as connector:
        await connector.execute(
            "CREATE TABLE IF NOT EXISTS customers_test (name varchar, address varchar);"
        )
        await connector.execute_many(
            "INSERT INTO customers_test (name, address) VALUES (%(name)s, %(address)s);",
            seq_of_parameters=[
                {"name": "Ford", "address": "Highway 42"},
                {"name": "Unknown", "address": "Space"},
                {"name": "Me", "address": "Myway 88"},
            ],
        )

@task
async def fetch_data(block_name: str) -> list:
    all_rows = []
    with await SnowflakeConnector.load(block_name) as connector:
        while True:
            # Repeated fetch* calls using the same operation will
            # skip re-executing and instead return the next set of results
            new_rows = await connector.fetch_many("SELECT * FROM customers_test", size=2)
            if len(new_rows) == 0:
                break
            all_rows.append(new_rows)
    return all_rows

@flow
async def snowflake_flow(block_name: str) -> list:
    await setup_table(block_name)
    all_rows = await fetch_data(block_name)
    return all_rows


if __name__=="__main__":
    asyncio.run(snowflake_flow("snowflake-connection-block"))
