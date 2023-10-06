FROM python:3.11-bullseye

RUN groupadd app_group
RUN useradd -m -g app_group app_user
RUN usermod -aG app_group app_user

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

#RUN mkdir -p file_uploads

#CMD python3 -m app.main
CMD uvicorn app.main:app --host $CONTAINER_HOST --port $CONTAINER_PORT