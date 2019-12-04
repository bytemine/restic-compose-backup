import os


class Config:
    """Bag for config values"""
    def __init__(self, check=True):
        self.repository = os.environ['RESTIC_REPOSITORY']
        self.password = os.environ['RESTIC_PASSWORD']
        self.docker_base_url = os.environ.get('DOCKER_BASE_URL') or "unix://tmp/docker.sock"

        if check:
            self.check()

    def check(self):
        if not self.repository:
            raise ValueError("CONTAINER env var not set")

        if not self.password:
            raise ValueError("PASSWORD env var not set")