'''
Created on 2018年3月24日

@author: LI
'''
import matplotlib.pyplot as plt


#result[maxCycle]={0}

#引用种群的定义
import BeeGroup as BG
import baseFunction
from pylab import *  


class myABC():
    def __init__(self,xNP=40,xlimit=20,xmaxCycle=1000,xD=2,xlb=-100,xub=100):
        '''
        NP 种群的规模，采蜜蜂+观察蜂 
        FoodNumber=NP/2 食物的数量，为采蜜蜂的数量  
        limit 限度，超过这个限度没有更新采蜜蜂变成侦查蜂
        maxCycle 停止条件 
        D=2#函数的参数个数
        lb=-100#函数的下界   
        ub=100#函数的上界 
        '''
        self.NP=xNP
        self.FoodNumber=self.NP/2
        self.limit=xlimit
        self.maxCycle=xmaxCycle
        self.D=xD
        self.lb=xlb
        self.ub=xub
        
    
    def run(self):
        #主函数
        f= open('process.txt','w')#将迭代过程保存至文件中
        
        NectarSource,EmployedBee,OnLooker,BestSource=baseFunction.initilize(self.FoodNumber,self.D,self.lb,self.ub) 
        BestSource=baseFunction.MemorizeBestSource(self.FoodNumber,NectarSource,BestSource)
        process=[]
        
        #主要循环
        gen =0
        while gen<self.maxCycle :
            NectarSource,EmployedBee=baseFunction.sendEmployedBees(self.FoodNumber,self.D,NectarSource,EmployedBee,self.lb,self.ub)
            NectarSource=baseFunction.calculateProbabilities(self.FoodNumber,NectarSource)  
            NectarSource,OnLooker=baseFunction.sendOnlookerBees(self.FoodNumber,self.D,NectarSource,OnLooker,self.lb,self.ub)  
            BestSource=baseFunction.MemorizeBestSource(self.FoodNumber,NectarSource,BestSource) 
            NectarSource=baseFunction.sendScoutBees(self.FoodNumber,self.D,NectarSource,self.lb,self.ub,self.limit)  
            BestSource=baseFunction.MemorizeBestSource(self.FoodNumber,NectarSource,BestSource)
           
            f.write(str(BestSource.trueFit)) 
            f.write('\n')
            process.append(BestSource.trueFit) 
            gen=gen+1
        
        f.close()
        
        mpl.rcParams['font.sans-serif'] = ['SimHei'] #在matplotlib中显示中文
        x=range(1,self.maxCycle+1)
        plt.xlabel('迭代次数')
        plt.ylabel('tureFit')
        plt.plot(x,process)
        plt.show()

item=myABC()
item.run()