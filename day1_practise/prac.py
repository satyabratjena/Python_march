
# def calculate_mean(a, b):
#     mean = (a + b) / 2
#     return mean

# def mean():
#     x = float(input("Enter the number: "))
#     y = float(input("Enter the number: "))
#     result = calculate_mean(x, y)
#     print("The mean is:", result)

# mean();

# from datetime import datetime, timedelta

# def is_date_difference_valid(birthDate, joinDate):
#     # parse the input dates as datetime objects
#     date_of_birth = datetime.strptime(birthDate, '%d/%m/%Y')
#     date_of_join = datetime.strptime(joinDate, '%d/%m/%Y')
    
#     age_difference = date_of_join - date_of_birth
    
#     eighteen_years = timedelta(days=18*365)
    
#     return age_difference >= eighteen_years

# def diffDate():
#     birthDate = input("Enter your birthdate: ")
#     joinDate = input("Enter your joining date: ")
#     result = is_date_difference_valid(birthDate, joinDate)
#     print(result)

# diffDate();

