import stats as st

def get_array_string(input_array):
	output_string = "["
	for val in input_array:
		output_string += str(val)
		output_string += ","
	output_string = output_string[0:len(output_string)-1]
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

def test_covariance(x_array, y_array):
	print("Covariance of " + get_array_string(x_array) + " and " + get_array_string(y_array) + " is " +
			str(st.find_covariance(x_array, y_array)))

def test_pear_corr(x_array, y_array):
	print("Pearson coefficient of correlation for " + get_array_string(x_array) + " and " + 
			get_array_string(y_array) + " is " +
			str(st.find_pearson_correlation_coeff(x_array, y_array)))

def test_rolling_covariance(x_array, y_array, interval):
	print("X array: " + get_array_string(x_array))
	print("Y array: " + get_array_string(y_array))
	print("Rolling " + str(interval) + " value covariance: " +
			get_array_string(st.find_rolling_values(x_array, y_array, interval, st.find_covariance)))

def test_rolling_correlation(x_array, y_array, interval):
	print("X array: " + get_array_string(x_array))
	print("Y array: " + get_array_string(y_array))
	print("Rolling " + str(interval) + " value correlation: " +
			get_array_string(st.find_rolling_values(x_array, y_array, interval, st.find_pearson_correlation_coeff)))


print("\n")

test_average()
print("\n")

test_covariance([1,2,3,4],[4,3,2,1])
test_covariance([1,2,3,4],[1,2,3,4])
test_covariance([3,4,4,3],[2,1,1,2])
test_covariance([1,2],[4,3])
print("\n")

test_pear_corr([1,2,3,4],[4,3,2,1])
test_pear_corr([1,2,3,4],[1,2,3,4])
test_pear_corr([1,2,3,4],[1,2,1,2])
test_pear_corr([1,2,3,4],[1,2,2,1])
test_pear_corr([1,2,3,4],[2,1,1,2])
test_pear_corr([1,2,3,4], [2,4,6,8])
test_pear_corr([1,2,3,4], [2,4,6,9])
print("\n")

test_rolling_covariance([1,2,3,4,4,3,2,1],[4,3,2,1,1,2,3,4], 4)
test_rolling_covariance([1,2,3,4,4,3,2,1], [4,3,2,1,4,3,2,1], 4)
print("\n")

test_rolling_correlation([1,2,3,4,4,3,2,1], [4,3,2,1,1,2,3,4], 4)
test_rolling_correlation([1,2,3,4,4,3,2,1], [4,3,2,1,4,3,2,1], 4)
test_rolling_correlation([1,2,3,4], [4,3,2,1], 2)
test_rolling_correlation([1,2,3,4], [2,4,6,8], 2)
print("\n")

test_array = [1,2,3,4]
print("Average of [1,2,3,4] is " + str(st.find_average(test_array)))

print_array(test_array)
