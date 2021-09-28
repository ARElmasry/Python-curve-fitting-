import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import re



############################
############################
############################
#Define the function here e.g.:
def objective(x=1.0, m=0.01):
	return pow(x,m)
############################
############################
############################
 
class CurveFitClass:
	
	def __init__(self, objective, x_values=[0.0], y_values=[0.0]):
		self.objective=objective ; self.x_values=x_values ; self.y_values=y_values

	def File_open(self):
		while True:
			try:
				file_name=input("Kindly Provide The Name of Data File: ")
				file_handler = open(file_name)
				break
			except IOError:
				print("Could not open file! ")
		with file_handler:
			lines=file_handler.readlines()
			self.x_values=list()
			self.y_values=list()	
			for i in range(len(lines)):		
					temp=lines[i]	
					temp=re.sub('\s+', ' ', lines[i])
					temp=temp.lstrip().rstrip().split(" ")
					self.x_values.append(float(temp[0]))                                       
					self.y_values.append(float(temp[1]))
					i+=1
	
	def curve_fit (self):
		popt, _ = curve_fit(self.objective, self.x_values, self.y_values)
		m = popt
		print('y = x ^ %.5f' % (m))
		plt.scatter(self.x_values, self.y_values)
		x_line = np.arange(min(self.x_values), max(self.x_values),step=0.001 )
		y_line = self.objective(x_line, m)
		plt.plot(x_line, y_line, 'r-')
		plt.ion()

def main():
	fit_obj=CurveFitClass(objective)
	fit_obj.File_open()
	fit_obj.curve_fit()
	
if __name__=="__main__":
	main()
