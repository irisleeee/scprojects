"""
File: boggle.py
Name: Iris Lee
----------------------------------------
This program runs a boggle game based on the words user entered
"""


# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
PYTHON_LIST = []
DICT = {}  # a dictionary of the defined indexes and values user entered
WORD_LIST = []  # list of the words found
BOGGLE_INDEX = 4  # number of the rows/columns
word_dict = []


def main():
	"""
	This program runs a boggle game based on the words user entered
	"""
	read_dictionary()
	for i in range(BOGGLE_INDEX):
		row = input(str(i + 1) + ' row of letters: ')
		row = row.lower()  # change all letters into lower cases
		if if_illegal(row) is True:
			break
		else:
			for j in range(BOGGLE_INDEX):
				voc_check(i, j, "", [], {})
				word_dict.append((i, j))
				# indexes rule: units digits represent column no., tens digits represent row no.
	# voc_check("", [], [], {})
	print("There are " + str(len(WORD_LIST)) + " words in total.")


def voc_check(x, y, word, find_list, take_out):
	"""
	:param current_w: the word currently checking
	:param temp_index_lst: the indexes of letters that current word contains
	:param temp_tried_index_lst: the list recording the tried first letters in a word
	:param temp_dict: DICT's copy that the keys and values will be removed and add to temp_index_lst and current_w
	:return:
	"""
	global word_dict
	if word in DICT and len(word) >= 4 and word not in WORD_LIST:
		WORD_LIST.append(word)
		voc_check(x, y, word, find_list, take_out)
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				if 4 > i+x >=0:
					if 4 > j+y >= 0:
						x1 = x+i
						y1 = y+j
						if (x1, y1) in word_dict:
							word += word_dict[(x1, y1)]
							if has_prefix(word, find_list) is False:
								take_out[(x1, y1)] = word_dict[(x1, y1)]
								word_dict.pop((x1, y1))
								if has_prefix(word):
									voc_check(x1, y1, word, find_list, take_out)
								word = word[0:-1]
								word_dict[(x1, y1)] = take_out[(x1, y1)]
								take_out.pop((x1, y1))

	# if len(current_w) >= 4 and current_w in PYTHON_LIST and current_w not in WORD_LIST:
	# 	print("Found " + current_w)
	# 	WORD_LIST.append(current_w)
	# 	voc_check(current_w, temp_index_lst, temp_tried_index_lst, temp_dict)
	# else:
	# 	num = [-11, -10, -9, -1, 1, 9, 10, 11]  # deltas of the indexes of surrounding letters
	# 	if len(temp_index_lst) == 0:
	# 		for i in list(DICT.keys()):
	# 			# return to initial status
	# 			current_w = ""
	# 			temp_index_lst.clear()
	# 			temp_dict = DICT.copy()
	# 			# add the first letter
	# 			if i not in temp_tried_index_lst and len(temp_index_lst) == 0:
	# 				temp_tried_index_lst.append(i)
	# 				current_w += DICT[i]
	# 				temp_index_lst.append(i)
	# 				temp_dict.pop(i, temp_dict[i])
	# 				voc_check(current_w, temp_index_lst, temp_tried_index_lst, temp_dict)
	# 	for j in num:
	# 		# Choose
	# 		if len(current_w) > 0 and str(int(temp_index_lst[len(temp_index_lst) - 1]) + j) in list(temp_dict.keys()):
	# 			temp_index_lst.append(str(int(temp_index_lst[len(temp_index_lst) - 1]) + j))
	# 			current_w += DICT.get(temp_index_lst[len(temp_index_lst) - 1], "")
	# 			temp_dict.pop(temp_index_lst[len(temp_index_lst) - 1], temp_dict[temp_index_lst[len(temp_index_lst) - 1]])
	# 		else:
	# 			continue
	# 		# Explore
	# 		if has_prefix(current_w) is True:
	# 			voc_check(current_w, temp_index_lst, temp_tried_index_lst, temp_dict)
	# 		# Un-choose
	# 		temp_dict[temp_index_lst[len(temp_index_lst) - 1]] = current_w[len(current_w) - 1]
	# 		current_w = current_w[:-1]
	# 		temp_index_lst.pop()


def if_illegal(r):
	"""
	check if format of entered row is illegal
	:param r: user entered rows
	:return:
	"""
	count = 0  # counting illegal formats
	if len(r) != 2 * BOGGLE_INDEX - 1:  # row length should be 7 including blanks
		count += 1
	else:
		for i in range(BOGGLE_INDEX - 1):
			if len(r) >= 2 * i + 1 and r[2 * i + 1] != " " and r[2 * i].isalpha():
				count += 1
	if count > 0:
		print('Illegal input')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			PYTHON_LIST.append(line)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for w in PYTHON_LIST:
		if w.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
