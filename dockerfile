FROM nikolaik/python-nodejs:latest
RUN apt-get update && apt-get install -y

RUN npm install -g configurable-http-proxy
RUN python3 -m pip install jupyterhub jupyterlab notebook

WORKDIR /dsastarhub
COPY jupyterhub_config.py .

RUN python3 -m pip install dockerspawner
RUN python3 -m pip install jupyter-client
RUN python3 -m pip install jupyterhub-firstuseauthenticator

EXPOSE 8000
CMD [ "jupyterhub", "-f", "/dsastarhub/jupyterhub_config.py" ]

