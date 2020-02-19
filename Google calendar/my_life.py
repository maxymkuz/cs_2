from icalendar import Calendar, Event

g = open('maxymkuz@gmail.com.ics', 'rb')
gcal = Calendar.from_ical(g.read())
lifetime_dict = {}
print(gcal)

for component in gcal.walk():
    if component.name == "VEVENT":
        name = component.get('summary')
        date = component.get('dtstart')
        print(date.dt, name)
        if name not in lifetime_dict:
            lifetime_dict[name] = [date.dt]
        else:
            lifetime_dict[name].append(date.dt)
        # print(component.get('DTSTART').dt)
        # print(component.get('dtstamp'))
        # print(component.get('CREATED').dt)
g.close()
print(lifetime_dict)
# with open("maxymkuz@gmail.com.ics", 'r', encoding='utf-8') as file:
#     print(c)
#     dic = {}
#     new_event = False
#     for line in file:
#         line = line.strip()
#         if line.startswith("BEGIN"):
#             new_event = False
#             continue
#         if line.startswith("DTSTART;VALUE=DATE"):
#             line = line.split(":")
#             year = int(line[1][:4])
#             month = int(line[1][4:6])
#             day = int(line[1][6:])
#             # print(year, month, day)
#         elif line.startswith("SUMMARY:"):
#             line = line.split(":")
#             # print(line[1])
#         # print(line)
