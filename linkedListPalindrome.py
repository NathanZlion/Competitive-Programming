def isPalindrome(head):
	# input is a node head in a linked list
	curr = head
	stack = []

	while curr != None:
		stack.append(curr.val)
		curr = curr.next

	i = stack.pop()
	while len(stack) != 0:
		if i != head.val:
			return False
		head = head.next
		i = stack.pop()

	return True
