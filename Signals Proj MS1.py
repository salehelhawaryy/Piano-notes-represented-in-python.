#from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd





N = 3*1024
frequency_axis = np. linspace(0 , 512 , int(𝑁/2))

f=np.array([440,493.88,493.88,493.88,523.25])
Start=np.array([0,0.6,1.25,2,2.5])
duration=np.array([0.5,0.4,0.35,0.3,0.5])
t=np.linspace(0, 3,(3*1024))
xf=0

for i in range(0,5,1):
    u1=np.where(t>=Start[i],1,0)
    u2=np.where(t>=duration[i]+Start[i],1,0)
    xf+=np.sin(f[i]*t*2*np.pi)*(u1-u2)

#x_f = fft(xf)
#x_f = 2/N * np.abs(x_f [0:np.int(N/2)])


noise=np. random. randint(0, 512, 2)

xnoised= xf +(np.sin(2*noise[0]*np.pi*t)+np.sin(2*noise[1]*np.pi*t))
#xn_f=fft(xnoised)
#xn_f= 2/N * np.abs(xn_f [0:np.int(N/2)])
maxNat=0;
#for i in range (0,len(x_f)):
    #if(maxNat<x_f[i]):
       # maxNat=frequency_axis[i]

fn1=0
fn2=0
maxN=0
fn1Notfound=True
#for i in range(0,len(frequency_axis)):
   # if( fn1Notfound==True &  xn_f[i]>maxNat ):
     #   fn1=frequency_axis[i]
     #   fn1Notfound=False
  # else:
       # if(xn_f[i]>maxNat):
         #   fn2=frequency_axis[i]


xfiltered= xnoised-(np.sin(2*fn1*np.pi*t)+np.sin(2*fn2*np.pi*t))

sd.play(xf)
#plt.Subplot(2,2)
#plt.plot()




plt.plot(t,xf)

sd.play(xf,(3*1024))