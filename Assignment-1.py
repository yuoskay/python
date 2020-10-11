#!/usr/bin/env python
# coding: utf-8

# # 1. Python program to find the largest number in a list

# In[3]:


num_list = [100, 200, 700, 900, 2000, 800]
print("{} is the largest number in the list ".format(max(num_list)))


# # 2. Python program to find the second largest number in a list

# In[4]:


list = [600,300,700,2000,1000,1200]
list.sort(reverse = True)
print("{} is the second largest number of list".format(list[1]))


# # 3.Python program to merge two lists and sort it

# In[5]:


list_1 = [100, 200, 300, 400, 500, 600]
list_2 = [700, 800, 900, 1000, 1100, 1200]
list_merged = list_1 + list_2
list_merged.sort()
list_merged


# # 4. Python program to swap the first and last value of a list

# In[6]:


list_num = [20, 33, 9, 200, 64, 73]
list_num[0], list_num[len(list_num) - 1] = list_num[len(list_num) - 1], list_num[0]
list_num


# In[ ]:




