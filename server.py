import asyncio
from message_queues import ServerMessageQueue

async def handle_request(request):
    await asyncio.sleep(1)
    if request.startswith('request1'):
        return 'Response to request1: Success'
    elif request.startswith('request2'):
        return 'Response to request2: Success'
    elif request.startswith('request3'):
        return 'Response to request3: Failed'
    else:
        return 'Invalid request'

async def main():
    client_queue = ServerMessageQueue('CL.Q')

    while True:
        request = await client_queue.receive()
        print(f'Received request: {request}')

        response = await handle_request(request)

        await client_queue.send(response)

if __name__ == "__main__":
    asyncio.run(main())
