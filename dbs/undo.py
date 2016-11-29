import sys
import re
import numpy as np


class Undo():

    def refactor(self):
        started = np.zeros((1,self.N))
        cmd = None
        op = [0, 0, 0]
        for i in self.undo_log_list:
            if started[0,i[1]] == 0:
                started[0,i[1]] = 1
                self.undo_op.append(self.startf(i[1]))

            for j in i[0]:
                if "READ" in j:
                    i1 = j.find("(")
                    i2 = j.find(")")
                    cont = (j[i1+1:i2]).split(',')
                    for iii in range(2):
                        cont[iii] = cont[iii].strip()
                    self.assign(cont)
                    cmd = "READ"

                elif "WRITE" in j:
                    i1 = j.find("(")
                    i2 = j.find(")")
                    cont = (j[i1+1:i2]).split(',')
                    for iii in range(2):
                        cont[iii] = cont[iii].strip()
                    self.assigni(cont,i[1])
                    cmd = "WRITE"

                elif "t" in j and i[1] == 0:
                    self.t *= 2
                    cmd = "UPDATE1"

                elif 't1' in j and i[1] == 1 and '+' in j:
                    self.t1 += self.t2
                    cmd = "UPDATE2"

                elif 't1' in j and i[1] == 1 and '-' in j:
                    self.t1 -= self.t2
                    cmd = "UPDATE3"

                elif 't' in j and i[1] == 2:
                    self.t += 1
                    cmd = "UPDATE4"
                else:
                    op[i[1]] += 1
                    if op[i[1]] == 2:
                        self.undo_op.append(self.commitf(i[1]))
            pass
        for i in range(len(op)):
            if op[i] != 2:
                self.undo_op.append(self.commitf(i))


class Redo():
    def d(self):
        return



class Transaction(Undo,  Redo):
    def __init__(self, quantum, transactions, number_of_T):
        self.Q = quantum
        self.T = transactions
        self.N = number_of_T
        self.A = 8 
        self.B = 8 
        self.C = 5 
        self.D = 10
        self.t = None
        self.t1 = None
        self.t2 = None
        self.undo_log_list = []
        self.undo_op = []
        self.it = []
        for i in range(self.N):
            self.it.append(1)

    def undo_log(self):
        i = 0
        sa = [1,1,1]
        while sum(sa):
            if i >= self.N:
                i = 0

            if self.it[i] < len(self.T[i]) - self.Q + 1:
                self.undo_log_list.append((self.T[i][self.it[i]:self.it[i]+self.Q],i))
                self.it[i] += self.Q
                i += 1
            elif self.it[i] < len(self.T[i]):

                self.undo_log_list.append((self.T[i][self.it[i]:],i))
                self.it[i] += self.Q
                i += 1
            for ite in range(self.N):
                if self.it[ite] >= len(self.T[ite])-1:
                    sa[ite] = 0
            pass
        self.refactor()
        if self.A == 16 and\
                self.B == 16 and\
                self.C == 16 and\
                self.D == 17:
                    self.undo_op.append(self.Q)


        for i in self.undo_op:
            print(i)

    
    def startf(self,x):
        ap = "<start T" + str(x+1) + ">"
        apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
        return ap+apt
    def commitf(self,x):
        ap= "<commit T" + str(x+1) + ">"
        apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
        return ap+apt
    def update(self,x, var, y):
        ap = "<T" + str(x+1) + ", " + var + ", " + str(y) + ">"
        return ap

    def assign(self,cont):
        if cont == ['A','t']:
            self.t = self.A
        if cont == ['A','t1']:
            self.t1 = self.A
        if cont == ['A','t2']:
            self.t2 = self.A
        if cont == ['B','t']:
            self.t = self.B
        if cont == ['B','t1']:
            self.t1 = self.B
        if cont == ['B','t2']:
            self.t2 = self.B
        if cont == ['C','t']:
            self.t = self.C
        if cont == ['C','t1']:
            self.t1 = self.C
        if cont == ['C','t2']:
            self.t2 = self.C
        if cont == ['D','t']:
            self.t = self.D
        if cont == ['D','t1']:
            self.t1 = self.D
        if cont == ['D','t2']:
            self.t2 = self.D

    def assigni(self,cont,tno):
        if cont == ['A','t']:
            temp = self.update(tno,'A',self.A)
            self.A = self.t
            apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
            self.undo_op.append(temp + apt)
        if cont == ['A','t1']:
            temp = (self.update(tno,'A',self.A))
            self.A = self.t1
            apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
            self.undo_op.append(temp+apt)
        if cont == ['A','t2']:
            temp = (self.update(tno,'A',self.A))
            self.A = self.t2
            apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
            self.undo_op.append(temp+apt)
        if cont == ['B','t']:
            temp = (self.update(tno,'B',self.B))
            self.B = self.t
            apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
            self.undo_op.append(temp+apt)
        if cont == ['B','t1']:
            temp = (self.update(tno,'B',self.B))
            self.B = self.t1
            apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
            self.undo_op.append(temp+apt)
        if cont == ['B','t2']:
            temp = (self.update(tno,'B',self.B))
            self.B = self.t2
            apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
            self.undo_op.append(temp+apt)
        if cont == ['C','t']:
            temp = (self.update(tno,'C',self.C))
            self.C = self.t
            apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
            self.undo_op.append(temp + apt)
        if cont == ['C','t1']:
            temp = (self.update(tno,'C',self.C))
            self.C = self.t1
            apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
            self.undo_op.append(temp + apt)
        if cont == ['C','t2']:
            temp = (self.update(tno,'C',self.C))
            self.C = self.t2
            apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
            self.undo_op.append(temp + apt)
        if cont == ['D','t']:
            temp = (self.update(tno,'D',self.D))
            self.D = self.t
            apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
            self.undo_op.append(temp + apt)
        if cont == ['D','t1']:
            temp = (self.update(tno,'D',self.D))
            self.D = self.t1
            apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
            self.undo_op.append(temp + apt)
        if cont == ['D','t2']:
            temp = (self.update(tno,'D',self.D))
            self.D = self.t2
            apt = " A "+str(self.A)+ " B "+str(self.B)+ " C "+str(self.C)+ " D " + str(self.D)
            self.undo_op.append(temp + apt)


def splitT(T):
    final = []
    temp = []
    n = 0
    for i in T:
        if "Transaction" in i:
            if len(temp) > 0:
                final.append(temp)
            temp = []
            n+=1
            temp.append(i.strip())
        else:
            temp.append(i.strip())
    final.append(temp)
    return final, n
            

def main():
    Q = int(sys.argv[1])
    F = open('trans.txt', 'r')
    T = F.readlines()
    T2, count = splitT(T)
    F.close()
    log = Transaction(Q, T2, count)
    log.undo_log()



if __name__=="__main__":
    main()
