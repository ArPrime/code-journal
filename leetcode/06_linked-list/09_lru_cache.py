'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

1 <= capacity <= 3000
At most 2 * 105 calls will be made to get and put.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
'''


class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.head = self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._remove(node)
            self._add_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            new_node = Node(key, value)
            self._add_to_head(new_node)
            self.key_to_node[key] = new_node

            if len(self.key_to_node) > self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.key_to_node[lru.key]

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# from collections import OrderedDict

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = OrderedDict()
    
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         # 移动到末尾表示最近使用
#         self.cache.move_to_end(key)
#         return self.cache[key]
    
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             # 更新并移动到末尾
#             self.cache[key] = value
#             self.cache.move_to_end(key)
#         else:
#             if len(self.cache) >= self.capacity:
#                 # 删除最久未使用的（第一个）
#                 self.cache.popitem(last=False)
#             self.cache[key] = value