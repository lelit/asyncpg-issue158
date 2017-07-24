FROM python:3.6.2-slim

RUN pip install --no-cache-dir asyncpg

COPY issue158.py /tmp/

ENTRYPOINT ["python3.6", "/tmp/issue158.py"]
