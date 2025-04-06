#Creating ,reading writing and appending files in python.
first_file = 'file1.txt'
modified_file = 'file2.txt'
#puting the codes that might generate error in a try block
try:
    #opening file1 and reading its content.
    file = open(first_file,'r')
    data = file.read()

    print("Reading the contents of the first file before modification:"+data)
     
    #changing the contents of file1 to uppercase
    modified_content = data.upper()
    
    #writing the modified contents in a new file 
    file = open(modified_file, 'w')
    data = file.write(modified_content)

    print(f"modified content writen to '{modified_file}' successfully")

#excepting/catching the errors that might be generated.
except FileNotFoundError:
    print(f"Sorry but the file '{first_file}' does not exist")
except PermissionError:
    print("Permission denied to access the file.")

#closes the files/always executes
finally:
    if first_file:
        file.close()
    if modified_file:
        file.close()
    print("Program execution completed successfully.")