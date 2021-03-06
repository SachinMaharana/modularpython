def init():
	global _stats
	_stats = {}

def event_occured(event):
	global _stats
	try:
		_stats[event] = _stats[event] + 1
	except KeyError:
		_stats[event] = 1

def get_stats():
	global stats
	return sorted(_stats.items())
