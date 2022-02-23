from steam import game_servers as gs
import logging
import json, sys

logging.basicConfig(filename='allservers', encoding='utf-8', format='%(message)s', level=logging.DEBUG)


for server_addr in gs.query_master(r'\appid\440', max_servers=sys.maxsize):
	try:	
		logging.info(server_addr)
	except TimeoutError:
		pass
	except RuntimeError:
		pass