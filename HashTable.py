class LTS:
    class Record:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
    def __init__(self, cap=1000):
        self.arr = [None] * cap
        self.cap = cap
        self.length = 0
        

    def hashIndex(self, key):
        return hash(key) % self.cap

    def resize(self):
        self.cap *= 2
        tmp = self.arr
        self.arr = [None] * self.cap
        self.length = 0
        for i in tmp:
            if i is not None:
                index = self.hashIndex(i.key)
                while self.arr[index] is not None:
                    index = (index + 1) % self.cap
                self.arr[index] = i
                self.length += 1

    def insert(self, k, v):
        tmp = self.Record(k, v)
        index = self.hashIndex(k)
        while self.arr[index]:
            if self.arr[index].key == k:
                self.arr[index].value = v
                return False
            index = (index + 1) % self.cap
        self.length += 1
        self.arr[index] = tmp
        if self.length >= self.cap * 0.7:
            self.resize()
        return True

    def modify(self, keys, values):
        index = self.hashIndex(keys)
        num_iterations = 0
        while num_iterations < self.cap and self.arr[index] is not None:
            if self.arr[index].key == keys:
                self.arr[index].value = values
                return True
            index = (index + 1) % self.cap
            num_iterations += 1
        return False

    """
        This function removes the key-value 
        pair with the matching key. If no record with matching 
        key exists in the table, the function does nothing and 
        returns False. Otherwise, record with matching 
        key is removed and returns True
     """

    def remove(self, keys):
        index = self.hashIndex(keys)
        itr = 0
        while itr < self.cap and self.arr[index] is not None:
            if self.arr[index].key == keys:
                self.arr[index] = self.dummy
                self.length -= 1
                return True
            index = (index + 1) % self.cap
            itr += 1
        return False

    """
    This function returns the value of the record with the matching
    key. If no reocrd with matching key exists in the table, 
    function returns None
    """

    def search(self, keys):
        index = self.hashIndex(keys)
        flag = False
        while self.arr[index]:
            if self.arr[index].key == keys:
                print('Found [', self.arr[index].value, ']')
                flag = True
                break
            # these index use for loop through the table
            index += 1
            index %= self.cap
            if index == self.hashIndex(keys):
                break
        if flag:
            return self.arr[index].value
        else:
            return None

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.length



class LNTS:
    class Record:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            
    def __init__(self, cap=1000):
        self.cap = cap
        self.arr = [None] * cap
        self.length = 0
        

    def hashIndex(self, k):
        return hash(k) % self.cap

    def resize(self):
        new_table = self.arr
        self.cap *= 2
        self.arr = [None] * self.cap
        for item in new_table:
            if item and item != self.dummy:
                self.insert(item.key, item.value)

    def insert(self, k, v):
        tmp = self.Record(k, v)
        i = self.hashIndex(k)
        while self.arr[i]:
            if self.arr[i].key == k:
                self.arr[i].value = v
                return False
            else:
                i = (i + 1) % self.cap
        if self.arr[i] is None:
            self.arr[i] = tmp
            self.length += 1
        if self.length > self.cap * 0.7:
            self.resize()
        return True

    def modify(self, k, v):
        index = self.hashIndex(k)
        itr = 0
        while self.arr[index] and itr < self.cap:
            if self.arr[index].key == k:
                self.arr[index].value = v
                return True
            index = (index + 1) % self.cap
            itr += 1
        return False

    def remove(self, keys):
        i = self.hashIndex(keys)
        while self.arr[i]:
            if self.arr[i].key == keys:
                self.arr[i] = self.dummy
                self.length -= 1
                return True
            i = (i + 1) % self.cap
        return False

    def search(self, keys):
        index = self.hashIndex(keys)
        while self.arr[index]:
            if self.arr[index].key == keys:
                return self.arr[index].value
            index = (index + 1) % self.cap
        return None

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.length
