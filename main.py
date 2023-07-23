from src.Blizzard.BlizzardClient import BlizzardClient
from src.Blizzard.BlizzardService import BlizzardService
import asyncio


async def main():
    l = await BlizzardClient.getAuctionHouse(11)


asyncio.run(main())
