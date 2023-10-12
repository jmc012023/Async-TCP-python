import asyncio

HOST = '127.0.0.1'
PORT = 8000

# ANSI colors
client_color_prompt = "\033[36m" # Cyan

async def client_async():
    reader, writer = await asyncio.open_connection(HOST, PORT)

    while True:
        message = input(client_color_prompt + "Digit you message -> ")

        writer.write(message.encode('utf-8'))
        await writer.drain()

        data = await reader.read(100)
        data = data.decode('utf-8')

        if data == "exit":
            print(client_color_prompt + 'Close the connection')
            writer.close()
            await writer.wait_closed()
            break

        print(client_color_prompt + f"\t Server Response -> {data}")


asyncio.run(client_async())