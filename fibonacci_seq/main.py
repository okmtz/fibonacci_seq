import sys
from fibonacci_seq import fib_num

def main(num):
    ans_num = fib_num(num)
    print(ans_num)

if __name__ == '__main__':
    try:
        arg_num = sys.argv[1]
        arg_num = int(arg_num)
    except Exception as e:
        print("please input integer arg")
        sys.exit()

    main(arg_num)