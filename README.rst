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
    Creating network "asyncpgissue158_default" with the default driver
    Creating asyncpgissue158_pg9_1 ...
    Creating asyncpgissue158_pg9_1 ... done
    Database at pg9:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg9:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg9:5432 is not ready yet, sleeping for 15 seconds...
    .................................................................................................... Ok!

* Run test againt PostgreSQL 10b4

  ::

    docker-compose run --rm test10

  Output::

    docker-compose run --rm test10
    Creating asyncpgissue158_pg10_1 ...
    Creating asyncpgissue158_pg10_1 ... done
    Database at pg10:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg10:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg10:5432 is not ready yet, sleeping for 15 seconds...
    .................................................................................................... Ok!

With plain docker
=================

* Execute postgres-issue308.sh::

    $ sh postgres-issue308.sh
    + docker build -t issue158 .
    Sending build context to Docker daemon  102.4kB
    Step 1/5 : FROM python:3.6.2
     ---> d3e1aad6d2e7
    Step 2/5 : RUN pip install --no-cache-dir cython
     ---> Using cache
     ---> 3c3a940abfd9
    Step 3/5 : RUN pip install --no-cache-dir https://github.com/MagicStack/asyncpg/archive/master.zip
     ---> Using cache
     ---> b90c2c5cbfa3
    Step 4/5 : COPY issue158.py /tmp/
     ---> Using cache
     ---> f2f32fdd2783
    Step 5/5 : ENTRYPOINT python3.6 /tmp/issue158.py
     ---> Using cache
     ---> 63f5774ced4c
    Successfully built 63f5774ced4c
    Successfully tagged issue158:latest
    + docker run --name pg9 -e POSTGRES_USER=pgu -e POSTGRES_PASSWORD=ugp -d postgres:9.6.3
    + pg9c=1d42bcbc5cb21d2b0077e8807d3e7f6a3b6ab7e7a9f89b6122b9698d6d47df1c
    + docker run --rm -ti --link pg9:pg issue158 pg
    Database at pg:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg:5432 is not ready yet, sleeping for 15 seconds...
    .................................................................................................... Ok!
    + docker stop 1d42bcbc5cb21d2b0077e8807d3e7f6a3b6ab7e7a9f89b6122b9698d6d47df1c
    1d42bcbc5cb21d2b0077e8807d3e7f6a3b6ab7e7a9f89b6122b9698d6d47df1c
    + docker rm -v 1d42bcbc5cb21d2b0077e8807d3e7f6a3b6ab7e7a9f89b6122b9698d6d47df1c
    1d42bcbc5cb21d2b0077e8807d3e7f6a3b6ab7e7a9f89b6122b9698d6d47df1c
    + docker run --name pg10 -e POSTGRES_USER=pgu -e POSTGRES_PASSWORD=ugp -d postgres:10-beta4
    + pg10c=ecaadbc6163bc611ed9291719160261c7de9d41969e50950de3ac8c3faa55047
    + docker run --rm -ti --link pg10:pg issue158 pg
    Database at pg:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg:5432 is not ready yet, sleeping for 15 seconds...
    Database at pg:5432 is not ready yet, sleeping for 15 seconds...
    .................................................................................................... Ok!
    + docker stop ecaadbc6163bc611ed9291719160261c7de9d41969e50950de3ac8c3faa55047
    ecaadbc6163bc611ed9291719160261c7de9d41969e50950de3ac8c3faa55047
    + docker rm -v ecaadbc6163bc611ed9291719160261c7de9d41969e50950de3ac8c3faa55047
    ecaadbc6163bc611ed9291719160261c7de9d41969e50950de3ac8c3faa55047
