# Modify this Procfile to fit your needs
web: gunicorn --keyfile=./key.pem --certfile=./cert.pem -k uvicorn.workers.UvicornWorker app.main:app

