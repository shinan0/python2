
# coding: utf-8

# In[26]:


def qiuhe(x,y):
    """
    用于求和的函数。
    
    Input:
    x:接收1个实数；
    y:接收1个实数。
    
    Output:
    返回x+y的计算结果
    """
    print(x)
    print(y)
    z = x + y
    return z


# In[27]:


result = qiuhe(1,2) #函数的调用


# In[28]:


qiuhe(y=1,x=2)


# 约瑟夫问题
#  1. 39个人，数到3淘汰，剩余2个；
#  2. 50个人，数到4淘汰，剩余3个；
#  3. 100个人，数到9淘汰，剩余1个；
#  4.3个结果打印输出

# In[33]:


def move(players,step):
    #移动step前的元素到列表末尾
    #将如何step的元素从列表中删除
    num = step - 1
    while num > 0:
        tmp = players.pop(0)
        players.append(tmp)
        num = num - 1
    return players #根据step做了元素的移动



def play(players,step,alive):
    """
    模拟约瑟夫问题的函数。
    
    Input:
    players:参加游戏的人数；
    step;数到step函数的人数淘汰；
    alive:幸存人数，即游戏结束。
    
    Output:
    返回一个列表，列表中元素为幸存者的编号。
    
    """
    
    #生成一个列表，从[1,...,piayers]
    list1=[i for i in range(1,players+1)]
    #进入游戏的循环，每次数到step淘汰，step之前的元素移动到列表末尾
    #游戏结束的条件，列表剩余人数小于alive
    
    while len(list1) > alive:
        
        #移动step前的元素到列表末尾
        #将如何step的元素从列表中删除
#        num = step - 1
 #       while num > 0:
  #          tmp = list1.pop(0)
   #         list1.append(tmp)
    #        num = num - 1
        list1=move(list1, step)
        
        list1.pop(0) #此时的step的元素在列表第一个位置，使用pop(0)从列表中删除
    return list1

players_num=int(input("请输入参与游戏的人数 "))
step_num=int(input("请输入淘汰的数字 "))
alive_num=int(input("请输入幸存的人数 "))

alive_list=play(players_num, step_num, alive_num)
print(alive_list)

