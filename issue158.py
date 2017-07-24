import asyncio, asyncpg

def assert_database_is_up(db_host, db_port=5432, attempts=15, seconds=15):
    from socket import AF_INET, SOCK_STREAM, gaierror, socket
    from time import sleep

    s = socket(AF_INET, SOCK_STREAM)
    address = (db_host, db_port)
    while True:
        try:
            s.connect(address)
        except (ConnectionRefusedError, TimeoutError, gaierror):
            attempts -= 1
            if attempts <= 0:
                print("Giving up!")
                return False
            print("Database at %s:%s is not ready yet, sleeping for %d"
                  " seconds..." % (db_host, db_port, seconds))
            sleep(seconds)
        else:
            break
    return True

async def get_pool(loop, pghost):
    pool = await asyncpg.create_pool(user="pgu",
                                     password="ugp",
                                     host=pghost,
                                     loop=loop)
    return pool

async def workhorse(loop, pghost):
    for i in range(200):
        print(".", end="")
        pool = await get_pool(loop, pghost)
        await pool.close()

def main():
    import sys
    pghost = sys.argv[1]
    assert_database_is_up(pghost)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(workhorse(loop, pghost))

main()
