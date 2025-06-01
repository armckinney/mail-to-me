FROM armck/python:3.9.5

ARG TERRAFORM_VERSION=1.10.5

# set workspace directory
ARG WORKSPACE=/workspaces/mail-to-me
ENV WORKSPACE=${WORKSPACE}

# avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir /tmp/container \
    && cd /tmp/container \
    # signing key locations
    && mkdir -p /etc/apt/keyrings \
    # supporting installs
    && apt update && apt -y install  \
    ca-certificates \
    curl \
    gnupg \
    software-properties-common \
    wget \
    # azure cli keys and registry
    && wget -O- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/keyrings/microsoft.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/azure-cli/ $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/azure-cli.list \
    # terraform keys & registry
    && curl -fsSL https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /etc/apt/keyrings/hashicorp.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/hashicorp.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/hashicorp.list \
    # primary installs
    && apt update && apt -y install \
    azure-cli \
    terraform=${TERRAFORM_VERSION}-1 \
    # azure cli configuration
    && az extension add --name containerapp --upgrade \
    # cleanup
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/container

COPY ./poetry.lock ./pyproject.toml ${WORKSPACE}/
RUN cd $WORKSPACE/ && poetry install --no-root

WORKDIR ${WORKSPACE}

# Switch back to dialog for any ad-hoc use of apt
ENV DEBIAN_FRONTEND=dialog
