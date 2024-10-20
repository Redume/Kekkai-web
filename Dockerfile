FROM python:3.12

WORKDIR /

COPY ./requirements.txt ./

RUN pip3 install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

EXPOSE 9000

CMD ["python", "main.py"]