import sys
import glx.helper as helper
from glx.collection import Collection
from glx.api.mothership import MothershipApi
from glx.api.community import CommunityApi
import json

APPNAME = "hyperspeed"
__version__ = "0.0.2"

def main():
    if "--version" in sys.argv[1:]:
        print(__version__)
        exit(0)

    config_template = { 
        "hyperspeed_id":False,
    }
    config = helper.load_or_create_app_config(APPNAME,config_template)
    mapi = MothershipApi()
    engines = mapi.get_asset_owners("engines")
    collection = Collection(config["community_name"],config["collection_id"])

    mcount = 0
    attr_to_remove = []
    cards = collection.cards()
    for card in cards:
        if card.data("owner").lower() in engines:
            mcount += 1
            ecount = len(engines[card.data("owner").lower()]) # the number of engines this card currently has
            value = calc_value(ecount)
            print("HS:",str(card.id),ecount,value)
            card.add_attribute(config["hyperspeed_id"],value)
        else:
            attr_to_remove.append(card.id)        

    if len(attr_to_remove) > 0:
        print("without hyperspeed:",len(attr_to_remove))
        capi = CommunityApi(config["community_name"])
        capi.remove_attribute_from_cards(config["collection_id"],config["hyperspeed_id"],attr_to_remove)

    print("cards with engines:",mcount)
    print("member count:",len(cards))

def calc_value(ecount):
    multipliers = [0,1,2,2,3,3,3,3,7,7,7,7,7,7,7,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10]
    if ecount > 32:
        return 10
    return multipliers[ecount]

if __name__ == "__main__":
    main()
