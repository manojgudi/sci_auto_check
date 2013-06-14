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

def extract_func(abs_file):
	file_obj = open(abs_file, 'r')
	file_content = rm_comments(file_obj.read())
	list_of_func = re.findall("[\w]+\(", file_content)
	
	# Function to remove false positive loop keywords like for/while and array declarations
	def rm_loops(list_of_func, content):
		proper_func_list = []
		for func in list_of_func:
			if ((func != 'if') and (func != 'for') and (func != 'while') and (not(isArray(func,content)))): # Replace last condition by array condition
				func = func.strip("(")
				proper_func_list.append(func)

		return proper_func_list
	
	# If no functions are used
	if list_of_func == []:
		return 0

	list_of_func = list(set(rm_loops(list_of_func, file_content)))
	return list_of_func


# MAIN LOOP FOR TRAVERSING
path='/media/d2c1960d-a6c5-4a50-a642-1cd33212cde0/uploads/45/CH7/EX7.4/'
#path='/media/d2c1960d-a6c5-4a50-a642-1cd33212cde0/uploads'
for roots, dirs, files in os.walk(path):
	for scifile in files:
		if (scifile.find('.sci') != -1) or (scifile.find('.sce') !=-1 ):
			fullfile = roots+'/'+scifile
			print fullfile
			(extract_func(fullfile))
			# Call yelp
			#subprocess.call(['./yelp', fullfile])

#argparse files
# remove comments from content before parsing DONE
# remove array from content, my_array(5) 5 => index
# integrate yelp
# printf( N(, N(, N(  case
# remove user funcions

