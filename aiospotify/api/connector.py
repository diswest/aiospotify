import asyncio


class Connector:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self._loop = loop

    def is_open(self) -> bool:
        return True

    def close(self):
        pass
