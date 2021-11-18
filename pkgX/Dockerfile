FROM python:3.8
WORKDIR /airflow-iguazio/pkgX
COPY requirements.txt /airflow-iguazio
RUN pip install -r requirements
COPY dist/airflow_iguazio-1.0-py3.8.egg /airflow-iguazio
