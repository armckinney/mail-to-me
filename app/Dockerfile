FROM armck/python:3.9.5

LABEL   deployable="true" \
        decription="This is the deployable version of the WEF application container. \
        It only includes nessecary items to run the application."

# Set Working Directory
ENV WORKDIR=/west-end-financial
WORKDIR ${WORKDIR}

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Bring project files into container
COPY ./poetry.lock ./pyproject.toml ${WORKDIR}/
COPY ./app ${WORKDIR}/app

RUN cd $WORKDIR/ && poetry install --no-root --without=dev


# ----- Container Command -----
# exec commands do not run in shell by default (See: https://docs.docker.com/engine/reference/builder/#cmd)
CMD ["/bin/bash", "-c", "cd app/ && poetry run uvicorn main:app --host 0.0.0.0 --port 8008"]
