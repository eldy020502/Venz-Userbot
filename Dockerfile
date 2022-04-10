# Using Python Slim-Buster
FROM kyyex/kyy-userbot:busterv2
#━━━━━ VenzUserbot ━━━━━

RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
    
RUN git clone -b Venz-Userbot https://github.com/eldy020502/Venz-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Rexashh/Venz-Userbot/Venz-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
