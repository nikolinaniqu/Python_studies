import threading
def calculate_cube(num):
    print("Cube: {}".format(num*num*num))

def calculate_square(num):
    print("Square: {}".format(num*num))

if __name__=="__main__":
    t1= threading.Thread(target=calculate_cube, args=(10,))
    t2=threading.Thread(target=calculate_square, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
