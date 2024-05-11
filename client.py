import asyncio
from message_queues import ClientMessageQueue

async def main():
    server_queue = ClientMessageQueue('SRV.Q')

    requests = ['request1', 'request2', 'request3']
    for request in requests:
        await server_queue.send(request)
        print(f'Sent request: {request}')

    client_queue = ClientMessageQueue('CL.Q')
    for _ in range(len(requests)):
        response = await client_queue.receive()
        print(f'Received response: {response}')

    await server_queue.close()
    await client_queue.close()

if __name__ == "__main__":
    asyncio.run(main())
