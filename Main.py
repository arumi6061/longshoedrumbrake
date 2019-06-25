#Summary of parameters and equations of long shoe drum brake
import math

#Brake parameters
a=0.34 #Lever length
r=0.18 #Radius of drum brake
c=0.2604 #Distance between pivot point of lever and drum center
f=0.35 #Brake coefficient of friction
w=0.07 #Width of Clucth lining
rpm=450

Pmax=780e3
sinTheta=1 #In case long shoe drom brake
theta1=math.pi/6
theta2=math.pi/2
psi=1.047 # 20 + 40 degree from diagram

#All related equations
Mn=(w*r*c*Pmax/(4*sinTheta))*(2*psi-math.sin(2*theta2)+math.sin(2*theta1))
Mf=(f*w*r*Pmax/(4*sinTheta))*((c*(math.cos(2*theta2)-math.cos(2*theta1)))-4*r*(math.cos(theta2)-math.cos(theta1)))

#Actuating force
Fa=(Mn-Mf)/a # When rotate clockwise
Fa_anti=(Mn+Mf)/a # When rotate clockwise

#Torque and Power
T=f*w*(r**2)*Pmax*(math.cos(theta1)-math.cos(theta2))/sinTheta
P=2*math.pi*rpm*T/60
