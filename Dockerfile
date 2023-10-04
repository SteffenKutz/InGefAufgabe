FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./main.py /code/main.py
COPY ./ServerApplication.py /code/ServerApplication.py
COPY ./logconfig.ini /code/logconfig.ini


EXPOSE 8080

CMD ["python", "main.py"]