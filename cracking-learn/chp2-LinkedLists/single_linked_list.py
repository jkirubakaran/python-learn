
class Node(object):
    """docstring for Node."""
    def __init__(self, val):
        super(Node, self).__init__()
        self.val = val
        self.next = None

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)
node1.next = node2 # 12->99
node2.next = node3 # 99->37


print(f'{node1.val}->{node2.val}->{node3.val}')

