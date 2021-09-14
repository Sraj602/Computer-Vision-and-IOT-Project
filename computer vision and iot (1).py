#!/usr/bin/env python
# coding: utf-8

# # The Sparks Foundation IOT and Computer Vision intern
# 
# ## Task -2 Color Identification in Images
# 
# 
# ## By Shivam Raj
# 
# ### Importing The Required Packages
# 

# In[1]:


import cv2
import pandas as pd
import numpy as np


# ### Variable Declaration For Mouse Pointer Movement

# In[2]:


clicked = False
r = g = b = xpos = ypos = 0


# ### Reading the image 

# In[3]:


img = cv2.imread("Downloads\colorpicture.jpg")


# ### Taking colors data as input using Pandas 

# In[4]:


index = ['colors', 'color-names', 'hex-value', 'R-value', 'G-value', 'B-value'] 
df = pd.read_csv('Downloads/colors.csv', names = index, header = None)


# In[5]:


df


# ### Function for selecting color of selected point by double clicking the left button of mouse¶ 

# In[6]:


def selectColor(event, x, y , flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


# ### Taking a window to display an Image and callback Function for Mouse Events 

# In[7]:


cv2.namedWindow('image')
cv2.setMouseCallback('image',selectColor)


# ### Function for getting color name of selected area 

# In[8]:


def getColorName(R,G,B):
    minimum = 10000

    #  calculate a distance(d) which tells us how close we are to color and choose the one having minimum distance.
    for i in range(len(df)):
        d = abs(R-int(df.loc[i,'R-value']))+abs(G-int(df.loc[i,'G-value']))+abs(B-int(df.loc[i,'B-value']))
        if d<=minimum:
            minimum = d
            colorName = df.loc[i,"color-names"]
    return colorName


# ### Updates the color name whenever the double click occurs

# In[ ]:


while(1):

    # We shown the image window
    cv2.imshow('image',img)
    if(clicked):
        cv2.rectangle(img,(20,20),(750,60),(b,g,r),-1)
        text = getColorName(r,g,b)
        cv2.putText(img, text, (50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)

        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        
        clicked = False

    # Exits when the user presses the 'Esc' button
    if cv2.waitKey(20) & 0xFF ==27:
        break


# Clears all the windows       
cv2.destroyAllWindows()


# In[ ]:




