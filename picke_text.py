import pickle

class Employee:
    def __init__(self, eno, ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr

    def display(self):
        print('ENO: {}, ENAME: {}, ESAL: {}, EADDR:{}'.format(self.eno,self.ename, self.esal,self.eaddr))

emp = Employee(100,"Tom",4321,"Nashville")

with open('emp.pkl','wb') as f:
    pickle.dump(emp,f)
    print("Pickle compeleted")

with open('emp.pkl',"rb") as f:
    obj=pickle.load(f)
    print('unplckle completed')
    obj.display()
        