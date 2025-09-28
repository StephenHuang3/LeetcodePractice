from collections import deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        q = deque()
        q.append(source)
        level = 0
        seen = set()
        bus_seen = set()
        bus_to_station = defaultdict(set)
        station_to_bus = defaultdict(set)

        for i in range(len(routes)):
            bus_to_station[i] = set(routes[i])
            for station in routes[i]:
                station_to_bus[station].add(i)

        # print(bus_to_station)
        # print(station_to_bus)

        while q:
            length = len(q)
            for i in range(length):
                station = q.popleft()
                if station == target:
                    return level
                all_buses = station_to_bus[station]
                for bus in all_buses:
                    if bus in bus_seen:
                        continue
                    bus_seen.add(bus)
                    for go_to_station in bus_to_station[bus]:
                        if go_to_station not in seen:
                            q.append(go_to_station)
                            seen.add(station)
            level += 1

        return -1


# start at station i
# get all buses that go to station i
# get all stops these buses go to and add to queue, check arrived
# level + 1
# for every station in queue,
# get all busses that to this station
# get all stops these buses go to, add to queue, check arrived