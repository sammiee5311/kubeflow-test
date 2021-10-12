FROM tensorflow/tensorflow:latest-py3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt
ENTRYPOINT ["python", "train_dataset.py"]