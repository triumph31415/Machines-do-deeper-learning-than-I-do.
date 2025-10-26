import pandas as pd
import numpy as np
def get_width(B):
    # 初始化参数
    D_0 = 120 # 海底坡面角 (单位: m)
    alpha = 1.5 # 坡度 (单位: 度)
    D = D_0 - distances * np.tan(np.radians(alpha)) * np.cos(np.radians(180 - B))
    theta = 120 # 换能器的开角 (单位: 度)
    alpha= np.arctan(abs(np.sin(np.radians(B)))*np.tan(np.radians(alpha)))*180/np.pi
    
    print(D)
    W = D * np.sin(np.radians(theta / 2)) * (
        1 / np.sin(np.radians((180 - theta) / 2 + alpha)) + 1 / np.sin(np.radians((180 - theta) / 2 - alpha)))
    print(W)
    return W

distances = np.array([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1])
distances = distances * 1852
print(distances)

angle=[0,45,90,135,180,225,270,315]
W=[]
for i in angle:
    W.append(get_width(i))

# 将 DataFrame 保存为 Excel 文件
path=r'C:\Users\PC\Desktop\res2.xlsx'
pd.DataFrame(W).to_excel(path, index=False)
