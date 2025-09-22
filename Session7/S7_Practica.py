import numpy as np
import matplotlib.pyplot as plt

dt=[i for i in range(200)] #lista
A=[12,20] #lista
f=[0.23,0.35]
theta_i=[0.26,1.45]
x1=A[0]*np.sin(2*np.pi*f[0]*np.array(dt)*0.1+theta_i[0]) #lista
x2=A[1]*np.sin(2*np.pi*f[1]*np.array(dt)*0.1+theta_i[1]) #lista
Xt=np.array(x1)+np.array(x2)

fig , axs = plt.subplots(3,1)
figtitle="Grafico comparativo respecto a X1-X2 y Total"
fig.suptitle(figtitle.upper(),fontdict={'fontweight' : 'bold'})

#axs[0].plot(x1,'bo-')

axs[0].plot(x1,color="#737373d4", marker='o', linestyle='-')
axs[0].set_title("datos para X1")
axs[0].set_ylim(-20,30)
axs[0].grid()
axs[0].set_xticks([])
axs[1].plot(x2,'rx:')
axs[1].set_title("datos para X2")
axs[1].set_ylim(-20,30)
axs[1].grid()

axs[2].plot(dt, Xt,'yo--')
axs[2].set_title("datos para XT")
axs[2].set_ylim(-30,30)
axs[2].grid()
#plt.plot(x1)
#plt.plot(x2)
plt.savefig('AcomplamientoArmonico.pdf',bbox_inches = "tight",
            pad_inches = 0.3,dpi=640,edgecolor="b",facecolor="#dcc8d9d4")