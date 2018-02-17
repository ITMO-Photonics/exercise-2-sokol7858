import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5.,5,100)
f=np.sqrt(np.abs(x))*np.sin(x**2)
fig, fx=plt.subplots()
fx.plot(x,f,color='black')
plt.show()
