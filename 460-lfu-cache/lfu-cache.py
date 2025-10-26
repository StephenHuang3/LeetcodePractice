import collections

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2val = {}
        self.key2freq = {}
        self.freq2key = collections.defaultdict(collections.OrderedDict)
        self.minf = 0

    def _promote(self, key: int):
        """Move key from freq f to f+1, fix minf/LRU structures."""
        f = self.key2freq[key]
        # remove from old freq bucket
        self.freq2key[f].pop(key)
        if not self.freq2key[f]:
            del self.freq2key[f]
            if self.minf == f:
                self.minf = f + 1
        # add to new freq bucket
        self.key2freq[key] = f + 1
        self.freq2key[f + 1][key] = None  # value inside OrderedDict is irrelevant

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        self._promote(key)
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.key2val:
            # update value and promote like a get
            self.key2val[key] = value
            self._promote(key)
            return

        # need space?
        if len(self.key2val) == self.cap:
            # evict least-recent among minf bucket
            k_evict, _ = self.freq2key[self.minf].popitem(last=False)
            if not self.freq2key[self.minf]:
                del self.freq2key[self.minf]
            del self.key2val[k_evict]
            del self.key2freq[k_evict]

        # insert new key with freq=1
        self.key2val[key] = value
        self.key2freq[key] = 1
        self.freq2key[1][key] = None
        self.minf = 1
