import asyncio

from game import HTMLGameLauncher


async def main():
    game_has_ready = await HTMLGameLauncher.has_launched()
    if game_has_ready:
        print('ready to start')
    else:
        print('failed')

    return True


if __name__ == '__main__':
    asyncio.run(main())
