FROM python:3.7

COPY . /emprestimoapp
WORKDIR /emprestimoapp
RUN pip install -r requirements.txt
CMD ["chmod +x ./start.sh"]
CMD ["./start.sh"]
