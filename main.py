import arithmetic_arranger

want_to_continue = False

problem_num = 0

problems_list = []

if len(problems_list) > 5:
    print("Error: Too many problems.")
else:
    for _ in range(5):
        problem = input(f"Input the problem #{problem_num + 1} Example - '1 + 1' (only + and -): ")
        if type(problem) == int :
            print("Please enter a valid equation Example - ('1 + 1')")
        else:
            problems_list.append(problem)
            problem_num += 1
        

display_answer = input("Would you like to display the asnwer?(yes, no): ")
if display_answer == "yes":
    display_answer = True
else:
    display_answer = False

first_num_list = []
operators_list = []
second_num_list = []
result_list = []

try: 
    for prob in problems_list:
        first_num, operators, second_num, result = arithmetic_arranger.arithmetic_arranger(numbers=prob, answers=display_answer)
        first_num_list.append(str(first_num))
        operators_list.append(operators)
        second_num_list.append(second_num)
        result_list.append(result)
    print()
except TypeError:
    quit()

for i in range(len(first_num_list)):
    print(f"{first_num_list[i] :>6}", end='    ')
print()

for i in range(len(operators_list)):
    print(f"{operators_list[i]}{second_num_list[i]:>5}", end='    ')
print()

for i in range(len(operators_list)):
    print("------", end='    ')
print()

if result_list != None:
    for i in range(len(result_list)):
        print(f"{result_list[i] :>6}", end='    ')
else:
    pass

print("\n")


       
    


