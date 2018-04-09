#!usr/bin/env python
# Defines a "repeat" function that takes 2 argument
def repeat(s, exclaim):
	"""
	Returns the string 's' repeated 3 times
	If exclaim is true, add exclamation marks
	"""
	
	result = s + s + s # can also use "s*3" which is faster (Why ?)
	if exclaim:
		result = result + '!!!'
	return result
	
def main():
	print(repeat('Yay', False))
	print(repeat('Woo Hoo', True))

# Standard boilerplate to call the main() function to begin
if __name__ == '__main__':
	main()
	
