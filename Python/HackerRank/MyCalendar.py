import calendar

ip = map(int,raw_input().split())
d = calendar.weekday(ip[2],ip[0],ip[1])
print calendar.day_name[d].upper()

