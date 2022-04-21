FROM python:latest
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN mkdir /app
RUN mkdir /root/Downloads
ADD src /app/src
ADD static /app/static
ADD templates /app/templates
ADD tests /app/tests
ADD app.py /app/app.py
ADD categoryurls.py /app/categoryurls.py
ADD config_manager.py /app/config_manager.py
ADD config.ini /app/config.ini
ADD contract_rates_job_search.py /app/contract_rates_job_search.py
ADD definitions.py /app/definitions.py
ADD main.py /app/main.py
ADD setup.py /app/setup.py
WORKDIR /app
CMD python app.py
