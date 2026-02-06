class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        c = 0
        last_complete = {}
        time = 1
        while c < len(tasks):
            next_task = tasks[c]
            prev_complete = -space - 1
            if next_task in last_complete:
                prev_complete = last_complete[next_task]
            if time <= prev_complete + space:
                time = prev_complete + space + 1
            last_complete[next_task] = time
            time += 1
            c += 1

        return time - 1