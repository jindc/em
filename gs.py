#coding=utf8
import random,math
def gsfunc(mu,sigmaf,x):
            f1= 1/(math.pow(2*math.pi,0.5)*math.pow(sigmaf,0.5))
            f2=math.exp(-1 * math.pow(x-mu,2)/(2*sigmaf))
            ret = f1 * max(f2,0.001)
            #print 'gsfunc',mu,sigmaf,x,f1,f2,ret
            return ret
class gs():
    def run(self,data,loopcnt=10,K=2):
        self.K = K
        datanum=len(data)
        alpha=[1 /float(K)] * K
        sigmaf=[1.0] *K
        mu = [0.0] * K
        print "alpha",alpha
        print 'sigma',sigmaf
        print 'mu',mu

        
        def gamma(j,k):
            return alpha[k] * gsfunc(mu[k],sigmaf[k],data[j])\
                   / sum([ alpha[n]*gsfunc(mu[n],sigmaf[n],data[j]) \
                          for n in range(self.K)])

        for i in range(loopcnt):
            print 'begin loop:',loopcnt
            for k in range(self.K):
                sum1=sum([gamma(j,k) for j in range(datanum) ])
                mu[k]=sum([gamma(j,k)*data[j]  for j in range(datanum)])/sum1
                sigmaf[k]=sum([gamma(j,k)*math.pow(data[j]-mu[k],2)
                               for j in range(datanum)])\
                           /sum1
                alpha[k]=sum1/datanum
            print "alpha",alpha
            print 'sigmaf',sigmaf
            print 'mu',mu
        self.alpha=alpha
        self.sigmaf=sigmaf
        self.mu=mu
        
    def forecast(self,y):        
        return sum( [self.alpha[k] * gsfunc(self.mu[k],self.sigmaf[k],y) \
                    for k in range(self.K)]) 
        
if __name__=='__main__':
    import sys
    data=[-67,-48,6,8,14,16,23,24,28,29,41,49,56,60,75]
    gsins = gs()
    gsins.run(data)
    print gsins.forecast(int(sys.argv[1]))
