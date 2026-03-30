class TimeMap:

    def __init__(self):
        # Using your variables, but making them dictionaries 
        # so each key gets its own list of values and timestamps.
        self.code = {}
        self.time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key is new, create empty lists for it
        if key not in self.code:
            self.code[key] = []
            self.time[key] = []
            
        self.code[key].append(value)
        self.time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist, return empty string
        if key not in self.time:
            return ""
            
        times = self.time[key]
        
        # l and r must be local variables so they reset on every get() call
        l = 0
        r = len(times) - 1

        # Your exact binary search logic
        while l <= r:
            m = (l + r) // 2
            
            if times[m] < timestamp:
                l = m + 1
            elif times[m] > timestamp:
                r = m - 1
            elif times[m] == timestamp:
                # Exact match found
                return self.code[key][m]
        
        # If no exact match is found, 'r' naturally points to the largest 
        # timestamp that is smaller than the requested timestamp.
        if r >= 0:
            return self.code[key][r]
            
        return ""