# -*- coding: UTF-8 -*-

'''

	Problem: Given two strings, check if one string is a permutation of another. 

	Naive Approach: Get all combinations of one string and match with the other string, if it is similar or not.

	Time Complexity: O(n!) where n is the length of the string.

	Better Solution: Store all the characters of a string in a hash-map and keep the count of each character across each key. 
	While parsing through the other string, reduce the count for each character in hash_map. If the final hash_map is empty, both
	the strings are permutation of each other.

	Time Complexity: O(n) where n is the length of string
	Space Complexity: O(n) 

'''


# function to check if two strings are permutation of each other
def check_permutation(s1, s2):

	hash_map = {}

	for i in s1:
		if i not in hash_map:
			hash_map[i] = 1

		else:
			hash_map[i] += 1


	# loop through the second string
	for i in s2:
		# delete the value for each character found in hash_map
		if i in hash_map:
			if hash_map[i] > 1:
				hash_map[i] -= 1

			else:
				del hash_map[i]

		# if any character is not found in hash map, return False
		else:
			return False


	# check if the hash_map is empty
	if len(hash_map) == 0:
		return True
	else:
		return False

# Writing unit-test for the above function
import unittest

class MyTest(unittest.TestCase):

	def test(self):
		self.assertEqual(check_permutation("aabcbaah"), "aabcbaah")
		self.assertEqual(check_permutation("aabcccccaaa"), "a2b1c5a3")

unittest.main()
