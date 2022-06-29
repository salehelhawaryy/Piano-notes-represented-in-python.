import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft


def pianoGenerate(F,f,t,t1,T):
    u1 = np.where(t-t1>=0,1,0)
    u2 = np.where(t-t1-T >= 0,1,0)
    
    x = (np.sin(2*np.pi*F*t)+np.sin(2*np.pi*f*t))*(u1-u2)
    return x


t1 = np.array([0,0.5,0.9,1.4,1.9,2.3,2.7])
T = np.array([0.3,0.2,0.2,0.3,0.2,0.2,0.3])
F =  np.array([130.81,146.83,164.81,174.61,196,220,246.93])
f = np.array([261.63,293.66,329.63,349.23,392,440,493.88])

i=0
x = 0
𝑡 = np. linspace(0 , 3 , 12 * 1024)
for i in range(7):
    x = x+pianoGenerate(F[i],f[i],t,t1[i],T[i])


𝑁 = 3*1024
𝑓 = np. linspace(0 , 512 , int(𝑁/2))

x_f = fft(x)
x_f = 2/N * np.abs(x_f [0:np.int(N/2)])

noise=np. random. randint(0, 512, 2)

xnoised= x +(np.sin(2*noise[0]*np.pi*t)+np.sin(2*noise[1]*np.pi*t))
xn_f=fft(xnoised)
xn_f= 2/N * np.abs(xn_f [0:np.int(N/2)])
maxNat=0;
for i in range (0,len(x_f)):
    if(maxNat<x_f[i]):
        maxNat=x_f[i]

fn1=0
fn2=0
fn1Notfound=True
for i in range(0,len(xn_f)):
    if( (fn1Notfound==True) and  (xn_f[i]>=maxNat) ):
        fn1=f[i]
        fn1Notfound=False
    else:
        if(xn_f[i]>=maxNat):
            fn2=f[i]

xfiltered= xnoised-(np.sin(2*np.int(fn1)*np.pi*t)+np.sin(2*np.int(fn2)*np.pi*t))
xfiltered_f=fft(xfiltered)
xfiltered_f= 2/N * np.abs(xfiltered_f [0:np.int(N/2)])
sd.play(xfiltered, 3 * 1024)

plt.subplot(3,2,1)
plt.plot(t,x)
plt.subplot(3,2,2)
plt.plot(f,x_f)
plt.subplot(3,2,3)
plt.plot(t,xnoised)
plt.subplot(3,2,4)
plt.plot(f,xn_f)
plt.subplot(3,2,5)
plt.plot(t,xfiltered)
plt.subplot(3,2,6)
plt.plot(f,xfiltered_f)