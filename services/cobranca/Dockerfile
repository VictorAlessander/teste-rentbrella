FROM python:3.7

COPY . /cobrancaapp

WORKDIR /cobrancaapp

RUN pip install -r requirements.txt

CMD ["chmod +x start.sh"]
CMD ["./start.sh"]
