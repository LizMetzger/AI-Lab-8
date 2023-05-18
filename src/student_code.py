import common

def one_train(train_data):
	weights = [0, 0]
	bias = 0
	converge = 100
	count = 0
	while converge > 10 and count < 1000:
		for data in train_data:
			# print(data[2])
			activation = weights[0]*data[0] + weights[1]*data[1] + bias
			# print("ACRIVEATIO")
			# print(activation)
			# classify = 100
			if activation >= 0:
				classify = 1
				value = 1
			else:
				classify = -1
				value = 0

			if value != data[2]:
				target = data[2]
				if target == 0:
					target = -1
				new_weights = [0, 0]
				new_bias = 0
				new_weights[0] = weights[0] + (target - classify)*data[0]
					# print("WHAT", weights[0] + data[2]*data[0])
				new_weights[1] = weights[1] + (target - classify)*data[1]
				new_bias = bias + (target - classify)
				converge = abs(new_weights[0] - weights[0]) + abs(new_weights[1] - weights[1]) + abs(new_bias - bias)
				# print("CONVERGE")
				# print(converge)
				weights = new_weights
				bias = new_bias
		count += 1

	return weights, bias

def one_test(weights, bias, test_data):
	# go through each value and predict 1 or 0
	for i in range(common.constants.TEST_SIZE):
		activation = weights[0]*test_data[i][0] + weights[1]*test_data[i][1] + bias
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
	weights, bias = one_train(data_train)
	# print(weights)
	# 
	# print(data_test)

		# print("COUNT", count)
	
	data_test = one_test(weights, bias, data_test)
	return data_test


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
