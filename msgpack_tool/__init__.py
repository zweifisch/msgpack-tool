import sys
from os import path
import json
import msgpack

def get_input():
	if not sys.stdin.isatty():
		f = sys.stdin
	else:
		if len(sys.argv) == 2:
			filename = sys.argv[1]
			if path.exists(filename):
				f = open(filename)
			else:
				print("%s not found" % filename)
				sys.exit(1)
		else:
			return None
	ret = f.read()
	f.close()
	return ret

def main():
	data = get_input()
	if data:
		data = data.strip()
		if (ord(data[0]) in [91, 123]):
			sys.stdout.write(msgpack.dumps(json.loads(data)))
		else:
			sys.stdout.write(json.dumps(msgpack.loads(data), indent=2))
