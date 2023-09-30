def arithmetic_arranger(numbers, answers):
    nums = numbers.split()
    result_list = []
    first_num_list = []
    operators_list = []
    second_num_list = []
    if len(nums) == 1:
        nums = nums[0]
        first_num = nums[0:1]
        operator = nums[1:2]
        second_num = nums[2:3]

        if answers == True:
            result = calculate(first_num, operator, second_num)
            result_list.append(result)
            
    else:
        first_num = nums[0]
        operator = nums[1]      
        second_num = nums[2]
        if answers == True:
            result = calculate(first_num, operator, second_num)

    try:
        if type(int(first_num)) and type(int(second_num)) != int:
            print("Error: Numbers must only contain digits.")
            print(len(first_num), second_num)
            quit()
        elif len(first_num) > 4 or len(second_num) > 4:
            print("Error: Numbers cannot be more than four digits.")
            quit()
        else:
            if answers == True:
                return first_num, operator, second_num, result
            else:
                result = None
                return first_num, operator, second_num, result
    except ValueError or TypeError:
        print("Error: Numbers must only contain digits.")
        quit()


def calculate(first_num, operator, second_num):
    if operator == "+":
        result = int(first_num) + int(second_num)
    elif operator == "-":
        result = int(first_num) - int(second_num)
    else:
        return "Error: Operator must be '+' or '-'."
    
    return result



