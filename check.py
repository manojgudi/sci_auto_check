import os
import subprocess

os.getcwd()

'''
def append_exit(absolute_file):
	file_obj = open(absolute_file,'r+w')
	content = file_obj.read()
	content += '\n exit'
	file_obj.close()
'''

for roots, dirs, files in os.walk('/media/d2c1960d-a6c5-4a50-a642-1cd33212cde0/uploads'):
	for scifile in files:
		if (scifile.find('.sci') != -1) or (scifile.find('.sce') !=-1 ):
			#print(roots+'/'+scifile)
			fullfile = roots+'/'+scifile
			print fullfile
			list(fullfile)
			subprocess.call(['./yelp', fullfile])
			#append_exit(fullfile)

