#!/usr/bin/env python
# coding: utf-8

# # Q.1

# First variable is  a = 10 & second variable is b= 5

# In[2]:


a = 10
b = 5


# In[4]:


print("the value of", a, "+" ,b , "is:" ,a+b )
print("the value of", a, "-" ,b , "is:" ,a-b )
print("the value of", a, "/" ,b , "is:" ,a/b )
print("the value of", a, "*" ,b , "is:" ,a*b )


# # Q.2

# ### (1)  "/" 

# it is used for the division 

# In[7]:


10 / 5


# In[8]:


20/3


# In[9]:


10/3


# ### "//"

# Floor division: it is used to print the only value before decimal 

# In[10]:


10//5


# In[11]:


20//3


# In[12]:


10//3


# ### (2)    '**'

# Exponential Operator : it is used to print the pwer of function.
# 

# In[14]:


(10**3)


# In[15]:


20**4


# In[16]:


4**6


# ### '^'

# Bitwise XOR : in this if one bit is 1 (bur not both) ,the corresponding result bit is set to be 1,otherwise 0
# 

# In[19]:


10^4


# In[23]:


bin(10)


# In[24]:


bin(4)


# In[27]:


# so 1010^100 is 1110


# In[28]:


bin(14)


# # Q.3

# ## Logical Operator
# these are conjuctuons that we can use to combine more than one condition.
# 
# we have three Python logicals operator and,or, and not.

# 1. and 
# 2. or
# 3. not

# # Q.4

# ## Right shift operator
# Bitwise right shift: Shifts the bits of the number to the right and fills 0 on voids left( fills 1 in the case of a negative number) as a result. Similar effect as of dividing the number with some power of two. Example:

# In[32]:


#Example 1:
a = 10  #0000 1010 (Binary)
a >> 1  #0000 0101 =  5 


# In[40]:


#Example 1:
a = 10  #0000 1010 (Binary)
a >> 2  #0000 0010 =  2 


# In[33]:


#Example 2:
a = -10 #= 1111 0110 (Binary)
a >> 1 #= 1111 1011 = -5 


# In[37]:


a = 20 
a>>2


# In[39]:


a = 20 
a>>1


# In[38]:


bin(5)


# In[38]:


bin(5)


# ## Left shift operator
# Bitwise left shift: Shifts the bits of the number to the left and fills 0 on voids right as a result. Similar effect as of multiplying the number with some power of two. Example:

# In[34]:


a = 10
a<<1


# In[41]:


a = 10
a<<2


# In[35]:


bin(20)


# In[36]:


a= -10
a<<1


# In[42]:


bin(40)


# # Q.5

# In[49]:


# Create a list of 15 random integers between 1 and 20
import random
my_list = [random.randint(1, 20) for i in range(15)]

# Print the list
print( my_list)

# Check if 10 is in the list
if 10 in my_list:
    print("10 is present in the list")
else:
    print("10 is not present in the list")


# In[ ]:




