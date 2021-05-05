import sys
from fibonacci_seq import fib_num

def main(num):
    ans_num = fib_num(num)
    print(ans_num)

if __name__ == '__main__':
    main(int(sys.argv[1]))