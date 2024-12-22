# import time
import multiprocessing

results = []

def calc_square(numbers):
    global results
    for i in numbers:
        print('square: ', str(i * i))
        results.append(i*i)
        print('witnin a result: ' + str(results))

# def calc_cube(numbers):
#     for i in numbers:
#         time.sleep(3)
#         print('cube: ', str(i * i * i))

if __name__ == '__main__':
    arr = [1,2,3,4,5]

    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p1.start()
    p1.join()

    print('result :' +str(results))
    print('sucess')