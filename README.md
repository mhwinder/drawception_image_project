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
|bin|int| drawception.com | Bin for reactions 0, 1-3, 4+| 


## Analysis

I made a Convolutional Neural Network to predict the reactions. Because of the large amount of data I needed to create a generator function to load the images in batches and convert them to numpy arrays. I also reduced the image resolution by half, to speed up the processing. I tried modeling in two different ways: doing a regression on the REACT variable, and a classification on the bin variable. Each network was constructed in the same way and only the output layer was changed. The most successful model took 8 hours to fit, had 2 convolution layers, 2 dense layers and 2 dropout layers.

### A Boar in the Matrix
![Figure: Mouseover text](/drawings/491204/QZVgV14ncW.png)


## Conclusion and Recommendation

Neither model performed well. Both models predicted 0 reactions almost exclusivly with only slight variations. The slight variations may have been marginally better but art is subjective and the metrics were terrible. The classification model predicted bin 0, accuracy 28.7%, which was actually worse than the baseline which was bin 1, 50.3%. The regression model had an r2 score of -0.44. The model would have benefitted greatly from more convolution layers and processing power to compute them.

I also had hoped to use the caption information and NLP to generate captions on images. I did use the captions in a script to find interesting images from the dataset. It takes a string and locates all the images that contain the string in their captions and it displays the one with the highst reaction total.

## Sources

https://www.drawception.com