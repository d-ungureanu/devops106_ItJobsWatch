FROM python:latest
ADD requirements.txt /requirements.txt
ADD src /src
ADD static /static
ADD templates /templates
ADD tests /tests
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
