import sys
import glx.apphelper
import os
import glx.helper as helper
from glx.community import Community

CONFIG_TEMPLATE = "config_template.toml"
APPNAME = "hyperspeed"
__version__ = "0.6.3"

def main(community_name):
    config_template = os.path.join(os.path.dirname(os.path.abspath(__file__)),CONFIG_TEMPLATE)
    config = helper.load_app_config(community_name,APPNAME,config_template)
    if not config:
        return False
    
    glx.apphelper.appupdate(calc_value,APPNAME,config,"engines",community_name) 

def calc_value(assetlist):
    ecount = len(assetlist)
    multipliers = [0,1,2,2,3,3,3,3,7,7,7,7,7,7,7,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10]
    if ecount > 32:
        return 10
    return multipliers[ecount]

def cli():
    p = glx.apphelper.setup_parser()
    p.add_argument("list",nargs="?", help="list cards with hyperspeed attribute")
    args = p.parse_args()
    community_name = glx.apphelper.process_common_args(args,__version__,APPNAME)

    if args.list:
        # get attribute id
        config = helper.load_app_config(community_name,APPNAME)
        if not config:
            print("Config file missing")
            exit(0)

        if args.collection:
            collection_id = args.collection
        else:
            collection_id = 1
        
        print("Cards with hyperspeed:")
        helper.prettyrow([("id",3,"r"),("val",3,"r")])
        community = Community(community_name)
        hs = sorted(community.collection(collection_id).attribute(config["attribute_id"]).instances(), key=lambda d: d["card_id"])
        for ins in hs:
            card_id = ins["card_id"]
            if ins["interacted_with"]:
                interacted = "*"
            else:
                interacted = "-"
            value = ins["value"]
            helper.prettyrow([(card_id,3,"r"),(value,3,"r")])
            #print(ins)
        exit(0)
    main(community_name)

