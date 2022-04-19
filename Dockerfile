FROM python:latest
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN mkdir /app
ADD src /app/src
ADD static /app/static
ADD templates /app/templates
ADD tests /app/tests
ADD main.py /app/main.py
ADD config.ini /app/config.ini
ADD definitions.py /app/definitions.py
ADD setup.py /app/setup.py
ADD config_manager.py /app/config_manager.py
WORKDIR /app
CMD python main.py
