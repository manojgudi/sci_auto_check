import os
import subprocess
import re


def list2str(list_data):
	formatted_string = ""
	for i in list_data:
		formatted_string = formatted_string + i + "\n"
	return formatted_string

def rm_comments(content):
	list_data = content.splitlines()
	content_void_comments = []
	for i in list_data:
		if i.count("//") != 0:
			i = i.split("//")[0]
		content_void_comments.append(i)
	return list2str(content_void_comments)		

# func_name is raw with "("
def isArray(func_name, content):
	func_name = func_name.strip("(")
	
	# Finds =>  'name('  'name ' 'name'
	all_func_invoked = re.findall(func_name+'[ =\(]', content)
	count = len(all_func_invoked)
	for func_invoked in all_func_invoked:
		if func_invoked.find("(") == -1:
			count -= 1
		else:
			pass
	
	# Yes, the func_name is actually an array
	if count != len(all_func_invoked):
	#	print "FUNCNAME" + func_name
		return True

	else:
		return False

### Beautiful Code, dont Touch ###
def extract_func(abs_file):
	file_obj = open(abs_file, 'r')
	file_content = rm_comments(file_obj.read())
	list_of_func = re.findall("[\w]+\(", file_content)
	
	# Function to remove false positive loop keywords like for/while and array declarations
	def rm_loops(list_of_func, content):
		proper_func_list = []
		elementary_loops = ['for','if','while']
		for func in list_of_func:
			if ((func not in elementary_loops) and (not(isArray(func,content)))): # Replace last condition by array condition
				func = func.strip("(")
				proper_func_list.append(func)

		return proper_func_list
	
	# If no functions are used
	if list_of_func == []:
		return 0
	# set removes the duplicate elements in list
	list_of_func = list(set(rm_loops(list_of_func, file_content)))
	return list_of_func


def inFuncList(func_name, func_list_file):
	# Code To open func_list_file with first letter of func_name
	try:
		file_obj = open(func_list_file,'r')
		func_list = file_obj.read().split('\n')
		file_obj.close()
		
		if func_list.count(func_name) == 1:
			return True
		else:
			return False
	except:
		# If no open(func_list_file) throws error like in case of 1.txt
		return False



# Is the func_name found in func_list_file of 5.3.3 version
def isCompatible(func_name):
	
	# Check for scilab 5.3.3 => base version
	# Code To open func_list_file with first letter of func_name
	func_list_file = 'sci_five_three_three/'+func_name[0].lower() + '.txt'

	if inFuncList(func_name, func_list_file):
		# Check For other versions
		func_list_file = func_name[0].lower()+'.txt'
		if inFuncList(func_name, func_list_file):
			return 0
		else:
			# Non-compatible Function
			return 1
	else:
		# func_name is either User Function or False Positive
		return -1
	

# MAIN LOOP FOR TRAVERSING
#path='/media/d2c1960d-a6c5-4a50-a642-1cd33212cde0/uploads/51/CH12/EX12.2/12_2data.sci'
#path='/media/d2c1960d-a6c5-4a50-a642-1cd33212cde0/uploads/45/CH7/EX7.4/'
path='/media/d2c1960d-a6c5-4a50-a642-1cd33212cde0/uploads'
#path = 'dummy_scripts'
for roots, dirs, files in os.walk(path):
	for scifile in files:
		if (scifile.find('.sci') != -1) or (scifile.find('.sce') !=-1 ):
			fullfile = roots+'/'+scifile
			print fullfile
			func_list = (extract_func(fullfile))
			
			if func_list != 0:
				for func_name in func_list:
					return_value = isCompatible(func_name)
					if return_value == 0 :
						print 'Function Compatible: ', func_name, '\n' 
					elif return_value == 1:
						print 'Function not compatible: ', func_name, '\n'
					else:
						print "User Function: ", func_name,'\n'
			# Call yelp
			#subprocess.call(['./yelp', fullfile])


# Remove contents from disp('contents') before searching functions
# argparse files
# remove comments from content before parsing DONE
# remove array from content, my_array(5) 5 => index
# integrate yelp
# printf( N(, N(, N(  case
# remove user funcions
# Function Centric Approach
