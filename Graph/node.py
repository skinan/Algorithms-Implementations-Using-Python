

class Node:
    def __init__(self, value):
        self.value = value
        self.status = False

    def mark_node(self):
        self.status = True

    def reset_node_status(self):
        self.status = False
