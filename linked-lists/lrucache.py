# LRU Cache - design a data structure that follows the constraints of Least Recently Used (LRU) cache

# Design choices: have a hash map that maps a key to a node where the node stores a value, prev, and next
# The node is a part of a linked list, which is in order (most recently used at end and LRU at head)
# To evict, remove head and add curr to end

MAX_SIZE = 5


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class Cache:
    def __init__(self):
        self.cache = {}
        self.head = None
        self.tail = None

    def _remove_node(self, node):
        """Helper to remove a node from the linked list."""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next  # Update head if node is at the front
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev  # Update tail if node is at the end

    def _add_node_to_tail(self, node):
        """Helper to add a node to the tail of the linked list."""
        node.prev = self.tail
        node.next = None
        if self.tail:
            self.tail.next = node
        else:
            self.head = node  # If list was empty, update head
        self.tail = node

    def write(self, key, value):
        # if key exits in cache, replace it and update
        print("writing key:", key)
        if key in self.cache:  # O(1)
            node = self.cache[key]
            node.val = value
            self._remove_node(node)
        else:
            # not in cache, so put it at the end
            if len(self.cache) > MAX_SIZE:
                raise ValueError
            elif len(self.cache) == MAX_SIZE:
                self.evict()
            # create node and add node to the end of linked list
            node = Node(key, value)
            self.cache[key] = node
        self._add_node_to_tail(node)

    # evict
    def evict(self):
        if self.head is None:
            raise IndexError("Cannot evict from an empty cache")
        else:
            self.cache.pop(self.head.key)
            self._remove_node(self.head)

    def read(self, key):
        if key in self.cache:
            self._remove_node(self.cache[key])
            self._add_node_to_tail(self.cache[key])
            return self.cache[key].val
        else:
            print("Key does not exist in cache")
            return None

    def __str__(self):
        curr = self.head
        linked_list = []
        while curr:
            linked_list.append((curr.key, curr.val))
            curr = curr.next
        cache_dict_print = {}
        for key in self.cache:
            cache_dict_print[key] = self.cache[key].val
        return f"cache looks like {cache_dict_print}\nIn-order of LRU position linked list looks like: {linked_list}"


if __name__ == "__main__":
    # Create cache
    cache = Cache()
    # insert key value pairs
    cache.write("key1", 1)
    cache.write("key2", 2)
    cache.write("key3", 3)
    cache.write("key4", 4)
    cache.write("key5", 5)
    print(cache)
    cache.write("key4", 44)
    cache.write("key6", 6)
    print(cache)
    print("reading key2:", cache.read("key2"))
    print("reading key2:", cache.read("key2"))
    print("reading key7:", cache.read("key7"))
    print(cache)
