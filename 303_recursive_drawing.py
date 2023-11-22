def draw_figure(n):
    if n == 0:
        return
    print("*" * n)     # pre-action
    draw_figure(n-1)   # recursion
    print("#" * n)     # post-action

n = int(input())
draw_figure(n)


# Not with recursion
#
# n = int(input())
# temp_increase = n
# temp_decrease = n
# while temp_decrease > 0:
#     print(temp_decrease * "*")
#     temp_decrease -= 1
#
# temp_num = 1
#
# while not temp_num > temp_increase:
#     print(temp_num * "#")
#     temp_num += 1
