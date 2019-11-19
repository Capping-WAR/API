FROM python:3.7
RUN apt-get update -y \
    && apt-get install -y \
        libpq-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

# Install pgapi package
WORKDIR /usr/src/app/database/pgapi
RUN make build \
    && make install

EXPOSE 8080

WORKDIR /usr/src/app
ENTRYPOINT ["python3"]
CMD ["run.py"]
# CMD ["-m", "swagger_server"]