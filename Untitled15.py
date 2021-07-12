#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
array1 = array([1, 3, 5, 3, 7, 1, 9, 3])
num_list = array_num.tolist()
print(num_list)


# In[22]:




import numpy as np
m = np.arange(6).reshape(2,3)
print("Original matrix:")
print(m)
result =  np.trace(m)
print("Condition number of the said matrix:")
print(result)


# In[23]:


def min(a,x):
    variable=np.shape(a)
    n=variable[0]
    m=variable[1]
    for i in range(n):
            for j in range(m):
                if a[i,j]>x:
                    print(a[i,j])
a = np.array([[1,2],[3,5],[7,8]])
x=2
min(a,x)


# In[6]:


import numpy as np
def mean(a):
    variable=np.shape(a)
    n=variable[0]
    m=variable[1]
    S=0
    for i in range(n):
            for j in range(m): 
                S += a[i,j]
            Moyenne = S / m 
            print(Moyenne)
            S=0
                    
a = np.array([[1,2,4],[3,5,9],[7,8,10]])
mean(a)


# In[ ]:





# In[ ]:




