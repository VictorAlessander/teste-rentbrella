FROM python:3.7

RUN mkdir /teste-rentbrella
WORKDIR /teste-rentbrella
ADD . /teste-rentbrella
RUN pip install -r requirements.txt
CMD ["./start_worker.sh"]
RUN chmod a+x ./start_worker.sh