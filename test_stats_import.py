import stats as st

def test_average():
	test_array = [2, 6, 9, 10]
	# 2+6+9+10=27, avg is then 6.75

	test_avg = st.find_average(test_array)
	print("Computed average: " + str(test_avg))
	print("Expected average: 6.75")

def test_covariance():
	test_x_array = [1, 2, 3, 4]
	test_y_array = [4, 3, 2, 1]

	print("Covariance of [1,2,3,4] and [4,3,2,1] is " + str(st.find_covariance(test_x_array, test_y_array)))

	test_x_array_2 = [1,2,3,4]
	test_y_array_2 = [1,2,3,4]

	print("Covariance of [1,2,3,4] and [1,2,3,4] is " + str(st.find_covariance(test_x_array_2, test_y_array_2)))

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


test_average()
test_covariance()
test_pear_corr()

test_array = [1,2,3,4]
print("Average of [1,2,3,4] is " + str(st.find_average(test_array)))
