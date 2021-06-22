#!/usr/bin/env python
# coding: utf-8

# # The OS module in Python provides functions for interacting with the operating system

# #Getting the Current working directory
# 
# ->To get the location of the current working directory os.getcwd() is used.
# 
# ->Consider Current Working Directory(CWD) as a folder, where the Python is operating
# 
# ->

# In[4]:


import os
cwd = os.getcwd()
print(cwd)


# In[ ]:


#Changing the Current working directory

->To change the current working directory(CWD) os.chdir() method is used. 

->This method changes the CWD to a specified path.


# In[16]:


import os

changedir = os.chdir('F:\game AI')

cwd = os.getcwd()
print(cwd)


# In[ ]:


#Creating a Directory


# In[ ]:


->Using os.mkdir()

os.mkdir() method in Python is used to create a directory named path with the specified numeric mode. 
This method raise FileExistsError if the directory to be created already exists.


# In[19]:


import os
directory = "kishandongare"
parentdir = "F:\game AI"
path = os.path.join(parentdir, directory)
os.mkdir(path)


# In[22]:


import os
directory = "kishan\dongare"
parentdir = "F:\game AI"
path = os.path.join(parentdir, directory)
os.mkdir(path)


# In[ ]:


->Using os.makedirs()

os.makedirs() method in Python is used to create a directory recursively.
That means while making leaf directory if any intermediate-level directory is
missing, os.makedirs() method will create them all.

mode: The permissions that needs to be given to deal with the file operations within the directory.
The default value being ‘0o777‘.Setting mode = 0o666, allows read and write file operations within the created directory.


# In[23]:


import os
directory = "kishan\dongare"
parentdir = "F:\game AI"
path = os.path.join(parentdir, directory)
mode = 0o666
os.makedirs(path, mode)


# In[ ]:


#Listing out Files and Directories with Python


# In[ ]:


->os.listdir()

method in Python is used to get the list of all files and directories in the specified directory. 
If we don’t specify any directory, then list of files and directories in the current working directory will be returned.


# In[24]:


list_dir = os.listdir('F:\game AI')
print(list_dir)                     


# In[ ]:


#Deleting Directory


# In[ ]:


->Using os.remove()

os.remove() method in Python is used to remove or delete a file path. This method can not remove or delete a directory.
If the specified path is a directory then OSError will be raised by the method.


# In[25]:


remove_file = os.remove('F:\game AI\kishandongare\kishan.txt')
print(remove_file)


# In[26]:


remove_file = os.remove('F:\game AI\kishandongare\kishan.txt')
print(remove_file)


# In[ ]:


->Using os.rmdir()

os.rmdir() method in Python is used to remove or delete a empty directory. 
OSError will be raised if the specified path is not an empty directory.


# In[30]:


remove_dir = os.rmdir('F:\game AI\kishandongare')
print(remove_dir)


# In[31]:


remove_dir = os.rmdir('F:\game AI\kishandongare')
print(remove_dir)


# In[ ]:


#Commonly Used Functions


# In[ ]:


->os.name 
    
This function gives the name of the operating system dependent module imported.
The following names have currently been registered: ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’ 


# In[32]:


import os
print(os.name)


# In[ ]:


->os.rename() 

A file old.txt can be renamed to new.txt, using the function os.rename(). 
The name of the file changes only if, the file exists and 
the user has sufficient privilege permission to change the file.


# In[39]:


fd  = "F:\\game AI\\New.txt"
os.rename(fd,'F:\game AI\kishan.txt')


# In[ ]:


fd  = "F:\\game AI\\New.txt"
os.rename(fd,'F:\game AI\kishan.txt')


# In[ ]:


-> os.path.exists()
    
This method will check whether a file exists or not by passing the name of the file as a parameter. 
OS module has a sub-module named PATH by using which we can perform many more functions. 


# In[43]:


import os

result = os.path.exists("file_name.txt") 
 
print(result)


# In[42]:


import os

result = os.path.exists("kishan.txt") 
 
print(result)


# In[ ]:


->os.path.getsize()

In this method, python will give us the size of the file in bytes.
To use this method we need to pass the name of the file as a parameter.


# In[46]:


import os 
 
size = os.path.getsize("kishan.txt")
print(size)


# In[ ]:


->os.popen()

This method opens a pipe to or from command. 
The return value can be read or written depending on whether the mode is ‘r’ or ‘w’. 
 


# In[47]:


import os
fd = "kishan.txt"
 
file = open(fd, 'w')
file.write("Hello")
file.close()

 


# In[48]:


file = open(fd, 'r')
text = file.read()
print(text)


# In[51]:


import os
fd = "kishan.txt"
file = os.popen(fd, 'w')
file.write("Hello")


# In[ ]:


->os.close() 

Close file descriptor fd. A file opened using open(), 
can be closed by close()only. But file opened through os.popen(),
can be closed with close() or os.close(). 
If we try closing a file opened with open(), 
using os.close(), Python would throw TypeError. 


# In[54]:


fd = "kishan.txt"
file = open(fd, 'r')
text = file.read()
print(text)
os.close(file)


# In[ ]:


->os.error
    
All functions in this module raise OSError in the case of invalid or inaccessible file names and paths, 
or other arguments that have the correct type, but are not accepted by the operating system.
os.error is an alias for built-in OSError exception.


# In[58]:



import os
try:   
    filename = 'ki.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()
except IOError:
      print('Problem reading:' + filename)
  


# In[ ]:




