# coding=utf-8
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

reload(sys)
sys.setdefaultencoding('utf8')
####################################################
################## Thrust code #####################
####################################################

Motor_name = "EMAX RS1108 - 5200KV"
Propeller_name = "EMAX avan Quad-Blade 2 inch"
Batt = "Batt 2S"
excel_file = 'datasets/StepsTest_2020-05-23_154840.csv'

#Motor_name = "BETA FPV 1105-6000KV"
#Propeller_name = "EMAX avan Quad-Blade 2 inch"
#Batt = "Batt 2S"
#excel_file = 'datasets/StepsTest_2020-05-22_102946.csv'


# Read data from file
data = pd.read_csv(excel_file)

# Create vector X
xmesh = np.linspace(min(data['Motor Electrical Speed (RPM)']), max(data['Motor Electrical Speed (RPM)']), 100)

# Create vector for polyfit
X = data.loc[:, "Motor Electrical Speed (RPM)"].values.reshape(-1, 1)
Y = data.loc[:, "Thrust (gf)"].values.reshape(-1, 1)

# Use poly fit and return polynomial equation
fit = np.polyfit(data['Motor Electrical Speed (RPM)'], data['Thrust (gf)'], 2)
equation = np.poly1d(fit)
print ("{0:.4e}x^2 {1:+.4e}) {2:+.4e}".format(*fit))


fig1 = plt.figure()

ax1 = fig1.add_subplot(111)
ax1.set_title('Thrust vs Motor Speed \n' + Batt+ ', '+ Motor_name + ' and ' + Propeller_name, fontsize=10, fontweight='bold')
ax1.grid(True)
yy=(max(Y)-min(Y))*0.8
color = 'tab:blue'
ax1.text(10000, yy, "f(x) = {0:.4e}x^2 {1:+.4e}x {2:+.4e}".format(*fit), style='italic')
ax1.set_xlabel('Motor Speed (RPM)')
ax1.set_ylabel('Thrust (gf)')
ax1.plot(X, Y, color=color,marker="o", linestyle='None', label='Thrust (gf)')
ax1.plot(xmesh, equation(xmesh), '-r', label='Curve fit')
ax1.legend(loc='best')




####################################################
################## Torque code #####################
####################################################

Column = "Torque (N·m)"


# Create vector X
xmesh = np.linspace(min(data['Motor Electrical Speed (RPM)']), max(data['Motor Electrical Speed (RPM)']), 100)

# Create vector for polyfit
X = data.loc[:, "Motor Electrical Speed (RPM)"].values.reshape(-1, 1)
Y = data.loc[:, Column].values.reshape(-1, 1)

# Use poly fit and return polynomial equation
fit = np.polyfit(data['Motor Electrical Speed (RPM)'], data[Column], 2)
equation = np.poly1d(fit)
print ("{0:.4e}x^2 {1:+.4e}) {2:+.4e}".format(*fit))

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.set_title('Torque vs Motor Speed \n'  + Batt+ ', ' + Motor_name + ' and ' + Propeller_name, fontsize=10, fontweight='bold')


ax2.grid(True)

yy=(max(Y)-min(Y))*0.9
color = 'tab:blue'
ax2.text(10000, yy, "f(x) = {0:.4e}x^2 {1:+.4e}x {2:+.4e}".format(*fit), style='italic')

ax2.set_xlabel('Motor Speed (RPM)')
ax2.set_ylabel(Column)
ax2.plot(X, Y, color=color,marker="o", linestyle='None', label = Column)
ax2.plot(xmesh, equation(xmesh), '-r', label='Curve fit')

ax2.legend(loc='best')


plt.show()

####################################################
################## Torque code #####################
####################################################

Column = "Propeller Mech. Efficiency (gf/W)"


# Create vector X
xmesh = np.linspace(min(data['Motor Electrical Speed (RPM)']), max(data['Motor Electrical Speed (RPM)']), 100)

# Create vector for polyfit
X = data.loc[:, "Motor Electrical Speed (RPM)"].values.reshape(-1, 1)
Y = data.loc[:, Column].values.reshape(-1, 1)

# Use poly fit and return polynomial equation
fit = np.polyfit(data['Motor Electrical Speed (RPM)'], data[Column], 2)
equation = np.poly1d(fit)
print ("{0:.4e}x^2 {1:+.4e}) {2:+.4e}".format(*fit))

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.set_title('Propeller Mech. Efficiency vs Motor Speed \n'  + Batt+ ', ' + Motor_name + ' and ' + Propeller_name, fontsize=10, fontweight='bold')


ax2.grid(True)

yy=min(Y)
color = 'tab:blue'
ax2.text(10000, yy, "f(x) = {0:.4e}x^2 {1:+.4e}x {2:+.4e}".format(*fit), style='italic')

ax2.set_xlabel('Motor Speed (RPM)')
ax2.set_ylabel(Column)
ax2.plot(X, Y, color=color,marker="o", linestyle='None', label = Column)
ax2.plot(xmesh, equation(xmesh), '-r', label='Curve fit')

ax2.legend(loc='best')


plt.show()

####################################################
################## Torque code #####################
####################################################

Column = "Motor Efficiency (%)"


# Create vector X
xmesh = np.linspace(min(data['Motor Electrical Speed (RPM)']), max(data['Motor Electrical Speed (RPM)']), 100)

# Create vector for polyfit
X = data.loc[:, "Motor Electrical Speed (RPM)"].values.reshape(-1, 1)
Y = data.loc[:, Column].values.reshape(-1, 1)

# Use poly fit and return polynomial equation
fit = np.polyfit(data['Motor Electrical Speed (RPM)'], data[Column], 2)
equation = np.poly1d(fit)
print ("{0:.4e}x^2 {1:+.4e}) {2:+.4e}".format(*fit))

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.set_title('Motor Efficiency vs Motor Speed \n'  + Batt+ ', ' + Motor_name + ' and ' + Propeller_name, fontsize=10, fontweight='bold')


ax2.grid(True)

yy=(max(Y)-min(Y))*0.9
color = 'tab:blue'
ax2.text(10000, yy, "f(x) = {0:.4e}x^2 {1:+.4e}x {2:+.4e}".format(*fit), style='italic')

ax2.set_xlabel('Motor Speed (RPM)')
ax2.set_ylabel(Column)
ax2.plot(X, Y, color=color,marker="o", linestyle='None', label = Column)
ax2.plot(xmesh, equation(xmesh), '-r', label='Curve fit')

ax2.legend(loc='best')


plt.show()


#data.plot(kind='scatter',x='Motor Electrical Speed (RPM)',y='Thrust (gf)',color='red')
