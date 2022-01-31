# Using Python Slim-Buster
FROM v-ex/Venz-userbot:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By v-ex-Userbot ━━━━━

RUN git clone -b Venz-Userbot https://github.com/eldy020502/Venz-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/eldy020502/Venz-Userbot/Venz-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
