class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def addNode(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._addNode(self.root, data)

    def _addNode(self, node, data):
        if data < node.val:
            if node.left is None:
                node.left = Node(data)
            else:
                self._addNode(node.left, data)
        elif data > node.val:
            if node.right is None:
                node.right = Node(data)
            else:
                self._addNode(node.right, data)

    def buildTreeFromList(self, datas):
        if not datas:
            return
        self.root = Node(datas[0])
        for data in datas[1:]:
            self.addNode(data)

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    def preOrder(self):
        result = []
        self._preOrder(self.root, result)
        return result

    def _preOrder(self, node, result):
        if node:
            result.append(node.val)
            self._preOrder(node.left, result)
            self._preOrder(node.right, result)

    def inOrder(self):
        result = []
        self._inOrder(self.root, result)
        return result

    def _inOrder(self, node, result):
        if node:
            self._inOrder(node.left, result)
            result.append(node.val)
            self._inOrder(node.right, result)

    def postOrder(self):
        result = []
        self._postOrder(self.root, result)
        return result

    def _postOrder(self, node, result):
        if node:
            self._postOrder(node.left, result)
            self._postOrder(node.right, result)
            result.append(node.val)

    def getHeight(self):
        return self._getHeight(self.root)

    def _getHeight(self, node):
        if node is None:
            return -1
        return 1 + max(self._getHeight(node.left), self._getHeight(node.right))

    def getSumLeftChild(self, node):
        return self._sumTree(node.left) if node else 0

    def getSumRightChild(self, node):
        return self._sumTree(node.right) if node else 0

    def _sumTree(self, node):
        if node is None:
            return 0
        return node.val + self._sumTree(node.left) + self._sumTree(node.right)

    def getTilt(self):
        return self._getTilt(self.root)

    def _getTilt(self, node):
        if node is None:
            return 0
        left_sum = self._sumTree(node.left)
        right_sum = self._sumTree(node.right)
        current_tilt = abs(left_sum - right_sum)
        return current_tilt + self._getTilt(node.left) + self._getTilt(node.right)


if __name__ == '__main__':
    bst = BinarySearchTree()

    datas = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]

    bst.buildTreeFromList(datas)

    print('Search 7:', bst.search(7))
    print('Search 12:', bst.search(12))

    print('PreOrder:', bst.preOrder())
    print('InOrder:', bst.inOrder())
    print('PostOrder:', bst.postOrder())
    print('Get height:', bst.getHeight())
    print('Sum of left child tree:', bst.getSumLeftChild(bst.getRoot()))
    print('Sum of right child tree:', bst.getSumRightChild(bst.getRoot()))
    print('Tilt of tree:', int(bst.getTilt()))
