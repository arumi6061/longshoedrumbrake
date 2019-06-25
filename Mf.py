#Friction moment exerted on long shoe drum brake
#Addition of coefficient of friction

f=0.35
omega=0.07
r=0.18
c=0.249
Pmax=780e3
sinTheta=1 #In case long shoe drom brake
theta1=math.pi/6
theta2=math.pi/2

Mf=(f*omega*r*Pmax/(4*sinTheta))*((c*(math.cos(2*theta2)-math.cos(2*theta1)))-4*r*(math.cos(theta2)-math.cos(theta1)))
Mf
