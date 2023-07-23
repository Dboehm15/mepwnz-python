from src.Blizzard.models.AuctionHouse.AuctionHouse import AuctionHouse
from src.Blizzard.models.Item.Item import ItemDetails
from src.Blizzard.models.Realm.ConnectedRealm import TheConnectedRealm
from src.Blizzard.models.Realm.MetaData import MetaData
import Constants
import requests
import json


class BlizzardClient(object):
    def __init__(self):
        self.realm = None

    @staticmethod
    async def getAuctionHouse(realmId: int) -> AuctionHouse:
        url = Constants.HOST + "data/wow/connected-realm/" + \
              str(realmId) + \
              "/auctions?namespace=dynamic-us&locale=en_US&access_token=" + \
              Constants.ACCESS_TOKEN

        response = json.loads(requests.request("GET", url).text)
        
        return AuctionHouse(connected_realm=response['connected_realm'],
                            auctions=response['auctions'],
                            commodities=response['commodities'])

    @staticmethod
    def getConnectedRealm(realmId: int) -> TheConnectedRealm:
        url = Constants.HOST + "data/wow/connected-realm/" + \
              str(realmId) + \
              "?namespace=dynamic-us&locale=en_US&access_token=" + \
              Constants.ACCESS_TOKEN

        response = json.loads(requests.request("GET", url).text)

        return TheConnectedRealm(id=response['id'],
                                 has_queue=response['has_queue'],
                                 status=response['status'],
                                 population=response['population'],
                                 realms=response['realms'],
                                 mythic_leaderboards=response['mythic_leaderboards'],
                                 auctions=response['auctions'])

    @staticmethod
    def getConnectedRealmMeta(page: int) -> MetaData:
        url = Constants.HOST + "data/wow/search/connected-realm?namespace=dynamic-us&status.type=UP&" + \
              "orderby=id&_page=1&_page=" + \
              str(page) + "&access_token=" + \
              Constants.ACCESS_TOKEN

        response = json.loads(requests.request("GET", url).text)

        return MetaData(
            page=response['page'],
            pageSize=response['pageSize'],
            maxPageSize=response['maxPageSize'],
            pageCount=response['pageCount'],
            results=response['results'])

    @staticmethod
    async def getItemDetails(itemId: int) -> ItemDetails:
        url = Constants.HOST + "data/wow/item/" + \
              str(itemId) + \
              "?namespace=static-us&locale=en_US&access_token=" + \
              Constants.ACCESS_TOKEN

        response = json.loads(requests.request("GET", url).text)

        return ItemDetails(
            id=response['id'],
            name=response['name'],
            quality=response['quality'],
            level=response['level'],
            required_level=response['required_level'],
            media=response['media'],
            item_class=response['item_class'],
            item_subclass=response['item_subclass'],
            inventory_type=response['inventory_type'],
            max_count=response['max_count'],
            is_equippable=response['is_equippable'],
            is_stackable=response['is_stackable'],
            preview_item=response['preview_item'],
            purchase_quantity=response['purchase_quantity'])
