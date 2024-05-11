import asyncio

class ServerMessageQueue:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.queue = asyncio.Queue()

    async def receive(self):
        return await self.queue.get()

    async def send(self, message):
        await self.queue.put(message)

class ClientMessageQueue:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.queue = asyncio.Queue()

    async def receive(self):
        return await self.queue.get()

    async def send(self, message):
        await self.queue.put(message)
