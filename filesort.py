#! python3 
# filesort.py
#sorts the files based on their type and then move them into the catogerized folders
import os,re,shutil
q = 0
path = os.path.isdir(r'D:\Chrome Downloads') #boolean for path
if(path):
	if(len(os.listdir(r'D:\Chrome Downloads')) != 0):                                                            #files should be there in directory
		if(os.path.isdir(r'D:\Chrome Sorted')):
			pass
		else:
			os.makedirs(r'D:\Chrome Sorted')
			print("directory created - D:\\Chrome Sorted")
		os.chdir(r'D:\Chrome Sorted') #enter the directory in which you want to perform the sort.
		files = os.listdir(r'D:\Chrome Downloads')
		folder_names = ['Setups','Zip','PDFs','rar_files','videos','Images']
		for names in folder_names:
			if(os.path.isdir(names)):
				pass
			else:
				os.makedirs(names)
				q +=1
				print("created directory - ",names)
		n = 0
		total = 0
		for i in files:
			if(i.endswith(".exe")|i.endswith(".msi")):
				shutil.move(i,r'D:\Chrome Sorted\Setups')
				total+=1
			if(i.endswith(".zip")):
				shutil.move(i,r'D:\Chrome Sorted\Zip')
				total+=1
			if(i.endswith(".pdf")):
				shutil.move(i,r'D:\Chrome Sorted\PDFs')
				total+=1
			if(i.endswith(".rar")):
				shutil.move(i,r'D:\Chrome Sorted\rar_files')
				total+=1
			if(i.endswith(".mp4")):
				shutil.move(i,r'D:\Chrome Sorted\videos')
				total+=1
			if(i.endswith(".jpg")):
				shutil.move(i,r'D:\Chrome Sorted\Images')
				total+=1
			n+=1
		if(q != 0):
			print("\n\n")
		print("total files - ",n)
		print("number of files moved - ",total)
		print("files left - ",n-total)
		if(total != 0):
			print("All files are placed in their respective folder")
	else:
		print("Place the files you want to sort in D:\\Chrome Downloads and run the program again")
else:
	os.makedirs(r'D:\Chrome Downloads')
	print("created the directory - Chrome Downloads ,place the files you want to sort in it and run the program again")
