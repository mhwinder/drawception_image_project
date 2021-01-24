# Drawception Image Project

## Problem Statement

Create a model to predict the number of reactions an image on drawception.com will recieve.

## Data
The data used for this project was scraped directly from drawception.com from dec-17-2020 to jan-1-2021. The images included in this repository are restricted to the ones I've personally created, the full set of data includes over 40,000 images with 500x600 resolution totalling ~1.4 GB. Full disclosure I have personnally provided reactions to ~ 100 images in this dataset. I have been a member of the site since 2015 and consider myself a typical user.

Scraping drawception occurs in 3 stages. The first step is to collect the url's to the pages with the images on them. These pages are each referred to as games, and each game has between 6-12 image panels. After the game url's are collected the data from the panels can be scraped. It's important to allow some time to pass for the players of the game to react to the images. Any reactions made after the scrape will not be included in my data. The final step is to download the images to disk, which is done with a third function.
 
|Feature|Type|Source|Description|
|---|---|---|---|
|pre_caption|object| drawception.com |Text used as a prompt for the drawing| 
|post_caption|object| drawception.com |Text written to describe the drawing| 
|image_url|object| drawception.com |URL of the image on drawception.com| 
|image_path|object| drawception.com |Local path of the drawing| 
|author|object| drawception.com |Username of the creator of the drawing| 
|panel_number|int| drawception.com |The place in the game that this drawing occurs|
|game_url|object| drawception.com |URL to the game in which the drawing appears| 
|player_num|int| drawception.com |Number of players who participated in the game in which this drawing appears| 
|game_duration|object| drawception.com |Number of days or hours the game took to complete (with units as a string)| 
|game_date|object| drawception.com |The date the game was completed| 
|game_tags|object| drawception.com |Any special modifiers to the game| 
|---|---|---|---|
|LIKE|int| drawception.com |Number of LIKE reactions this drawing recieved| 
|HAHA|int| drawception.com |Number of HAHA reactions this drawing recieved| 
|WOW|int| drawception.com |Number of WOW reactions this drawing recieved| 
|LOVE|int| drawception.com |Number of LOVE reactions this drawing recieved| 
|DUCK|int| drawception.com |Number of DUCK reactions this drawing recieved| 
|REACT|int| drawception.com | Total number of reactions this drawing recieved| 


## Analysis

I created a convolutional neural network to predict the total number of reactions an image would recieve.

### A Boar in the Matrix
![Figure: Mouseover text](/drawings/491204/QZVgV14ncW.png)


## Conclusion and Recommendation



## Sources

https://www.drawception.com