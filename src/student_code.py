import common

def one_train(train_data):
	weights = [0, 0]
	bias = 0
	converge = 100
	count = 0
	while converge > 10 and count < 1000:
		for data in train_data:
			activation = weights[0]*data[0] + weights[1]*data[1] + bias
			if activation >= 0:
				classify = 1
				value = 1
			else:
				classify = -1
				value = 0
			# if it was not predicted right update weights
			if value != data[2]:
				target = data[2]
				if target == 0:
					target = -1
				new_weights = [0, 0]
				new_bias = 0
				new_weights[0] = weights[0] + (target - classify)*data[0]
				new_weights[1] = weights[1] + (target - classify)*data[1]
				new_bias = bias + (target - classify)
				# check convergence
				converge = abs(new_weights[0] - weights[0]) + abs(new_weights[1] - weights[1]) + abs(new_bias - bias)
				# update values
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
	weights, bias = one_train(data_train)
	print(weights)
	results = one_test(weights, bias, data_test)
	return results

def multi_train(train_data):
	weights = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
	converge = 100
	# while it has not converged
	count = 0
	while converge > 10 and count < 100:
		# for each entry in the training data
		for data in train_data:
			# preds are empty, need one for each option
			activations = []
			# print(f"weights: {weights}")
			for weight in weights:
				activations.append(weight[0]*data[0] + weight[1]*data[1])
			# print("ACTIVATIONS")
			# print(activations)
			# find the predicted value
			pred = activations.index(max(activations))
			# if the predicted value is wrong update weights
			if pred != data[2]:
				incorrect_update = [weights[pred][0] - data[0], weights[pred][1] - data[1]]
				correct_update = [weights[int(data[2])][0] + data[0], weights[int(data[2])][1] + data[1]]
				converge = abs(weights[pred][0] - incorrect_update[0]) + abs(weights[pred][1] - incorrect_update[1]) + abs(weights[int(data[2])][0] - correct_update[0]) + abs(weights[int(data[2])][1] - correct_update[1])
				weights[pred][0] = incorrect_update[0]
				weights[pred][1] = incorrect_update[1]
				weights[int(data[2])][0] = correct_update[0]
				weights[int(data[2])][1] = correct_update[1]
		count += 1
	return weights

def multi_test(weights, test_data):
	for data in test_data:
		activations = []
		for weight in weights:
				activations.append(weight[0]*data[0] + weight[1]*data[1])
		# find the predicted value
		data[2] = activations.index(max(activations))
	return test_data

def part_two_classifier(data_train, data_test):
	weights = multi_train(data_train)
	print(weights)
	results = multi_test(weights, data_test)
	return results
