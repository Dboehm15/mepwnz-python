from src.Blizzard.BlizzardClient import BlizzardClient
from src.Blizzard.models.Service import AhListing, AhListings


class BlizzardService(object):
    @staticmethod
    async def getRealmIdByServerName(serverName: str) -> int:
        realm = BlizzardClient.getConnectedRealmMeta(1)
        for result in realm.results:
            for realm in result.data.realms:
                if realm.name.en_US.upper() == serverName.upper():
                    return realm.id

        return 0

    @staticmethod
    async def listAllServers():
        realm = BlizzardClient.getConnectedRealmMeta(1)
        for result in realm.results:
            for realm in result.data.realms:
                print("server: " + str(realm.name.en_US) + " id: " + str(realm.id))

    @staticmethod
    async def getAuctions(serverId: int) -> AhListings:
        auctionHouse = await BlizzardClient.getAuctionHouse(serverId)
        listings = []

        for auction in auctionHouse.auctions:
            name = await BlizzardClient.getItemDetails(auction.item.id)
            L = AhListing(
                id=auction.id,
                name=name.name,
                buyout=auction.buyout,
                bid=auction.bid,
                quantity=auction.quantity,
                timeLeft=auction.time_left)
            print(L)
            listings.append(L)
        return AhListings(listings=listings)
