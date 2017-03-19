grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
# Function to print the grades
def print_grades(grades):
    for grade in grades:
        print grade
print_grades(grades)
# Function to get the sum of the grades
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total
print grades_sum(grades)
# Function to get the average of the grades
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average
print grades_average(grades)
# Function to get the variance of the grades
def grades_variance(scores):
    average=grades_average(scores)
    variance=0
    for score in scores:
        variance+=(average-score)**2
    result=variance/len(scores)
    return result
print grades_variance(grades)
 # Function to get the standard deviation of the grades
def grades_std_deviation(variance):
    return variance**0.5
variance=grades_variance(grades)
print grades_std_deviation(variance)