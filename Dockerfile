# Using Python Slim-Buster
FROM v-ex/venz-userbot:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By v-ex-Userbot ━━━━━

RUN git clone -b venz-Userbot https://github.com/eldy020502/venz-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/eldy020502/venz-Userbot/venz-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
