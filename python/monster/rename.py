import os,sys

path=r'C:\Users\v_vyhzheng\Pictures\11mhw\images'

def rename(path):
	for file in os.listdir(path):
			newName = file.replace("cmn_item00_ori_","it-")
			# newName = 'cl-'+file
			os.rename(os.path.join(path,file), os.path.join(path,newName))
rename(path)
#结束

print("End")

