FROM kyyex/kyy-userbot:busterv2
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Venz-Userbot https://github.com/eldy020502/Venz-Userbot /home/Venz-Userbot/ \
    && chmod 777 /home/Venz-Userbot \
    && mkdir /home/Venz-Userbot/bin/
WORKDIR /home/Venz-Userbot/
COPY ./sample_config.env ./config.env* /home/Venz-Userbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
