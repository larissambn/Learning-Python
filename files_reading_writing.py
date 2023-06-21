## Char	    Meaning
## 'r'	    open for reading (default)
## 'w'	    open for writing, truncating the file first
## 'x'	    open for exclusive creation, failing if the file already exists
## 'a'	    open for writing, appending to the end of the file if it exists
## 'b'	    binary mode
## 't'	    text mode (default)
## '+'	    open a disk file for updating (reading and writing)


# Open a file for writing and create it if it doesn't exist
f = open("textfile.txt", "w+")

# write some lines of data to the file
for i in range(10):
    f.write("This is line " + str(i) + "\r\n")

# close the file when done
f.close()


# Open the file for appending text to the end
f = open("textfile.txt", "a")
for i in range(10):
    f.write("This is line " + str(i) + "\r\n")

# close the file when done
f.close()

# Open the file back up and read the contents
f = open("textfile.txt", "r") 
    
if f.mode == 'r':
    contents = f.read()
    print(contents)

# close the file when done
f.close()
