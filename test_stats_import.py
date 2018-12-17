import stats as st

def get_array_string(input_array):
	output_string = "["
	for val in input_array:
		output_string += str(val)
		output_string += ","
	output_string += "]"
	return output_string

def print_array(input_array):
	print(get_array_string(input_array))

def test_average():
	test_array = [2, 6, 9, 10]
	# 2+6+9+10=27, avg is then 6.75

	test_avg = st.find_average(test_array)
	print("Computed average of " + get_array_string(test_array) + ": " + str(test_avg))
	print("Expected average: 6.75")

def test_covariance():
	test_x_array = [1, 2, 3, 4]
	test_y_array = [4, 3, 2, 1]

	print("Covariance of [1,2,3,4] and [4,3,2,1] is " + str(st.find_covariance(test_x_array, test_y_array)))

	test_x_array_2 = [1,2,3,4]
	test_y_array_2 = [1,2,3,4]

	print("Covariance of [1,2,3,4] and [1,2,3,4] is " + str(st.find_covariance(test_x_array_2, test_y_array_2)))

	test_x_array_3 = [3,4,4,3]
	test_y_array_3 = [2,1,1,2]

	print("Covariance of [3,4,4,3] and [2,1,1,2] is " + str(st.find_covariance(test_x_array_3, test_y_array_3)))

	test_x_array_4 = [1,2]
	test_y_array_4 = [4,3]
	print("Covariance of [1,2] and [2,1] is " + str(st.find_covariance(test_x_array_4, test_y_array_4)))

def test_pear_corr():
	test_x_array = [1,2,3,4]
	test_y_array = [4,3,2,1]

	print("Pearson coefficient of correlation for [1,2,3,4] and [4,3,2,1] is "
			+ str(st.find_pearson_correlation_coeff(test_x_array, test_y_array)))

	test_y_array_2 = [1,2,3,4]
	print("Pearson coefficient of correlation for [1,2,3,4] and [1,2,3,4] is "
			+ str(st.find_pearson_correlation_coeff(test_x_array, test_y_array_2)))

	test_y_array_3 = [1,2,1,2]
	print("Pearson coefficient of correlation for [1,2,3,4] and [1,2,1,2] is "
			+ str(st.find_pearson_correlation_coeff(test_x_array, test_y_array_3)))

	test_y_array_4 = [1,2,2,1]
	print("Pearson coefficient of correlation for [1,2,3,4] and [1,2,2,1] is "
			+ str(st.find_pearson_correlation_coeff(test_x_array, test_y_array_4)))

	test_y_array_5 = [2,1,1,2]
	print("Pearson coefficient of correlation for [1,2,3,4] and [2,1,1,2] is "
			+ str(st.find_pearson_correlation_coeff(test_x_array, test_y_array_5)))

def test_rolling_covariance():
	test_x_array = [1,2,3,4,4,3,2,1]
	test_y_array = [4,3,2,1,4,3,2,1]

	rolling_4_covariance = st.find_rolling_values(test_x_array, test_y_array, 4, st.find_covariance)

	print("X array: [1,2,3,4,4,3,2,1]\n")
	print("Y array: [4,3,2,1,1,2,3,4]\n")
	print("Rolling 4 value average: ")
	for i in range(0, len(rolling_4_covariance)):
		print(str(rolling_4_covariance[i]) + " ")

	print("\n")


print("\n")
test_average()
print("\n")
test_covariance()
print("\n")
test_pear_corr()
print("\n")
test_rolling_covariance()
print("\n")

test_array = [1,2,3,4]
print("Average of [1,2,3,4] is " + str(st.find_average(test_array)))

print_array(test_array)
