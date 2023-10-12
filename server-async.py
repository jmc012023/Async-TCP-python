import asyncio

# ANSI colors
server_color_prompt = "\033[91m"  # Red
HOST = '127.0.0.1'
PORT = 8000

async def handle_clients(reader, writer):
    addr = writer.get_extra_info('peername')
    print(server_color_prompt + f"Client connected from {addr}")

    while True:
        data = await reader.read(100)
        message = data.decode('utf-8')

        if message == "exit":
            writer.write(data)
            await writer.drain()

            print(server_color_prompt + f"\t{addr} -> Close the connection")
            writer.close()
            await writer.wait_closed()
            break

        print(server_color_prompt + f"\t{addr} -> {message}")

        writer.write(data)
        await writer.drain()

async def main():
    server = await asyncio.start_server(
        handle_clients, HOST, PORT
    )

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(server_color_prompt + f"Serving on {addrs}")

    async with server:
        await server.serve_forever()

asyncio.run(main())