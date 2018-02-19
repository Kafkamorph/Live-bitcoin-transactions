#!/usr/bin/env python

from websocket import create_connection
import simplejson as json
from datetime import datetime
import time
from decimal import *

raw = 0

ws = create_connection("ws://ws.blockchain.info/inv")
ws.send('{"op":"unconfirmed_sub"}')
while ( 1 ) :
	result = ws.recv()

	if raw :
		print result

	result = json.loads(result)
	marker = "	*** new transaction ***"
	if 'out' in result['x'] :
		for out in result['x']['out'] :
			a = int( Decimal( result['x']['time'] ))
			b = datetime.fromtimestamp( a )
			c = format( Decimal( out['value'] ) / Decimal(100000000.0))
			if type(out['addr']) == str:
			    print str( b ) + ' ' + out['addr'] + ' got ' + c + marker
			marker = ''

print "Done"
ws.close()
