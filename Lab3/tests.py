import unittest
import algo

class TestFindSuccessor(unittest.TestCase):

    def setUp(self):
        self.root = BinaryTree(10)
        self.root.left = BinaryTree(5, parent=self.root)
        self.root.right = BinaryTree(15, parent=self.root)
        self.root.left.left = BinaryTree(3, parent=self.root.left)
        self.root.left.right = BinaryTree(7, parent=self.root.left)
        self.root.right.right = BinaryTree(20, parent=self.root.right)
        self.root.right.right.left = BinaryTree(12, parent=self.root.right.right)

    def test_successor_of_7(self):
        result = find_successor(self.root, self.root.left.right)
        self.assertEqual(result.value, 10)

    def test_successor_of_15(self):
        result = find_successor(self.root, self.root.right)
        self.assertEqual(result.value, 12)

    def test_no_successor_for_20(self):
        result = find_successor(self.root, self.root.right.right)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
