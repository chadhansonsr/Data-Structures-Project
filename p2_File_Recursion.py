
import glob

search1 = glob.glob(r"\Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project/**/*.c", recursive = True)
print("Here are the files ending with .c.")
for search in search1:
    print(search) # search will return
                  # \Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project\testdir\t1.c
                  # \Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project\testdir\subdir1\a.c
                  # \Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project\testdir\subdir3\subsubdir1\b.c
                  # \Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project\testdir\subdir5\a.c


search2 = glob.glob(r"\Users\t9349ch\Desktop\SWX\Udacity\Data Structures Project/**/*.jpg", recursive = True)
print("Here are the files ending with .jpg.")
for search in search2:
    print(search) # search will be blank because there are no .jpg files

search3 = glob.glob(r"\my location has a typo/**/*.c", recursive = True)
print("Here are the files ending with .c.")
for search in search3:
    print(search) # search will be blank because of directory typo