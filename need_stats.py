import stats

stats.init()
stats.event_occured('meal Eaten')
stats.event_occured("meal Eaten")
stats.event_occured("diet Eaten")
stats.event_occured("diet Eaten")
stats.event_occured("snack Eaten")
stats.event_occured("snake Eaten")
stats.event_occured("snake Eaten")
stats.event_occured("snake Eaten")
stats.event_occured("snack Eaten")
stats.event_occured("meal Eaten")

for event, num in stats.get_stats():
	print("{} occured {} times".format(event, num))