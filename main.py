import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


import streamlit as st

st.title('4R Mechanism')




fig = plt.figure()
ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
line, = ax.plot([], [], lw=1)

link,   = plt.plot([], [], 'r-', linewidth=4) #link için oluşturulan grafik parametreleri
joints, = plt.plot([], [],marker='o', ls="" ,markersize=10) #joint için oluşturulan grafik parametreleri


def init():
    line.set_data([], [])
    return line,


L1 = st.number_input('L1')
L2 = st.number_input('L2')
L3 = st.number_input('L3')
L4 = st.number_input('L4')
w2 = st.number_input('w2')
t2 = st.number_input('Theta2 (in degrees')

t2 = (t2*np.pi)/180

bd = np.sqrt(L1**2+L2**2-2*L1*L2*np.cos(t2))
alfa = np.arccos((L3**2+L4**2-bd**2)/(2*L3*L4))
t3 = 2*np.arctan((-L2*np.sin(t2)+L4*np.sin(alfa))/(L1+L3-L2*np.cos(t2)-L4*np.cos(alfa)))
t4 = 2*np.arctan((L2*np.sin(t2)-L3*np.sin(alfa))/(L4-L1+L2*np.cos(t2)-L3*np.cos(alfa)))

jy = L2*((L4*np.sin(t2-t4))+(L1*np.sin(t2)))
jx = L4*((L2*np.sin(t2-t4))+(L1*np.sin(t4)))

j = jy/jx

w4 = j*w2

st.write("theta4 = ", t4)
st.write("w4 = ", w4)

j2y = (L1*L2*np.sin(t4))*((L1*np.cos(t2))+(L4*np.cos(t2-t4))-L2)
j2x = L4*(np.square((L2*np.sin(t2-t4))+(L1*np.sin(t4))))

j2 = j2y/j2x

j4y = (L1*L2*np.sin(t4))*((L1*np.cos(t4))+(L4*np.cos(t2-t4))-L4)
j4x = L4*(np.square((L2*np.sin(t2-t4))+(L1*np.sin(t4))))

j4 = j4y/j4x

alpha4 = (j2 + (j4*j))*w2*w2

st.write("alpha4 = ", alpha4)


def calculate(theta2):

    BD = np.sqrt(L1**2+L2**2-2*L1*L2*np.cos(theta2))
    alfa = np.arccos((L3**2+L4**2-BD**2)/(2*L3*L4))
    theta3 = 2*np.arctan((-L2*np.sin(theta2)+L4*np.sin(alfa))/(L1+L3-L2*np.cos(theta2)-L4*np.cos(alfa)))
    theta4 = 2*np.arctan((L2*np.sin(theta2)-L3*np.sin(alfa))/(L4-L1+L2*np.cos(theta2)-L3*np.cos(alfa)))


    A = [0,0]
    B = [L2*np.cos(theta2),L2*np.sin(theta2)]
    C = [L2*np.cos(theta2)+L3*np.cos(theta3),L2*np.sin(theta2)+L3*np.sin(theta3)]
    D = [L1,0]
    return BD,alfa,theta3,theta4,A,B,C,D


def animate(theta2):
    BD, alfa, theta3, theta4, A, B, C, D = calculate(theta2)
    x = [A[0], B[0], C[0], D[0]]
    y = [A[1], B[1], C[1], D[1]]

    link.set_data(x, y)
    joints.set_data(x, y)


    return link, joints


p=10
anim = animation.FuncAnimation(fig, animate, np.arange(0, 2*np.pi, 0.01) , interval=p,blit=False)





plt.show()


anim.save('file_name.gif', writer='jai')
st.image('file_name.gif')
