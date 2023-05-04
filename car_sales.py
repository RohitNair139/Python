#!/usr/bin/env python
# coding: utf-8

# Analyzing Used Car Listings on eBay Kleinanzeigen
# We will be working on a dataset of used cars from eBay Kleinanzeigen, a classifieds section of the German eBay website.
# 
# The dataset was originally scraped and uploaded to Kaggle. The version of the dataset we are working with is a sample of 50,000 data points that was prepared by Dataquest including simulating a less-cleaned version of the data.
# 
# The data dictionary provided with data is as follows:
# 
# dateCrawled - When this ad was first crawled. All field-values are taken from this date.
# name - Name of the car.
# seller - Whether the seller is private or a dealer.
# offerType - The type of listing
# price - The price on the ad to sell the car.
# abtest - Whether the listing is included in an A/B test.
# vehicleType - The vehicle Type.
# yearOfRegistration - The year in which which year the car was first registered.
# gearbox - The transmission type.
# powerPS - The power of the car in PS.
# model - The car model name.
# kilometer - How many kilometers the car has driven.
# monthOfRegistration - The month in which which year the car was first registered.
# fuelType - What type of fuel the car uses.
# brand - The brand of the car.
# notRepairedDamage - If the car has a damage which is not yet repaired.
# dateCreated - The date on which the eBay listing was created.
# nrOfPictures - The number of pictures in the ad.
# postalCode - The postal code for the location of the vehicle.
# lastSeenOnline - When the crawler saw this ad last online.
# The aim of this project is to clean the data and analyze the included used car listings.

# In[28]:


import pandas as pd
import numpy as np


# In[29]:


autos = pd.read_csv("autos.csv",encoding ="Latin-1")


# In[30]:


autos.head()


# In[31]:


autos.info()


# In[32]:


autos["seller"].unique()


# In[33]:


autos["seller"].value_counts()


# In[34]:


autos.columns


# In[35]:


autos.shape


# In[36]:


### there has been some problems with column names so renaming it


# In[37]:


autos = autos.rename(columns={'yearOfRegistration' : 'registration_year','monthOfRegistration' :'registration_month',
                             'notRepairedDamage': 'unrepaired_damage','dateCreated' :'ad_created'})


# In[38]:


autos.columns


# In[39]:


autos.head()


# In[40]:


### cleaning of the data


# In[41]:


autos.describe(include ='all') ### so that we can get both categorical and numerical columsn


# In[43]:


### the  number of phots colums has some problem while most of the columns have same value


# In[46]:


autos = autos.rename(columns = {'nrOfPictures':'num_photos'})


# In[49]:


autos["num_photos"].value_counts()


# In[50]:


# any columns that have mostly one unique value will be dropped


# In[52]:


autos = autos.drop(["num_photos", "seller", "offerType"], axis=1)


# In[54]:


autos["price"] =  (autos["price"].str.replace("$","")
                                .str.replace(",","")
                                .astype(int)
                  )
        


# In[55]:


autos["price"].head()


# In[57]:


autos["odometer"] = (autos["odometer"].str.replace("km","")
                                       .str.replace(",","")
                                       .astype(int))


# In[58]:


autos.rename({"odometer": "odometer_km"}, axis=1, inplace=True)
autos["odometer_km"].head()


# In[61]:


autos["odometer_km"].value_counts()


# In[67]:


autos["odometer_km"].describe().round(0)


# In[69]:


autos["odometer_km"].shape


# In[70]:


autos["price"].shape


# In[74]:


autos["price"].unique().shape


# In[75]:


autos["price"].describe()


# In[76]:


autos["price"].value_counts()


# In[77]:


### there are 1421 entries that have listed 0 dollars in price


# In[80]:


autos["price"].sort_index(ascending= True)


# In[86]:


autos_less30 = autos[autos["price"] <30].shape[0]


# In[87]:


print(autos_less30)


# In[88]:


autos = autos[autos["price"].between(1,315000)]


# In[90]:


autos["price"].describe().round(0)


# In[91]:


### will be xploring the date columns


# In[95]:


autos[['dateCrawled','ad_created','lastSeen']][0:5]


# In[94]:


autos.columns


# In[98]:


autos["dateCrawled"].value_counts()


# In[99]:


autos["dateCrawled"].sort_index(ascending= True)


# In[102]:


print(autos["dateCrawled"].str[:10])


# In[103]:


autos["dateCrawled"].value_counts(normalize= True, dropna= False)


# In[105]:


(autos["ad_created"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_values()
        )


# In[106]:


(autos["lastSeen"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_values()
        )


# In[108]:


autos["registration_year"].describe().round(0)


# In[109]:


# the age of the car cant be 9999 so rectifiying it


# In[111]:


(~autos["registration_year"].between(1900,2016)).sum()/autos.shape[0]


# In[ ]:


# since this is an negligible value we will be removing these


# In[112]:


autos = autos[autos["registration_year"].between(1900,2016)]


# In[114]:


autos["registration_year"].value_counts(normalize=True).head()


# In[117]:


autos["registration_year"].unique()


# In[118]:


autos["registration_year"].shape


# In[119]:


cars_per_year = autos.groupby("registration_year").count()["name"]


# In[120]:


print(cars_per_year)


# In[123]:


cars_per_year.describe()


# In[124]:



autos["brand"].value_counts(normalize=True)


# In[125]:


#German manufacturers represent four out of the top five brands, almost 50% of the overall listings. Volkswagen is by far the most popular brand, with approximately double the cars for sale of the next two brands combined.


# In[131]:


brand_counts = autos["brand"].value_counts(normalize=True)
common_brands = brand_counts[brand_counts > .05].index
print(common_brands)


# In[132]:


brand_mean_prices = {}

for brand in common_brands:
    brand_only = autos[autos["brand"] == brand]
    mean_price = brand_only["price"].mean()
    brand_mean_prices[brand] = int(mean_price)

brand_mean_prices


# In[134]:


brand_mean_mileage = {}

for brand in common_brands:
    brand_only = autos[autos["brand"] == brand]
    mean_mileage = brand_only["odometer_km"].mean()
    brand_mean_mileage[brand] = int(mean_mileage)

mean_mileage = pd.Series(brand_mean_mileage).sort_values(ascending=False)
mean_prices = pd.Series(brand_mean_prices).sort_values(ascending=False)


# In[135]:


brand_info = pd.DataFrame(mean_mileage,columns=['mean_mileage'])
brand_info


# In[136]:


brand_info["mean_price"] = mean_prices
brand_info


# In[ ]:




