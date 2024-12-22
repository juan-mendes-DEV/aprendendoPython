import time
import threading

def calc_square(numbers):
    print('calculate square numbers ')
    for i in numbers:
        time.sleep(2)
        print('square: {} '.format(str(i * i)))

def calc_cube(numbers):
    print('calculate cube numbers: ')
    for i in numbers:
        time.sleep(2)
        print('cube: {} '.format(str(i * i * i)))

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    t1 = threading.Thread(target=calc_square, args=(arr,))
    t2 = threading.Thread(target=calc_cube, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('main Thread here!!')
    print('successes')