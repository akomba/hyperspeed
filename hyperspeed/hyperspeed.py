import sys
from glx.apphelper import *

APPNAME = "hyperspeed"
CONFIG_TEMPLATE = { 
    "attribute_id":False,
    "repeat": 10
}
__version__ = "0.1.0"

def main(community_name=None):
    print("calc_value:",calc_value)
    print("APPNAME:",APPNAME)
    print("CONFIG_TEMPLATE:",CONFIG_TEMPLATE)
    print("community_name:",community_name)
    appupdate(calc_value,APPNAME,CONFIG_TEMPLATE,__version__,"engines",community_name) 

def calc_value(ecount):
    multipliers = [0,1,2,2,3,3,3,3,7,7,7,7,7,7,7,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10]
    if ecount > 32:
        return 10
    return multipliers[ecount]

#if __name__ == "__main__":
#    main()
