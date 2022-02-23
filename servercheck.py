config_timeout=3
config_workers=20
inputlist='allservers'
outputdata='data.txt'

from steam import game_servers as gs
import logging
import json, sys
from ast import literal_eval
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(filename=outputdata, encoding='utf-8', format='%(message)s', level=logging.DEBUG)


def check(passed):
    try:	
            status = gs.a2s_players(passed, timeout=config_timeout)
            if(len(status) != 0) :
                info = str(passed) 
                info += str(list(status))
                print(info)
                logging.info(info)
            else :
                print(str(passed[0]) + ":" + str(passed[1]) + " is empty")
    except TimeoutError:
        print(str(passed[0]) + ":" + str(passed[1]) + " timed out")
    except RuntimeError:
        print(str(passed[0]) + ":" + str(passed[1]) + " sent invalid data ")
    return


def main():
    threads= []
    with ThreadPoolExecutor(max_workers=config_workers) as executor:
        with open(inputlist, "r") as serverlist:
            for line in serverlist:
                server_addr = literal_eval(line)
                threads.append(executor.submit(check, server_addr))
                
main()