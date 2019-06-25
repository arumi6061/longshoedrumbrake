#Normal moment exerted on long shoe drum brake
#Change variable below to find Mn
w=0.07
r=0.18
c=0.249
Pmax=780e3
sinTheta=1 #In case long shoe drom brake
theta1=math.pi/6
theta2=math.pi/2
psi=1.047 # 20 + 40 degree from diagram

Mn=(w*r*c*Pmax/(4*sinTheta))*(2*psi-math.sin(2*theta2)+math.sin(2*theta1))
Mn
