#! python3 
# filesort.py
#sorts the files based on their type and then move them into the catogerized folders
import os,re,shutil
os.chdir(r'D:\Chrome downloads') #enter the directory in which you want to perform the sort.
files = os.listdir(r'D:\Chrome downloads')
for i in files:
	if(i.endswith(".exe")):
		shutil.move(r'D:\Chrome Sorted\Setups')
	if(i.endswith(".zip")):
		shutil.move(r'D:\Chrome Sorted\Zip')
