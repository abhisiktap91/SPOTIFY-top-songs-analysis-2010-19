#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install pandas


# In[51]:


pip install numpy


# In[52]:


pip install seaborn


# In[53]:


import pandas as pd
import sqlite3
import os
import matplotlib.pylab as plt
import seaborn as sns


# In[108]:


df=pd.read_csv('top10s.csv',encoding= "latin-1")


# In[9]:


df.columns=df.columns.str.strip()
df.columns=df.columns.str.replace(".","")
df.head()


# In[11]:


conn=sqlite3.connect('database.db')
c=conn.cursor()


# In[12]:


df.to_sql("TopSongss",conn)


# In[13]:


c.execute('''SELECT*from TopSongss;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[ ]:


conn.close()


# # GENRE

# In[17]:


c.execute('''SELECT "top genre",count(*)
from TopSongs
group by "top genre"
order by count(*) desc;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[19]:


c.execute('''SELECT count(*) as 'PopSongs'
from TopSongs
where "top genre" like '%pop%';''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[20]:


c.execute('''SELECT count(*) as 'RapSongs'
from TopSongs
where "top genre" like '%rap%';''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[21]:


c.execute('''SELECT count(*) as 'HipHopSongs'
from TopSongs
where "top genre" like '%hip hop%';''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[23]:


c.execute('''SELECT count(*) as HouseSongs
from TopSongs
where "top genre" like '%house%';''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[26]:


c.execute('''SELECT count(*) as EdmSongs
from TopSongs
where "top genre" like '%edm%';''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# # BEATS PER MINUTE

# In[33]:


c.execute('''SELECT avg(bpm)
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[34]:


c.execute('''SELECT Title,bpm,
(case when bpm > 118.545605 then 'Above Average'
when bpm = 118.545605 then 'Average'
when bpm < 118.545605 then 'Below Average' end)as CompareAverage
from TopSongss
limit 10;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[47]:


c.execute('''SELECT Title,bpm,
(case when bpm between 108.545605 and 128.545605 then 'Within 10'
when (bpm between 98.545605 and 108.545605) or (bpm between 128.545605 and 138.545605) then 'Within 20'
when (bpm between 88.545605 and 98.545605) or (bpm between 138.545605 and 148.545605)then 'Within 30'
else 'Greater than 30'
end)as CompareAverage
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[48]:


c.execute('''SELECT
sum(case when bpm between 108.545605 and 128.545605 then 1
else 0
end)as "Within 10",
sum(case when (bpm between 98.545605 and 108.545605) or (bpm between 128.545605 and 138.545605) then 1
else 0
end)as "Within 20",
sum(case when (bpm between 88.545605 and 98.545605) or (bpm between 138.545605 and 148.545605) then 1
else 0
end)as "Within 30",
sum(case when (bpm < 88.545605) or (bpm > 148.545605) then 1
else 0
end)as "Greater than 30"
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# # ENERGY

# In[39]:


c.execute('''SELECT avg(nrgy)
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[41]:


c.execute('''SELECT Title,nrgy,
(case when nrgy > 70.504146 then 'Above Average'
when nrgy = 70.504146 then 'Average'
when nrgy < 70.504146 then 'Below Average'
end)as CompareAverage
from TopSongs
limit 10;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[49]:


c.execute('''SELECT Title,nrgy,
(case
when nrgy between 60.504146 and 80.504146 then 'Within 10'
when (nrgy between 50.504146 and 60.504146) or (nrgy between 80.504146 and 90.504146) then 'Within 20'
when (nrgy between 40.504146 and 50.504146) or (nrgy between 90.504146 and 100.504146) then 'Within 30'
else 'Greater than 30'
end)as 'Compare Average'
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[50]:


c.execute('''SELECT
sum(case when nrgy between 60.504146 and 80.504146 then 1
else 0
end)as 'Within 10',
sum(case when (nrgy between 50.504146 and 60.504146) or (nrgy between 80.504146 and 90.504146) then 1
else 0
end)as 'Within 20',
sum(case when (nrgy between 40.504146 and 50.504146) or (nrgy between 90.504146 and 100.504146) then 1
else 0
end)as 'Within 30',
sum(case when (nrgy < 40.504146) or (nrgy > 100.504146) then 1
else 0
end)as 'Greater than 30'
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# # DANCEABILITY

# In[45]:


c.execute('''SELECT avg(dnce)
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[46]:


c.execute('''SELECT Title,dnce,
(case
when dnce between 54.379768 and 74.379768 then 'Within 10'
when (dnce between 44.379768 and 54.379768) or (dnce between 74.379768 and 84.379768) then 'Within 20'
when (dnce between 34.379768 and 44.379768) or (dnce between 84.379768 and 94.379768) then 'Within 30'
else 'Greater than 30'
end)as CompareAverage
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[52]:


c.execute('''SELECT
sum(case when dnce between 54.379768 and 74.379768 then 1
else 0
end)as 'Within 10',
sum(case when (dnce between 44.379768 and 54.379768) or (dnce between 74.379768 and 84.379768) then 1
else 0
end)as 'Within 20',
sum(case when (dnce between 34.379768 and 44.379768) or (dnce between 84.379768 and 94.379768) then 1
else 0
end)as 'Within 30',
sum(case when (dnce < 34.379768) or (dnce > 94.379768) then 1
else 0
end)as 'Greater than 30'
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# # LOUDNESS

# In[53]:


c.execute('''SELECT avg(dB)
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[55]:


c.execute('''SELECT Title,dB,
(case 
when dB > -5.578773 then 'Above Average'
when dB = -5.578773 then 'Average'
when dB < -5.578773 then 'Below Average'
end)as CompareAverage
from TopSongs
limit 10;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[58]:


c.execute('''SELECT Title,dB,
(case
when dB between -6.578773 and -4.578773 then 'Within 1'
when (dB between -7.578773 and -6.578773) or (dB between -4.578773 and -3.578773) then 'Within 2'
when (dB between -8.578773 and -7.578773) or (dB between -3.578773 and -2.578773) then 'Within 3'
else 'Greater than 3'
end)as CompareAverage
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[60]:


c.execute('''SELECT
sum(case when dB between -6.578773
 and -4.578773
 then 1
else 0
end)as 'Within 1',
sum(case when (dB between -7.578773
 and -6.578773
) or (dB between -4.578773
 and -3.578773
) then 1
else 0
end)as 'Within 2',
sum(case when (dB between -8.578773
 and -7.578773
) or (dB between -3.578773
 and -2.578773
) then 1
else 0
end)as 'Within 3',
sum(case when (dB < -8.578773) or (dB > -2.578773) then 1
else 0
end)as 'Greater than 3'
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# # LIVENESS

# In[61]:


c.execute('''SELECT avg(Live)
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[62]:


c.execute('''SELECT Title,Live,
(case 
when Live > 17.774461 then 'Above Average'
when Live = 17.774461 then 'Average'
when Live < 17.774461 then 'Below Average'
end)as CompareAverage
from TopSongs
limit 10;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[63]:


c.execute('''SELECT Title,Live,
(case
when Live between 14.774461 and 20.774461 then 'Within 3'
when (Live between 11.774461 and 14.774461) or (Live between 20.774461 and 23.774461) then 'Within 6'
when (Live between 8.774461 and 11.774461) or (Live between 23.774461 and 26.774461) then 'Within 9'
else 'Greater than 3'
end)as CompareAverage
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[64]:


c.execute('''SELECT
sum(case when Live between 14.774461 and 20.774461 then 1
else 0
end)as 'Within 3',
sum(case when (Live between 11.774461 and 14.774461) or (Live between 20.774461 and 23.774461) then 1
else 0
end)as 'Within 6',
sum(case when (Live between 8.774461 and 11.774461) or (Live between 23.774461 and 26.774461) then 1
else 0
end)as 'Within 9',
sum(case when (Live < 8.774461) or (Live > 26.774461) then 1
else 0
end)as 'Greater than 9'
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# # VALENCE

# In[12]:


c.execute('''SELECT avg(val)
from TopSongss;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[14]:


c.execute('''SELECT Title,val,
(case 
when val > 52.225539 then 'Above Average'
when val = 52.225539 then 'Average'
when val < 52.225539 then 'Below Average'
end)as CompareAverage
from TopSongs
limit 10;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[15]:


c.execute('''SELECT Title,val,
(case
when val between 47.225539 and 57.225539 then 'Within 5'
when (val between 42.225539 and 47.225539) or (val between 57.225539 and 62.225539) then 'Within 10'
when (val between 37.225539 and 42.225539) or (val between 62.225539 and 67.225539) then 'Within 15'
else 'Greater than 15'
end)as CompareAverage
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[16]:


c.execute('''SELECT
sum(case when val between 47.225539 and 57.225539 then 1
else 0
end)as Within5,
sum(case when (val between 42.225539 and 47.225539) or (val between 57.225539 and 62.225539) then 1
else 0
end)as Within10,
sum(case when (val between 37.225539 and 42.225539) or (val between 62.225539 and 67.225539) then 1
else 0
end)as Within15,
sum(case when (val< 37.225539) or (live > 67.225539) then 1
else 0
end)as Greater15
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# # SPEECHINESS

# In[17]:


c.execute('''SELECT avg(spch)
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[32]:


c.execute('''SELECT Title,"top genre",spch
from TopSongss
where "top genre" like '%rap%';''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[34]:


c.execute('''SELECT Title,"top genre",spch
from TopSongs
where spch >=36;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[37]:


c.execute('''SELECT ((SELECT count(*)*1.0
from TopSongs
where "top genre" like '%pop%' and spch>=36)/count(*)*1.0)*100 as PopPercentWithHighSpeechiness
from TopSongs
where "top genre" like '%pop%';''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[38]:


c.execute('''SELECT Title,spch,
(case 
when spch > 8.358209 then 'Above Average'
when spch = 8.358209 then 'Average'
when spch < 8.358209 then 'Below Average'
end)as CompareAverage
from TopSongs
limit 10;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[39]:


c.execute('''SELECT Title,spch,
(case
when spch between 17.16 and 27.16 then 'Within 5'
when (spch between 12.16 and 17.15) or (spch between 27.17 and 32.16) then 'Within 10'
when (spch between 7.16 and 12.15) or (spch between 32.16 and 37.16) then 'Within 15'
else 'Greater than 15'
end)as CompareAverage
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[40]:


c.execute('''SELECT
sum(case when spch between 17.16 and 27.16 then 1
else 0
end)as Within5,
sum(case when (spch between 12.16 and 17.15) or (spch between 27.17 and 32.16) then 1
else 0
end)as Within10,
sum(case when (spch between 7.16 and 12.15) or (spch between 32.16 and 37.16) then 1
else 0
end)as Within15,
sum(case when (spch < 7.16) or (spch > 37.16) then 1
else 0
end)as Greater15
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# # POPULARITY

# In[41]:


c.execute('''SELECT avg(pop)
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[42]:


c.execute('''SELECT Title,pop
from TopSongs
order by pop desc
limit 10;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data



# In[43]:


c.execute('''SELECT Title,pop,
(case 
when pop > 66.52073 then 'Above Average'
when pop = 66.52073 then 'Average'
when pop < 66.52073 then 'Below Average'
end)as CompareAverage
from TopSongs
limit 10;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[45]:


c.execute('''SELECT title,pop,
(case
when pop between 63.52073 and 69.52073 then 'Within 3'
when (pop between 60.52073 and 63.52073) or (pop between 69.52073 and 72.52073) then 'Within 6'
when (pop between 57.52073 and 60.52073) or (pop between 72.52073 and 75.52073) then 'Within 9'
else 'Greater than 9'
end)as CompareAverage
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[46]:


c.execute('''SELECT
sum(case when pop between 63.52073 and 69.52073 then 1
else 0
end)as Within3,
sum(case when (pop between 60.52073 and 63.52073) or (pop between 69.52073 and 72.52073) then 1
else 0
end)as Within6,
sum(case when (pop between 57.52073 and 60.52073) or (pop between 72.52073 and 75.52073) then 1
else 0
end)as Within9,
sum(case when (pop < 57.52073) or (pop > 75.52073) then 1
else 0
end)as Greater9
from TopSongs;''')
data=pd.DataFrame(c.fetchall())
data.columns=[x[0] for x in c.description]
data


# In[60]:


# heatmap of all numerical variables
selected_columns = df[['year', 'bpm', 'nrgy', 'dnce', 'dB', 'live', 'val', 'dur', 'acous', 'spch', 'pop']]

sns.set_theme(rc={'figure.figsize': (13, 13)})
colormap = sns.color_palette("coolwarm", as_cmap=True)
sns.heatmap(selected_columns.corr(), cmap=colormap, annot=True)

plt.show()


# In[61]:


# histogram for all variables
df.hist(figsize= [15, 15])


# In[63]:


# Query the Artist with Top Songs and Count of Top Songs Each Artist has
c.execute('''SELECT artist, COUNT(*)
            FROM TopSongs
            GROUP BY artist
            ORDER BY COUNT(*) DESC;''')
df = pd.DataFrame(c.fetchall())
df.columns = [x[0] for x in c.description]
df_top_ten = df.head(10)
df_top_ten


# In[127]:


sns.barplot(x="artist", y="COUNT(*)", color="Orange", data=df_top_ten, width=0.5)
sns.set(style="whitegrid", font_scale=0.9)


# In[118]:


nrgy_column = df['nrgy']
print(nrgy_column)
acous_column= df['acous']
print(acous_column)


# In[119]:


plt.figure(figsize=(6, 4))
plt.scatter(x=nrgy_column, y=acous_column, color='blue', marker='.', label='Data Points')
plt.xlabel('energy')
plt.ylabel('acoustics')
plt.title('Energy vs. Acoustics')

plt.show()


# In[120]:


dB_column= df['dB']
print(acous_column)
dnce_column = df['dnce']
print(nrgy_column)



# In[124]:


plt.figure(figsize=(3, 3))
plt.scatter(x=dnce_column, y=dB_column, color='blue', marker='.', label='Data Points')
plt.xlabel('danceability')
plt.ylabel('dB')
plt.title('danceability vs.dB')

plt.show()


# In[130]:


bpm_column= df['bpm']
print(bpm_column)
dnce_column = df['dnce']
print(dnce_column)


# In[131]:


plt.figure(figsize=(3, 3))
plt.scatter(x=dnce_column, y=bpm_column, color='blue', marker='.', label='Data Points')
plt.xlabel('danceability')
plt.ylabel('bpm')
plt.title('danceability vs.bpm')

plt.show()


# In[132]:


bpm_column= df['bpm']
print(bpm_column)
dur_column = df['dur']
print(dur_column)


# In[133]:


plt.figure(figsize=(3, 3))
plt.scatter(x=bpm_column, y=dur_column, color='blue', marker='.', label='Data Points')
plt.xlabel('bpm')
plt.ylabel('duration')
plt.title('bpm vs.duration')

plt.show()


# In[150]:


from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
slices=[17,16,15,15,14,13,11,11,11,11]
labels=['Katy Perry','Justin Bieber','Rihanna','Maroon 5','Lady Gaga','Bruno Mars','The Chainsmokers','Shawn Mendes','Pitbull','Ed Sheeran']
colours=['b','g','r','c','m','y','k','w','g','r']
plt.pie(slices,labels=labels,colors=colours,shadow='true',autopct='%1.1f%%')
plt.title('Top 10 Artists')
plt.tight_layout()
plt.show()

