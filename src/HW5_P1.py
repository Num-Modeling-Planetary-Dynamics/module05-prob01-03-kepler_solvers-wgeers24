import numpy as np
M=5*(np.pi)/180
E=[M]
e=0.100
while True:
    Enew=M+e*np.sin(E[-1])
    E.append(Enew)
    if np.abs(E[-1]-E[-2])<0.000001*(np.pi/180):
        break
with open ("../data/module05-prob01-output.csv", "w") as f:
    for Eval in E:
        f.write(f"{Eval}\n")
        print(Eval)
    
