FROM python:3.10

COPY ./requirements.txt /api/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /api/requirements.txt

WORKDIR rest_api

COPY . /rest_api

EXPOSE 7500


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]