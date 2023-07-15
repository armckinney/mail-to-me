import os


class EnvironmentConfigurationProvider:
    def get(self, key: str) -> str:
        return os.environ.get(key)
