"""
LRU Cache 中 Dummy Head 和 Tail 节点的详细解释
"""

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
    def __repr__(self):
        return f"Node({self.key}, {self.val})"


def demonstrate_without_dummy_nodes():
    """演示不使用 dummy 节点的问题"""
    print("=== 不使用 Dummy 节点的问题 ===")
    
    # 假设我们有一个简单的双向链表，没有 dummy 节点
    # 当链表为空时：head = None, tail = None
    head = None
    tail = None
    
    print("1. 插入第一个节点时需要特殊处理：")
    node1 = Node(1, 100)
    if head is None:  # 特殊情况！
        head = tail = node1
    print(f"   head: {head}, tail: {tail}")
    
    print("\n2. 删除最后一个节点时也需要特殊处理：")
    if head == tail:  # 又是特殊情况！
        head = tail = None
    print(f"   删除后 head: {head}, tail: {tail}")
    
    print("\n这样的代码充满了 if-else 判断，容易出错！")


def demonstrate_with_dummy_nodes():
    """演示使用 dummy 节点的优势"""
    print("\n=== 使用 Dummy 节点的优势 ===")
    
    # 创建 dummy 节点
    dummy_head = Node(0, 0)  # 假的头节点，不存储真实数据
    dummy_tail = Node(0, 0)  # 假的尾节点，不存储真实数据
    
    # 初始状态：dummy_head <-> dummy_tail
    dummy_head.next = dummy_tail
    dummy_tail.prev = dummy_head
    
    print("初始状态：")
    print("dummy_head <-> dummy_tail")
    print(f"dummy_head.next: {dummy_head.next}")
    print(f"dummy_tail.prev: {dummy_tail.prev}")
    
    def add_to_head(node):
        """添加节点到头部（最近使用）"""
        node.prev = dummy_head
        node.next = dummy_head.next
        dummy_head.next.prev = node
        dummy_head.next = node
    
    def remove_node(node):
        """移除指定节点"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def remove_tail():
        """移除尾部节点（最久未使用）"""
        last_node = dummy_tail.prev
        if last_node != dummy_head:  # 确保不是空链表
            remove_node(last_node)
            return last_node
        return None
    
    # 演示操作
    print("\n1. 添加节点 (1,100)：")
    node1 = Node(1, 100)
    add_to_head(node1)
    print("dummy_head <-> (1,100) <-> dummy_tail")
    
    print("\n2. 添加节点 (2,200)：")
    node2 = Node(2, 200)
    add_to_head(node2)
    print("dummy_head <-> (2,200) <-> (1,100) <-> dummy_tail")
    
    print("\n3. 添加节点 (3,300)：")
    node3 = Node(3, 300)
    add_to_head(node3)
    print("dummy_head <-> (3,300) <-> (2,200) <-> (1,100) <-> dummy_tail")
    
    print("\n4. 移除尾部节点（最久未使用）：")
    removed = remove_tail()
    print(f"移除了：{removed}")
    print("dummy_head <-> (3,300) <-> (2,200) <-> dummy_tail")
    
    print("\n5. 访问节点 (2,200)，移动到头部：")
    remove_node(node2)  # 先移除
    add_to_head(node2)  # 再添加到头部
    print("dummy_head <-> (2,200) <-> (3,300) <-> dummy_tail")


def visualize_lru_operations():
    """可视化 LRU 的操作过程"""
    print("\n=== LRU Cache 操作可视化 ===")
    
    class SimpleLRU:
        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = {}
            self.head = Node(0, 0)
            self.tail = Node(0, 0)
            self.head.next = self.tail
            self.tail.prev = self.head
        
        def _add_to_head(self, node):
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
        
        def _remove(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
        
        def _remove_tail(self):
            last = self.tail.prev
            self._remove(last)
            return last
        
        def get(self, key):
            if key in self.cache:
                node = self.cache[key]
                self._remove(node)
                self._add_to_head(node)
                return node.val
            return -1
        
        def put(self, key, value):
            if key in self.cache:
                node = self.cache[key]
                node.val = value
                self._remove(node)
                self._add_to_head(node)
            else:
                new_node = Node(key, value)
                if len(self.cache) >= self.capacity:
                    tail = self._remove_tail()
                    del self.cache[tail.key]
                self.cache[key] = new_node
                self._add_to_head(new_node)
        
        def display(self):
            """显示当前链表状态"""
            result = []
            current = self.head.next
            while current != self.tail:
                result.append(f"({current.key},{current.val})")
                current = current.next
            print(f"HEAD <-> {' <-> '.join(result)} <-> TAIL")
    
    # 演示完整操作
    lru = SimpleLRU(3)
    
    print("创建容量为3的LRU Cache")
    lru.display()
    
    print("\n1. put(1, 100)")
    lru.put(1, 100)
    lru.display()
    
    print("\n2. put(2, 200)")
    lru.put(2, 200)
    lru.display()
    
    print("\n3. put(3, 300)")
    lru.put(3, 300)
    lru.display()
    
    print("\n4. get(1) - 访问key=1，移到最前面")
    print(f"返回值: {lru.get(1)}")
    lru.display()
    
    print("\n5. put(4, 400) - 容量满了，移除最久未使用的")
    lru.put(4, 400)
    lru.display()
    
    print("\n6. get(2) - key=2已被移除")
    print(f"返回值: {lru.get(2)}")


if __name__ == "__main__":
    demonstrate_without_dummy_nodes()
    demonstrate_with_dummy_nodes()
    visualize_lru_operations()