# if you wish to use your sorted list from a1, copy and paste it here
# this is not the best way to do this but the test scripts are not
# designed to pick up an extra file. 

class LinearProbingTS:
    # This is a single record in a chaining hash table.  You can
    # change this in anyway you wish (including not using it at all)
    class Record:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value

    # You cannot change the function prototypes below.  Other than that
    # how you implement the class is your choice (but it must be a hash
    # table that use chaining for collision resolution)

    def __init__(self, cap=32):
        self.arr = [None] * cap
        self.cap = cap
        self.length = 0
        self.dummy = self.Record("Del")

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


def test_remove_and_modify():
    table = LinearProbingTS()
    table.insert("apple", 5)
    table.insert("banana", 7)
    table.insert("orange", 9)

    # Test remove
    result = table.remove("banana")
    print("Remove result: ", result)  # expected output: True
    print("Table length after remove: ", len(table))  # expected output: 2

    # Test modifying an existing key
    result = table.modify("orange", 10)
    print("Modify result: ", result)  # expected output: True
    print("Value of 'orange' key after modify: ", table.search("orange"))  # expected output: 10

    # Test modifying a non-existing key
    result = table.modify("watermelon", 12)
    print("Modify result: ", result)  # expected output: False
    print("Table length after modify: ", len(table))  # expected output: 2


def test_remove_2():
    keys = ["apple", "banana", "strawberry", "mango",
            "orange", "lichee", "peach", "pear",
            "grape", "nectarine", "blackberry", "clementine",
            "apricot", "cantaloupe", "honeydew", "pineapple",
            "blueberry", "coconut", "raspberry", "cherry",
            "lettuce", "mushroom", "carrot", "broccoli",
            "pepper", "onion", "garlic", "shallots",
            "cabbage", "kale", "leeks", "beets",
            "squash", "pumpkin", "potato", "tomato",
            "watercress", "yam", "taro", "okra",
            "cilantros", "parsley", "basil", "sage",
            "thyme", "tumeric", "paprika", "cloves"]

    values = [32, 16, 18, 19, 22, 25, 72, 12,
              11, 33, 51, 43, 23, 71, 5, 13,
              5, 17, 35, 12, 13, 44, 46, 76,
              8, 10, 15, 18, 11, 64, 73, 7,
              18, 15, 22, 73, 41, 56, 54, 36,
              22, 34, 40, 34, 19, 8, 9, 52]

    tables = LinearProbingTS()

    for i in range(0, 48):
        tables.insert(keys[i], values[i])
    if tables.capacity() == 128 and len(tables) == 48:
        print("Intial insertion: passed")
    else:
        print("Not passed")

    total = 48

    # remove every other value, return should be true
    for i in range(0, 48, 2):
        total -= 1
        if tables.remove(keys[i]) == True and len(tables) == total:
            print(f"Removing {keys[i]}: Passed")
        else:
            print(f"Removing {keys[i]}: Failed")
        # perform search and make sure that only those that
        # should be gone are gone, and those that should be there
        # are there
    for i in range(0, 48):
        if i % 2 == 0:
            if tables.search(keys[i]) is None:
                print(f"Search for {keys[i]}: Passed")
            else:
                print(f"Search for {keys[i]}: Failed")
        else:
            if tables.search(keys[i]) == values[i]:
                print(f"Search for {keys[i]}: Passed")
            else:
                print(f"Search for {keys[i]}: Failed")

        # removing records that are not there should result
        # in false return
    for i in range(0, 48, 2):
        print(f"Removing {keys[i]}: Passed" + f"Value {values[i]}")
        if tables.remove(keys[i]) == False and len(tables) == total and tables.capacity() == 128:
            print(f"Removing {keys[i]}: Passed" + f"Value {values[i]}")
        else:
            print(f"Removing {keys[i]}: Failed")

    # ensure that trying to remove records that
    for i in range(0, 48, 2):
        print(f"All Table {keys[i]} + {values[i]}")


def test_LinearProbingTS_capacity():
    # Create a new hash table with initial capacity 8
    table = LinearProbingTS()

    # Check initial capacity
    capacity = table.capacity()
    print("Initial capacity: ", capacity)

    # Insert 5 items into the table
    table.insert("apple", 10)
    table.insert("banana", 20)
    table.insert("cherry", 30)
    table.insert("orange", 40)
    table.insert("pear", 50)

    # Check capacity again
    capacity = table.capacity()
    print("Capacity after inserting 5 items: ", capacity)

    # Insert another 5 items into the table (total of 10)
    table.insert("grape", 60)
    table.insert("kiwi", 70)
    table.insert("mango", 80)
    table.insert("peach", 90)
    table.insert("watermelon", 100)

    # Check capacity again
    capacity = table.capacity()
    print("Capacity after inserting 10 items: ", capacity)

    # Remove an item from the table
    table.remove("banana")

    # Check capacity again
    capacity = table.capacity()
    print("Capacity after removing 1 item: ", capacity)
    table.resize()
    print("Capacity after removing 1 item: ", table.cap)
    print("Before modifying:")
    print("Capacity:", table.capacity())
    print("Number of records:", table.__len__())

    # Call modify() function here

    print("After modifying:")
    print("Capacity:", table.capacity())
    print("Number of records:", table.__len__())


class LinearProbingNoTS:
    # This is a single record in a chaining hash table.  You can
    # change this in anyway you wish (including not using it at all)
    class Record:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value

    # You cannot change the function prototypes below.  Other than that
    # how you implement the class is your choice (but it must be a hash
    # table that use linear probing for collision resolution)

    def __init__(self, cap=32):
        self.cap = cap
        self.arr = [None] * cap
        self.length = 0
        self.dummy = self.Record(-1, -1)

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


def test_remove():
    table = LinearProbingTS()
    keys = [1, 2, 34, 5, 6]
    values = ['a', 'b', 'c', 'd', 'e']
    for i in range(len(keys)):
        table.insert(keys[i], values[i])
    table.remove(34)
    # Check that the slot corresponding to key 34 is marked as "removed"
    if table.arr[table.hashIndex(34)].key == 'Del':
        print("Key 34 was successfully removed")
    else:
        print("Error removed not finish")


if __name__ == "__main__":
    test_remove_and_modify()
    test_remove_2()
    test_LinearProbingTS_capacity()
    test_remove()
