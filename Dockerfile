FROM python:3
COPY startIpBot.py /
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir discord requests
CMD ["python3", "startIpBot.py"]
