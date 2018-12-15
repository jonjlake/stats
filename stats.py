def find_average(x_array):
	sum = 0
	count = 0
	for val in x_array:
		sum += val
		count += 1
	return sum/count

def find_covariance(x_array, y_array):
	# Milton p.165:
	# E[X] = Sum{all_x}( Sum{all_y}( x*f_xy(x,y) ) )

	# Milton p.167:
	# Cov(X,Y) = E[(X-ux)(Y-uy)]

	sum = 0
	ux = find_average(x_array)
	uy = find_average(y_array)
	count = 0

	# We should test whether the lengths are the same
	for x, y in zip(x_array, y_array):
		sum += (x - ux)*(y - uy)
		count += 1

	return sum/count

def find_variance(x_array, x_array_mean):
	sq_dev_sum = 0
	count = 0
	for val in x_array:
		sq_dev_sum += (val - x_array_mean) ** 2
		count += 1
	
	return sq_dev_sum/count

def find_pearson_correlation_coeff(x_array, y_array):
	# Milton p. 170
	# p_xy = Cov(X, Y) / Sqrt( Var(X) * Var(Y))

	cov = find_covariance(x_array, y_array)
	var_x = find_variance(x_array, find_average(x_array))
	var_y = find_variance(y_array, find_average(y_array))

	return cov / ( (var_x * var_y) ** 0.5)


