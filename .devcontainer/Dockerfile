
FROM armck/python-base:1.1

ARG DOTNET_VERSION=6.0

# ----- Environment Setup -----

# Set Workspace directory
ARG WORKSPACE=/workspaces/mail-to-me
ENV WORKSPACE=${WORKSPACE}

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# ----- Primary Installs -----
# uses tmp install directory to keep from caching install downloads

RUN mkdir /tmp/dockerinstall \
    && cd /tmp/dockerinstall \
    # Install supporting packages
    && apt-get update \
    && apt-get install -y \
    apt-transport-https \
    wget \
    # Add microsoft package signing key
    && wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && rm packages-microsoft-prod.deb \
    # Install .NET
    && apt-get update \
    && ACCEPT_EULA=Y apt-get -y install --no-install-recommends \
    dotnet-sdk-${DOTNET_VERSION}  \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/dockerinstall

COPY ./src/api/poetry.lock ./src/api/pyproject.toml ${WORKSPACE}/src/api/
RUN cd $WORKSPACE/src/api && poetry install --no-root

# ----- Workspace Prep -----
WORKDIR ${WORKSPACE}

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog
