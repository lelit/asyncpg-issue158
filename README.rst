===========================
 Experiments on issue158__
===========================

__ https://github.com/MagicStack/asyncpg/issues/158

Howto
=====

* Install docker-compose::

    python3.6 -m venv env
    source env/bin/activate
    pip install docker-compose

* Build the services images::

    docker-compose build

* Run test against PostgreSQL 9.6.3

  ::

    docker-compose run --rm test9

  Output::

    docker-compose run --rm test9
    Creating issue158_pg9_1 ...
    Creating issue158_pg9_1 ... done
    Database at pg9:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg9:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg9:5432 is not ready yet, sleeping for 15 seconds...
    ........................................................................................................................................................................................................

* Run test againt PostgreSQL 10b2

  ::

    docker-compose run --rm test10

  Output::

    Creating issue158_pg10_1 ...
    Creating issue158_pg10_1 ... done
    Database at pg10:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg10:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg10:5432 is not ready yet, sleeping for 15 seconds...
    ..........Traceback (most recent call last):
      File "/tmp/issue158.py", line 44, in <module>
        main()
      File "/tmp/issue158.py", line 42, in main
        loop.run_until_complete(workhorse(loop, pghost))
      File "/usr/local/lib/python3.6/asyncio/base_events.py", line 467, in run_until_complete
        return future.result()
      File "/tmp/issue158.py", line 34, in workhorse
        pool = await get_pool(loop, pghost)
      File "/tmp/issue158.py", line 28, in get_pool
        loop=loop)
      File "/usr/local/lib/python3.6/site-packages/asyncpg/pool.py", line 349, in _async__init__
        await asyncio.gather(*connect_tasks, loop=self._loop)
      File "/usr/local/lib/python3.6/site-packages/asyncpg/pool.py", line 138, in connect
        connection_class=self._pool._connection_class)
      File "/usr/local/lib/python3.6/site-packages/asyncpg/connect_utils.py", line 274, in _connect_addr
        await asyncio.wait_for(connected, loop=loop, timeout=timeout)
      File "/usr/local/lib/python3.6/asyncio/tasks.py", line 358, in wait_for
        return fut.result()
    asyncpg.exceptions.InvalidPasswordError: password authentication failed for user "pgu"
