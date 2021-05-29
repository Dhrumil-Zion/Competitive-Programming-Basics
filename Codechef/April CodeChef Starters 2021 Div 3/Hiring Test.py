T=int(input())
for _ in range(T):
    final_string = ""
    total_student,no_of_test = map(int,input().split())
    min_completly,min_partially = map(int,input().split())
    for _ in range(total_student):
        string_input = input()
        if string_input.count('F') >=min_completly:
            final_string+='1'
        elif string_input.count('F') >= min_completly-1 and string_input.count('P')>=min_partially:
            final_string+='1'
        else:
            final_string+='0'
    print(final_string)