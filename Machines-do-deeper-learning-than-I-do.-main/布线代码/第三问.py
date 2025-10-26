# (1)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文

def get_width(B,D_0):
    # 初始化参数
    alpha = 1.5 # 坡度 (单位: 度)
    theta = 120 # 换能器的开角 (单位: 度)
    alpha= np.arctan(abs(np.sin(np.radians(B)))*np.tan(np.radians(alpha)))*180/np.pi
    
    print(D_0)
    
    W = D_0 * np.sin(np.radians(theta / 2)) * (
        1 / np.sin(np.radians((180 - theta) / 2 + alpha)) + 1 / np.sin(np.radians((180 - theta) / 2 - alpha)))
    
    print(W)
    return W

angle=np.linspace(0,360,360)
W=[]
for i in angle:
    W.append(get_width(i,150))

print(W)
plt.plot(angle,W)

plt.scatter(90,W[89],color='r')
plt.scatter(270,W[269],color='r')
plt.text(90,W[89], '({}, {})'.format(90,W[89]))
plt.text(270,W[269], '({}, {})'.format(270,W[269]))

angle=np.linspace(0,360,360)
W=[]
for i in angle:
    W.append(get_width(i,149.5))

print(W)
plt.plot(angle,W)

plt.scatter(90,W[89],color='r')
plt.scatter(270,W[269],color='r')
plt.text(90,W[89], '({}, {})'.format(90,W[89]))
plt.text(270,W[269], '({}, {})'.format(270,W[269]))

plt.xlabel("不同角度")
plt.ylabel("覆盖宽度")
plt.show()

# (2)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文

def sin(a):
    return np.sin(np.radians(a))
def cos(a):
    return np.cos(np.radians(a))
def tan(a):
    return np.tan(np.radians(a))

angle=np.linspace(0,360,360)
low=110.2*1852*np.tan(np.radians(1.5))
high=110.2*1852*np.tan(np.radians(1.5))

alpha = 1.5 # 坡度 (单位: 度)
theta = 120 # 换能器的开角 (单位: 度)

n=np.linspace(0.1,9.2,100)
cnt=[]
for i in n:
    x = sin(theta / 2) * cos(alpha) * high / (sin(90 - theta / 2 - alpha) + sin(alpha) * sin(theta / 2))
    ans = []
    print(x)
    A = sin(90 - theta / 2 + alpha)
    B = sin(90 - theta / 2 - alpha)
    C = sin(theta / 2) / A - 1 / tan(alpha)
    D = n * sin(theta / 2) * (1 / A + 1 / B) - sin(theta / 2) / B - 1 / tan(alpha)
    
    while True:
        x = x * C / D
        if x < low:
            break
        ans.append(x)
    
    # print(len(ans))
    cnt.append(len(ans))
    # print(ans[-1])

n=np.array(n)
print(n)
print(cnt)
plt.plot(n,cnt,color='r')
plt.xlabel("不同重复率")
plt.ylabel("测线总数")
plt.show()

# (3)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文

def sin(a):
    return np.sin(np.radians(a))
def cos(a):
    return np.cos(np.radians(a))
def tan(a):
    return np.tan(np.radians(a))
def get_Wleft(D):
    return D*sin(theta/2)/sin(90-theta/2-alpha)

angle=np.linspace(0,360,360)
low=110.2*1852*np.tan(np.radians(1.5))
high=110.2*1852*np.tan(np.radians(1.5))

alpha = 1.5 # 坡度 (单位: 度)
theta = 120 # 换能器的开角 (单位: 度)

n=0.1
cnt=[]
x = sin(theta / 2) * cos(alpha) * high / (sin(90 - theta / 2 - alpha) + sin(alpha) * sin(theta / 2))
x = high - x * tan(alpha)
print(x)
ans = []
ans.append(x)
A = sin(90 - theta / 2 + alpha)
B = sin(90 - theta / 2 - alpha)
C = sin(theta / 2) / A - 1 / tan(alpha)
D = n * sin(theta / 2) * (1 / A + 1 / B) - sin(theta / 2) / B - 1 / tan(alpha)

while True:
    x = x * C / D
    if x < low:
        break
    ans.append(x)

# print(len(ans))
# # print(ans[-1])
index=np.arange(len(ans))
ans=np.array(ans)
dis=[]
for i in range(len(ans)-1):
    dis.append((ans[i]-ans[i+1])/tan(alpha))
for i in range(len(dis)-1):
    dis[i+1]+=dis[i]

# plt.scatter(index,ans,color='g')
# plt.xlabel("测线编号")
# plt.ylabel("水深")
# plt.show()
print(dis)
dis.insert(0,0)
dis=np.array(dis)/1852
