import common

def one_train(train_data):
	# initialize weights (x, y, bias)
	weights = [0,0,0]

	for i in range(len(train_data)):
		activation = weights[0]*train_data[i][0] + weights[1]*train_data[i][1]# + weights[2]
		classify = 0
		# classify based on the activation
		if activation >= 0:
			classify = 1
		else:
			classify = -1
		compare = classify
		if classify == -1:
			compare = 0
		# if classify doesn't match that in train, update weights
		if compare != train_data[i][2]:
			# # if classify is 1 add
			# if classify == 1:
			weights = [weights[0]+(train_data[i][2] - classify)*train_data[i][0], weights[1]+(train_data[i][2] - classify)*train_data[i][1]]#, weights[2] + (1 - classify)]
			# else subtract
			# else:
			# 	weights = [weights[0]-train_data[i][0], weights[1]-train_data[i][1], 1]

	return weights

def one_test(weights, test_data):
	# go through each value and predict 1 or 0
	for i in range(len(test_data)):
		activation = weights[0]*test_data[i][0] + weights[1]*test_data[i][1] #+ weights[2]
		if activation >= 0:
			test_data[i][2] = 1
		else:
			test_data[i][2] = 0
	return test_data

def part_one_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 1
	weights = one_train(data_train)
	print(weights)
	data_test = one_test(weights, data_test)
	return


def part_two_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8
	return
