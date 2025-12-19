FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install redis

COPY . /code/

ENV PYTHONPATH="${PYTHONPATH}:/code"

#EXPOSE 8000

#CMD ["fastapi", "run", "main.py", "--port", "80"]
CMD ["fastapi", "run", "main.py", "--port", "80", "--workers", "4"]
#CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
#CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "main:app"]