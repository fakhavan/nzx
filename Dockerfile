FROM ubuntu:20.04

LABEL maintainer="zabenno"

COPY ./nzx_scraper/ /opt/

RUN apt update && DEBIAN_FRONTEND='noninteractive' apt upgrade -y && \
    DEBIAN_FRONTEND='noninteractive' apt install -y \
    python3-pip && \
    pip3 install requests beautifulsoup4 waitress flask

ENTRYPOINT [ "/bin/python3",  "/opt/nzx_data_rest.py" ]