class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUcache:
    def __init__(self, capacity):
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head

    def move2tail(self, key):
        node = self.hashmap[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def put(self, key, value):
        if self.hashmap.get(key):
            self.move2tail(key)
            self.hashmap.get(key).value = value
        else:
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            node = ListNode(key=key, value=value)
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
            self.hashmap[key] = node

    def get(self, key):
        if key in self.hashmap:
            self.move2tail(key)
            return self.hashmap.get(key).value
        else:
            return -1


