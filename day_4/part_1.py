"""Find the guard that has the most minutes asleep and the time."""
import re
from collections import defaultdict, Counter

# [1518-11-01 00:00] Guard #10 begins shift
BEGIN_SHIFT = re.compile(
    r"\[(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\]\s+Guard\s+#(\d+)\s+begins shift")
SLEEPS = re.compile(
    r"\[(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\]\s+falls asleep")
AWAKE = re.compile(
    r"\[(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\]\s+wakes up")


def main():
    """Calculate the most minute slept by a guard.

    Return the most minutes multiplied by the guard ID.
    """
    with open("day_4/input.txt") as file:
        events = sorted(file.readlines())

    max_sleeptime = Counter()
    guard_sleeptimes = defaultdict(Counter)
    guard_id, sleep_time, wakeup_time, checkin = None, None, None, None

    for event in iter(events):
        begin_shift = BEGIN_SHIFT.match(event)
        falls_asleep = SLEEPS.match(event)
        wakes_up = AWAKE.match(event)
        if begin_shift is not None:
            checkin, guard_id = begin_shift.groups()
        elif falls_asleep is not None:
            sleep_time = falls_asleep.group(1)
        elif wakes_up is not None:
            wakeup_time = wakes_up.group(1)
            up_min = int(wakeup_time[-2:])
            sleep_min = int(sleep_time[-2:])
            max_sleeptime[int(guard_id)] += up_min - sleep_min

            common_sleeptime = Counter({i: 0 for i in range(00, 61)})
            for time in range(sleep_min, up_min):
                common_sleeptime[time] += 1
            guard_sleeptimes[guard_id] += common_sleeptime

    max_guard_id, _ = max_sleeptime.most_common(1).pop()
    most_sleep_min, _ = guard_sleeptimes.get(
        str(max_guard_id)).most_common(1).pop()
    answer = max_guard_id*most_sleep_min
    print(answer)


if __name__ == "__main__":
    main()
