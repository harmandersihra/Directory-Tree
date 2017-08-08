#get_directory_structure.py
#Generates text file of all files and folders in specified directory
#Usage: list_directory_names_harmy.py <directory to be searched>
import os  #Used for getting directory information
import sys #Used for sys.exit and arguments
import io  #Used to avoid encoding errors

#Recursive function which searches through directories
def traverse(directory, depth):
	#Setting global to make sure counts are updated
	global directory_count, file_count, file_size

	#Make sure directory is accessible
	try:
		files = os.listdir(directory)
	except:
		print("Could not access: " + directory)
		return

	#Iterate through list and add all files to report
	for file in files:
		#Ignore if file ends in .ini or .db
		if ".ini" in file or ".db" in file: continue

		#Adding formatting
		for i in range(0, depth): report.write("\t")

		#Getting full path
		full_path = directory + "\\" + file

		#If it's a directory, print to report and traverse further
		if os.path.isdir(full_path):
			report.write(file + "\n")
			directory_count += 1
			traverse(full_path, depth + 1)

		#If it's a file, add file size
		elif os.path.isfile(full_path):
			report.write(file + "\n")
			file_count += 1
			file_size += os.path.getsize(full_path)

	#Add new line to separate
	report.write("\n")

#Function to convert bytes to human readable formats
def get_human_readable(size):
	suffixes = ['B','KB','MB','GB','TB']
	suffixIndex = 0
	while size > 1024 and suffixIndex < 4:
		suffixIndex += 1   #increment the index of the suffix
		size = size/1024.0 #apply the division
	return "%.2f%s"%(size, suffixes[suffixIndex])


#Beginning of Script Logic
print("list_directory_names_harmy.py running")

#Ensuring that arguments are correct
if len(sys.argv) != 2:
	print("Improper number of arguments.")
	print("Usage: list_directory_names_harmy.py <directory to be searched>")
	sys.exit(1)

#Create file in current working directory
report = io.open(os.getcwd() + "/report.txt", "w", encoding = "utf-8")

#If final backslash is present, get rid of it
directory = sys.argv[1]
if directory.endswith("\\"): directory = directory[:-1]

#Making sure directory is valid
if not os.path.exists(sys.argv[1]):
	print("Invalid directory entered")
	sys.exit(1)

#Variables to return number of files/directories, and total filesize
file_count      = 0
directory_count = 0
file_size       = 0

#Calling traverse function
traverse(directory, 0)

#Printing stats
print("Total Files:\t\t" + str(file_count))
print("Total Directories:\t" + str(directory_count))
print("Total Size:\t\t" + get_human_readable(file_size))
print("Check report.txt for list of all files and directories found")

#Ending program
report.close()
sys.exit(0)
