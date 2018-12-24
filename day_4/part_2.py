"""Find the guard that is most frequently asleep on the same minute."""
import re
from collections import Counter, defaultdict

BEGIN_SHIFT = re.compile(
    r"\[(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\]\s+Guard\s+#(\d+)\s+begins shift")
SLEEPS = re.compile(
    r"\[(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\]\s+falls asleep")
AWAKE = re.compile(
    r"\[(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\]\s+wakes up")


def main():
    """Calculate which guard is the most frequently asleep on the same minute."""
    with open("day_4/input.txt") as file:
        events = sorted(file.readlines())

    guard_sleeptimes = defaultdict(Counter)
    guard_id, sleep_time, wakeup_time = None, None, None
    current_max_min, current_guard_id, current_min_count = 0, 0, 0

    for event in iter(events):
        begin_shift = BEGIN_SHIFT.match(event)
        falls_asleep = SLEEPS.match(event)
        wakes_up = AWAKE.match(event)
        if begin_shift is not None:
            _, guard_id = begin_shift.groups()
        elif falls_asleep is not None:
            sleep_time = falls_asleep.group(1)
        elif wakes_up is not None:
            wakeup_time = wakes_up.group(1)
            up_min = int(wakeup_time[-2:])
            sleep_min = int(sleep_time[-2:])

            common_sleeptime = Counter({i: 0 for i in range(00, 61)})
            for time in range(sleep_min, up_min):
                common_sleeptime[time] += 1
            guard_sleeptimes[guard_id] += common_sleeptime
    for g_id, count in guard_sleeptimes.items():
        max_minute, minute_cnt = count.most_common(1).pop()
        if minute_cnt > current_min_count:
            current_min_count = minute_cnt
            current_max_min = max_minute
            current_guard_id = g_id
    answer = int(current_guard_id)*int(current_max_min)
    print(current_guard_id, current_max_min, answer)


if __name__ == "__main__":
    main()
