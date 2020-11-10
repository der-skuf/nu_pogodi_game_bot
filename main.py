import asyncio

from game import Game


async def main():
    await Game.start()

    return True


if __name__ == '__main__':
    asyncio.run(main())
