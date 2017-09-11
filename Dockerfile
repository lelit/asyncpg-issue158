FROM python:3.6.2

RUN pip install --no-cache-dir cython
RUN pip install --no-cache-dir https://github.com/MagicStack/asyncpg/archive/master.zip

COPY issue158.py /tmp/

ENTRYPOINT ["python3.6", "/tmp/issue158.py"]
