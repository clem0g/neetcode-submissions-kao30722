class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.store = {}
        self.count = {}

    def get(self, key: int) -> int:
        if key in self.store:
            return self.store[key]
            self.count[key] +=1
        else: 
            return -1
        
    def put(self, key: int, value: int) -> None:
        if len(self.store) == self.cap:
            x = min(self.count.items(), key=lambda x:x[1])
            del(self.store[x[0]])
            if key in self.store:
                self.store[key] = value
                self.count[key] +=1
            else:
                self.store[key] = value
                self.count[key] = 1 
        else:
            if key in self.store:
                self.store[key] = value
                self.count[key] +=1
            else:
                self.store[key] = value
                self.count[key] = 1 
            
