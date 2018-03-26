'''
Created on 2018年3月24日

@author: LI
'''
import matplotlib.pyplot as plt
NP=40 #种群的规模，采蜜蜂+观察蜂 
FoodNumber=NP/2#食物的数量，为采蜜蜂的数量  
limit=20#限度，超过这个限度没有更新采蜜蜂变成侦查蜂
maxCycle=10000#停止条件 

D=2#函数的参数个数
lb=-100#函数的下界   
ub=100#函数的上界 

#result[maxCycle]={0}

#引用种群的定义
import BeeGroup as BG

'''
BeeGroup NectarSource[FoodNumber];//蜜源，注意：一切的修改都是针对蜜源而言的  
BeeGroup EmployedBee[FoodNumber];//采蜜蜂  
BeeGroup OnLooker[FoodNumber];//观察蜂  
BeeGroup BestSource;//记录最好蜜源  
'''

import baseFunction
'''
double random(double, double);//产生区间上的随机数  
void initilize();//初始化参数  
double calculationTruefit(BeeGroup);//计算真实的函数值  
double calculationFitness(double);//计算适应值  
void CalculateProbabilities();//计算轮盘赌的概率  
void evalueSource();//评价蜜源  
void sendEmployedBees();  
void sendOnlookerBees();  
void sendScoutBees();  
void MemorizeBestSource(); 
'''

#主函数
f= open('process.txt','w')#将迭代过程保存至文件中

NectarSource,EmployedBee,OnLooker,BestSource=baseFunction.initilize(FoodNumber,D,lb,ub) 
# print(NectarSource[10].getcode())
# print(EmployedBee[10].getcode())
# print(OnLooker[10].getAllinof())
# print(BestSource.getcode())
BestSource=baseFunction.MemorizeBestSource(FoodNumber,NectarSource,BestSource)
process=[]
# print('阶段1')
#主要循环
gen =0
while gen<maxCycle :
    NectarSource,EmployedBee=baseFunction.sendEmployedBees(FoodNumber,D,NectarSource,EmployedBee,lb,ub)
    NectarSource=baseFunction.calculateProbabilities(FoodNumber,NectarSource)  
    NectarSource,OnLooker=baseFunction.sendOnlookerBees(FoodNumber,D,NectarSource,OnLooker,lb,ub)  
    BestSource=baseFunction.MemorizeBestSource(FoodNumber,NectarSource,BestSource) 
    NectarSource=baseFunction.sendScoutBees(FoodNumber,D,NectarSource,lb,ub,limit)  
    BestSource=baseFunction.MemorizeBestSource(FoodNumber,NectarSource,BestSource)
   
    f.write(str(BestSource.trueFit)) 
    f.write('\n')
    process.append(BestSource.trueFit) 
    gen=gen+1

f.close()

from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #在matplotlib中显示中文


x=range(1,maxCycle+1)
plt.xlabel('迭代次数')
plt.ylabel('tureFit')
plt.plot(x,process)
plt.show()
