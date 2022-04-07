FROM python:3.10

WORKDIR /usr/src/app

RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt install -y python3-pip npm

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

RUN npm install --prefix drgmik/static

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
