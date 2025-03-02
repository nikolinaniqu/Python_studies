import threading
class Cube():
    def num(self,kocka1,kocka2):
        self.kocka1=kocka1
        self.kocka2=kocka2
        pass
        
    def calculate_cube(num):
        print("Zapremina kocke je: {}".format(num*num*num))

    def calculate_length(num):
        print("Ukupna duzina ivica kocke je: {}".format(12*num))
    
kocka1=10
kocka2=20

if __name__=="__main__":
    t1= threading.Thread(target=Cube.calculate_cube, args=(kocka1,))
    t2=threading.Thread(target=Cube.calculate_length, args=(kocka1,))

    t2.start()
    t1.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    t1= threading.Thread(target=Cube.calculate_cube, args=(kocka2,))
    t2=threading.Thread(target=Cube.calculate_length, args=(kocka2,))

    t2.start()
    t1.start()

    t1.join()
    t2.join()
