import pandas as pd
import numpy as np
# 初始化参数
D_0 = 70
theta = 120
alpha = 1.5
d = 200
d = d*np.sin(np.radians(90-theta/2))/np.sin(np.radians(90-alpha*theta/2))

distances = np.array([-800, -600, -400, -200, 0, 200, 400, 600, 800])
D= D_0 - distances * np.tan(np.radians(alpha))

print(D)

w=(np.sin(np.radians(theta/2))*(1/np.sin(np.radians((180-theta)/2+alpha))+1/np.sin(np.radians((180-theta)/2-alpha))))

print(w)
n=1-d/w

print(n)
# 创建 DataFrame 用于存储结果
df = pd.DataFrame({'海水深度/m': distances})

df['覆盖宽度/m'] = D
df['覆盖宽度/m'] = w
df['与相邻一条航迹线的重叠率/m'] = n
# # 转 DataFrame 保存为 Excel 文件
# path= r'C:\Users\PC\Desktop\res1.xlsx'
# df.to_excel(path, index=False)
