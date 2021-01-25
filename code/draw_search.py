############################
# DRAWCEPTION IMAGE SEARCH #
############################

# Get user input
print("Enter a substring to search the captions.")
my_string = input().lower()

import pandas as pd
import PIL.Image

# Grab the data
drawception = pd.read_csv('../data/drawception_master.csv')

# Add a total reactions feature
drawception['REACT'] = drawception['LIKE']+drawception['HAHA']+drawception['WOW']+drawception['LOVE']+drawception['DUCK']

# Add image path column
drawception['img_path'] = ['../'+'/'.join(drawception.iloc[index,2].split('/')[3:6]) for index in range(len(drawception))]

# Get the index of the highest REACT image with the substring in a caption
index = drawception[
    drawception['pre_caption'].str.lower().str.contains(my_string)  
    |  drawception['post_caption'].str.lower().str.contains(my_string)
    ].sort_values(by='REACT', ascending=False).head(1).index.tolist()[0]

# Load and show Image
image = PIL.Image.open(drawception.iloc[index,15])
image.show()

# Output some info about the image
print(' ' + drawception.iloc[index,15])
print(' ' + drawception.iloc[index,0])
print(' ' + drawception.iloc[index,1])
print(' REACT: ', drawception.iloc[index,14])
print()
print(' https://drawception.com' + drawception.iloc[index,10])
