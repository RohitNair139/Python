#!/usr/bin/env python
# coding: utf-8

# Exploring Hackers News Posts
# In this project, we'll compare two different types of posts from Hacker News, a popular site where technology related stories (or 'posts') are voted and commented upon. The two types of posts we'll explore begin with either Ask HN or Show HN.
# 
# Users submit Ask HN posts to ask the Hacker News community a specific question, such as "What is the best online course you've ever taken?" Likewise, users submit Show HN posts to show the Hacker News community a project, product, or just generally something interesting.
# 
# We'll specifically compare these two types of posts to determine the following:
# 
# Do Ask HN or Show HN receive more comments on average?
# Do posts created at a certain time receive more comments on average?
# It should be noted that the data set we're working with was reduced from almost 300,000 rows to approximately 20,000 rows by removing all submissions that did not receive any comments, and then randomly sampling from the remaining submissions.

# In[2]:


import csv

f = open('hacker_news.csv')
hn = list(csv.reader(f))
hn[:5]


# In[3]:


headers = hn[0]


# In[4]:


hn= hn[1:]


# In[5]:


print(headers)


# In[6]:


print(hn[:5])


# In[7]:


ask_posts = []
show_posts =[]
other_posts = []

for post in hn:
    title = post[1]
    if title.lower().startswith("ask hn"):
        ask_posts.append(post)
    elif title.lower().startswith("show hn"):
        show_posts.append(post)
    else:
        other_posts.append(post)
        
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))


# In[8]:


total_ask_comments = 0
for row in ask_posts:
    total_ask_comments += int(row[4])
avg_ask_post = total_ask_comments / len(ask_posts)
print(avg_ask_post)


# In[9]:


total_show_comments = 0
for post in show_posts:
    total_show_comments += int(post[4])
average_show_comments = total_show_comments / len(show_posts)
print(average_show_comments)


# In[11]:


import datetime as dt


# In[17]:


result_list = []

for post in ask_posts:
    result_list.append(
        [post[6], int(post[4])])
    


# In[21]:


result_list = []

for post in ask_posts:
    result_list.append(
        [post[6], int(post[4])]
    )

comments_by_hour = {}
counts_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

for each_row in result_list:
    date = each_row[0]
    comment = each_row[1]
    time = dt.datetime.strptime(date, date_format).strftime("%H")
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1

comments_by_hour


# In[23]:


avg_comments_hr =[]
for comment in comments_by_hour:
    avg_comments_hr.append([comment,comments_by_hour[comment]/counts_by_hour[comment]])
    
    


# In[25]:


avg_comments_hr


# In[29]:


avg_by_hour = []

for hr in comments_by_hour:
    avg_by_hour.append([hr, comments_by_hour[hr] / counts_by_hour[hr]])

avg_by_hour


# In[30]:


swap_avg_by_hour = []

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])
    
print(swap_avg_by_hour)

sorted_swap = sorted(swap_avg_by_hour, reverse=True)

sorted_swap


# In[31]:


print("Top 5 Hours for 'Ask HN' Comments")
for avg, hr in sorted_swap[:5]:
    print(
        "{}: {:.2f} average comments per post".format(
            dt.datetime.strptime(hr, "%H").strftime("%H:%M"),avg
        )
    )


# In[ ]:




