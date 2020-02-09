#! python3 
# filesort.py
#sorts the files based on their type and then move them into the catogerized folders
import os,re,shutil
os.chdir(r'D:\Chrome downloads') #enter the directory in which you want to perform the sort.
files = os.listdir(r'D:\Chrome downloads')
for i in files:
	if(i.endswith(".exe")|i.endswith(".msi")):
		shutil.move(i,r'D:\Chrome Sorted\Setups')
	if(i.endswith(".zip")):
		shutil.move(i,r'D:\Chrome Sorted\Zip')
	if(i.endswith(".pdf")):
		shutil.move(i,r'D:\Chrome Sorted\PDFs')
	if(i.endswith(".rar")):
		shutil.move(i,r'D:\Chrome Sorted\rar_files')
	if(i.endswith(".mp4")):
		shutil.move(i,r'D:\Chrome Sorted\videos')
	if(i.endswith(".jpg")):
		shutil.move(i,r'D:\Chrome Sorted\Images')
print("All files are placed in their respective folder")
