try:
    with open("../samplefile.txt", "r") as fh:
        content = fh.read()
        num_w = content.split()
        print("Number of words = ", len(num_w))
        num_l = content.split("\n")
        print("Number of lines = ", len(num_l))
except FileNotFoundError:
    print("The file you're trying to access does not exist")
except PermissionError:
    print ("You do not have permission to view this file")    
except OSError:
    print("Corrupt file detected")
except IsADirectoryError:
    print("The file is a directory")
except:
    print("Error access file") 