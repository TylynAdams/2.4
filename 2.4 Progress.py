#Mtech progress

# def main():
# #     unit = eval(input('How many units have done? '))
# #     assignments = eval(input('How many assignments have you done in your unfinished units? '))
# #     total = (unit * 5) + assignments
# #
# #     print(total)
# #
# #
# # main()

# def main():
#     unit = eval(input('How many units have done? '))
#     assignments = eval(input('How many assignments have you done in your unfinished units? '))
#     days = float(input('How many classes have you been to? '))
#     total = ((unit * 5) + assignments)(0.1 * days)
#
#     print(total)


# main()

def main():
    unit = eval(input('How many units have done? '))
    assignments = eval(input('How many assignments have you done in your unfinished units? '))
    total = ((unit * 5) + assignments) * (.1) * 100

    print('You are at', total, '%')


main()

