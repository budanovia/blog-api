FROM python:3.10-slim-bookworm 
# (python) base image

WORKDIR /usr/src/app
# specify working directory

COPY ./requirements.txt .
# first, add in requirements.txt to docker image

RUN pip install -r requirements.txt
# download all required dependencies, then the rest of code

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY . .
# now copy the rest of local directory to docker image

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# define the command to run app when the container starts
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "-b", "0.0.0.0:8000"]
