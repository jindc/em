#coding=utf8
import sys,math
class em():
    def run(self,data,loopcnt=2):
        print data
        pi=0.4
        p=0.6
        q=0.7
        datanum=float(len(data))

        def cpi(j):
            tmp1 = pi*math.pow(p,data[j])*math.pow(1-p,1-data[j])
            tmp2 = (1-pi)*math.pow(q,data[j])*math.pow(1-q,1-data[j])
            return tmp1/(tmp1+tmp2)
            
        for i in range(loopcnt):
            pi = 1/datanum *\
                 sum([ cpi(j)for j in range(int(datanum))])
            p = sum( [cpi(j)*data[j] for j in range(int(datanum)) ]) /(pi * datanum)
            q = sum( [ (1-cpi(j))*data[j] for j in range(int(datanum)) ] )/(datanum*(1-pi))
            print i,pi ,p, q
        self.pi =pi
        self.p = p
        self.q = q

if __name__=='__main__':
    data=[1,1,0,1,0,0,1,0,1,1]
    emi = em()
    emi.run(data)
    print emi.pi,emi.p,emi.q
