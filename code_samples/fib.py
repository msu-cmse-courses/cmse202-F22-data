# fib.py
#
# Routine to calculate the first N Fibonacci numbers, where
#   F_n = F_{n-1} + F_{n-2}, and the first two numbers are 0,1.
#
# Note: if you're not familiar with the equation above,
# try copying and pasting it here: http://latex2png.com/
#
# The sequence *should* be: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#
# It is currently broken, fix it!

def get_new_high(low_num, high_num):
    return low_num - high_num

def main():

    low_num = 0
    high_num = 1

    print(low_num)

    for i in range(10):
        print(high_num)

        new_high_num = get_new_high(low_num, high_num)
        low_num = high_num
        high_num = new_high_num


if __name__== "__main__":
    main()
