import os,sys

path=r'C:\Users\v_vyhzheng\Pictures\14\cloak'
# path=r'C:\Users\v_vyhzheng\Pictures\ite'
path=r'C:\Users\v_vyhzheng\Pictures\14\73'

def rename(path):
	for file in os.listdir(path):
			newName = file.replace("cl","73")
			# newName = file.replace("it-","")
			# newName = 'cl-'+file
			os.rename(os.path.join(path,file), os.path.join(path,newName))
rename(path)
#结束

print("End")

