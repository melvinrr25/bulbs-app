FROM nickgryg/alpine-pandas:latest
ARG port
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install python-dotenv
COPY . .
ENV PORT=$port
EXPOSE $PORT
CMD gunicorn app:server --bind 0.0.0.0:$PORT --preload
