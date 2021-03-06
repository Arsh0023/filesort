#! python3 
# filesort.py
#sorts the files based on their type and then move them into the catogerized folders
import os,shutil
q = 0
moved_files = []
not_moved = []
moved_files_address = []
path = os.path.isdir(r'D:\Chrome Downloads') 

if(path):
	if(len(os.listdir(r'D:\Chrome Downloads')) != 0):                                                            #files should be there in directory
		if(os.path.isdir(r'D:\Chrome Sorted')):
			pass
		else:
			os.makedirs(r'D:\Chrome Sorted')
			print("directory created - D:\\Chrome Sorted")
		os.chdir(r'D:\Chrome Downloads') #enter the directory in which you want to perform the sort.
		files = os.listdir(r'D:\Chrome Downloads')
		folder_names = ['Setups','Zip','PDFs','rar_files','videos','Images','CSV']
		for names in folder_names:
			os.chdir(r'D:\Chrome Sorted')
			if(os.path.isdir(names)):
				pass
			else:
				os.makedirs(names)
				q +=1
				print("created directory - ",names)
		os.chdir(r'D:\Chrome Downloads')
		n = 0
		total = 0
		for i in files:
			temp = total
			if(i.endswith(".exe")|i.endswith(".msi")):
				shutil.move(i,r'D:\Chrome Sorted\Setups')
				moved_files.append(i)
				moved_files_address.append(r'D:\Chrome Sorted\Setups')
				total+=1
			if(i.endswith(".zip")):
				shutil.move(i,r'D:\Chrome Sorted\Zip')
				moved_files.append(i)
				moved_files_address.append(r'D:\Chrome Sorted\Zip')
				total+=1
			if(i.endswith(".pdf")):
				shutil.move(i,r'D:\Chrome Sorted\PDFs')
				moved_files.append(i)
				moved_files_address.append(r'D:\Chrome Sorted\PDFs')
				total+=1
			if(i.endswith(".rar")):
				shutil.move(i,r'D:\Chrome Sorted\rar_files')
				moved_files.append(i)
				moved_files_address.append(r'D:\Chrome Sorted\rar_files')
				total+=1
			if(i.endswith(".mp4")):
				shutil.move(i,r'D:\Chrome Sorted\videos')
				total+=1
				moved_files.append(i)
				moved_files_address.append(r'D:\Chrome Sorted\videos')
			if(i.endswith(".jpg")):
				shutil.move(i,r'D:\Chrome Sorted\Images')
				total+=1
				moved_files.append(i)
				moved_files_address.append(r'D:\Chrome Sorted\Images')
			if(i.endswith(".csv")|i.endswith(".CSV")):
				shutil.move(i,r'D:\Chrome Sorted\CSV')
				total += 1
				moved_files.append(i)
				moved_files_address.append(r'D:\Chrome Sorted\CSV')
			if(temp == total):
				not_moved.append(i)
			

			n+=1
		if(q != 0):
			print("\n\n")
		print("total files - ",n)
		print("number of files moved - ",total)
		print("files left - ",n-total)
		if(total != 0):
			print("All files are placed in their respective folder")
			count = 1
			print("\n\nfiles moved - "+"\n")
			address_count = 0
			for i in moved_files:
				print(str(count)+". ",i," >>> ",moved_files_address[address_count],"\n")
				address_count += 1
				count+=1
		while(not_moved[0]):
			print("\n\nFiles not moved are :-")
			not_moved_count = 1
			for i in not_moved:
				print(str(not_moved_count)+".",i,"\n")
				not_moved_count+=1
			break
	else:
		print("Place the files you want to sort in D:\\Chrome Downloads and run the program again")
else:
	os.makedirs(r'D:\Chrome Downloads')
	print("created the directory - Chrome Downloads ,place the files you want to sort in it and run the program again")
