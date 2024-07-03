FROM debian:testing
    MAINTAINER Arun Mani J <j.arunmani@proton.me>

RUN apt-get update && apt-get install -y python3 python3-pip --no-install-recommends
COPY . DoNotRepeatBot
WORKDIR DoNotRepeatBot
RUN pip install -r requirements.txt --break-system-packages

ENV TOKEN=""
ENV DATABASE_URL=""

ENV INTERVAL="2"

ENV LISTEN="0.0.0.0"
ENV PORT="80"
ENV URL_PATH=""
ENV WEBHOOK_URL=""

ENTRYPOINT python3 -m DoNotRepeatBot
