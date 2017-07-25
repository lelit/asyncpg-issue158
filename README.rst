===========================
 Experiments on issue158__
===========================

__ https://github.com/MagicStack/asyncpg/issues/158

With docker-compose
===================

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


With plain docker
=================

* Execute postgres-issue308.sh::

    sh postgres-issue308.sh
    + docker build -t issue158 .
    Sending build context to Docker daemon  76.29kB
    Step 1/4 : FROM python:3.6.2-slim
     ---> 0622c70b79ce
    Step 2/4 : RUN pip install --no-cache-dir asyncpg
     ---> Using cache
     ---> 7a49952376af
    Step 3/4 : COPY issue158.py /tmp/
     ---> Using cache
     ---> ff6c2d1eaacf
    Step 4/4 : ENTRYPOINT python3.6 /tmp/issue158.py
     ---> Using cache
     ---> 45097312f685
    Successfully built 45097312f685
    Successfully tagged issue158:latest
    + docker run --name pg9 -e POSTGRES_USER=pgu -e POSTGRES_PASSWORD=ugp -d postgres:9.6.3
    + pg9c=a10c0a8941b64b4bed33b6e1237ca91fe29a11bae913fe4f17802e37c2c4d76c
    + docker run --rm -ti --link pg9:pg issue158 pg
    Database at pg:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg:5432 is not ready yet, sleeping for 15 seconds...
    .................................................................................................... Ok!
    + docker stop a10c0a8941b64b4bed33b6e1237ca91fe29a11bae913fe4f17802e37c2c4d76c
    a10c0a8941b64b4bed33b6e1237ca91fe29a11bae913fe4f17802e37c2c4d76c
    + docker rm -v a10c0a8941b64b4bed33b6e1237ca91fe29a11bae913fe4f17802e37c2c4d76c
    a10c0a8941b64b4bed33b6e1237ca91fe29a11bae913fe4f17802e37c2c4d76c
    + docker run --name pg10 -e POSTGRES_USER=pgu -e POSTGRES_PASSWORD=ugp -d postgres:10-beta2
    + pg10c=95a30998a2110b19a66aac7ac55f085381d81facdc36804cfef4dafbf646cd0f
    + docker run --rm -ti --link pg10:pg issue158 pg
    Database at pg:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg:5432 is not ready yet, sleeping for 15 seconds...
    .......Traceback (most recent call last):
      File "/tmp/issue158.py", line 45, in <module>
        main()
      File "/tmp/issue158.py", line 43, in main
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
    + docker stop 95a30998a2110b19a66aac7ac55f085381d81facdc36804cfef4dafbf646cd0f
    95a30998a2110b19a66aac7ac55f085381d81facdc36804cfef4dafbf646cd0f
    + docker rm -v 95a30998a2110b19a66aac7ac55f085381d81facdc36804cfef4dafbf646cd0f
    95a30998a2110b19a66aac7ac55f085381d81facdc36804cfef4dafbf646cd0f
