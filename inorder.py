def inorder():
	return self.inorder(root.left) + root + self.inorder(root.right) if root else []
