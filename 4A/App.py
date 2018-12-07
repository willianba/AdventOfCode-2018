import fileinput

entries = []
data = {}
result = {}

for line in fileinput.input():
    entries.append(line)
list.sort(entries)

guard_id = 0
sleep_time = 0
wake_time = 0

for entry in entries:
    if "shift" in entry:
        guard_id = int(entry.split("#")[1].split()[0])
        if guard_id not in data:
            data[guard_id] = {}
    elif "falls" in entry:
        sleep_time = int(entry[15:17])
    elif "wakes" in entry:
        date = entry[1:11]
        wake_time = int(entry[15:17])
        if date not in data[guard_id]:
            data[guard_id][date] = []

        for minute in range(sleep_time, wake_time):
            data[guard_id][date].append(minute)

for guard in data:
    if guard not in result:
        result[guard] = {}
    for day in data[guard]:
        for minute in data[guard][day]:
            if minute in result[guard]:
                result[guard][minute] += 1
            else:
                result[guard][minute] = 1

higher_asleep_guard = 0
minutes_asleep = 0
guard_qtt = {}

for guard in result:
    guard_qtt[guard] = len(result[guard])

higher_asleep_guard = max(guard_qtt, key=guard_qtt.get)
minutes_asleep = max(result[higher_asleep_guard], key=lambda x: result[higher_asleep_guard][x])

print(higher_asleep_guard, minutes_asleep)
print(minutes_asleep * higher_asleep_guard)
