import os

print ("Renaming files in directory:......" , os.getcwd().upper(), )
curr = os.listdir(os.getcwd())
go = "y"
go = input("If this directory is correct, press Y to continue... \n")

if go == "y" or go == "Y":
    suffix = 1
    for file in curr:
        base, ext = os.path.splitext(file)
        if ext == ".txt" or ext == ".doc":
            dst = os.getcwd() + "\\" + "Machine__" + str(suffix) + ".pdf"
            src = os.getcwd() + "\\" + file
            print("Renaming", file, "right now...")
            os.rename(src,dst)
            suffix += 1
            print ("Rename was successfull!! \n \n")
        else:
            pass
    print ("Program Completed.")
else:
    pass
