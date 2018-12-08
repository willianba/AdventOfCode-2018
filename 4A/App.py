import fileinput
from collections import Counter

entries = []
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
        if guard_id not in result:
            result[guard_id] = []
    elif "falls" in entry:
        sleep_time = int(entry[15:17])
    elif "wakes" in entry:
        date = entry[1:11]
        wake_time = int(entry[15:17])
        for minute in range(sleep_time, wake_time):
            result[guard_id].append(minute)

higher_asleep_guard = max(result, key=lambda x: len(result[x]))
minute_asleep = Counter(result[higher_asleep_guard]).most_common()[0][0]

print(higher_asleep_guard, minute_asleep)
print(higher_asleep_guard * minute_asleep)
