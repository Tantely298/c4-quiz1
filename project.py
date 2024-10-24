#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:14:17 2024

@author: astrostudent1
"""

import pandas as pd
df = pd.read_csv("movie_dataset.csv")
print(df.head())
print(df.info())

#The highest rated movie 
highest_rated_index = df['Rating'].idxmax()
highest_rated_movie = df.loc[highest_rated_index]
print('The highest rated movie is:', highest_rated_movie)

#The average revenue 
average_revenue = df['Revenue (Millions)'].mean()
print('The average revenue is:', average_revenue)

#Average Revenue (2015-2017)
filtered_df = df[(df['Year']>=2015) & (df['Year']<=2017)]
average_revenue = filtered_df['Revenue (Millions)'].mean()
print('Average Revenue (2015-2017):', average_revenue)

#Number pf movies released in 2016
print(df.columns)
movies_2016 = df[df['Year'] == 2016]
num_movies_2016 = movies_2016.shape[0]
print("Number pf movies released in 2016:", num_movies_2016)

#Number of movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']
num_nolan_movies = len(nolan_movies)
print('Number of movies directed by Christopher Nolan :', num_nolan_movies)

#The number of movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= 8.0]
count_high_rated_movies = high_rated_movies.shape[0]
print('The number of movies with a rating of at least 8.0 is:', count_high_rated_movies)

#VThe median rating of movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']
median_rating = nolan_movies['Rating'].median()
print('The median rating of movies directed by Christopher Nolan is:', median_rating)

#The year with the highest average rating is
average_ratings = df.groupby('Year')['Rating'].mean()
highest_avg_year = average_ratings.idxmax()
highest_avg_rating = average_ratings.max()
print('The year with the highest average rating is:', highest_avg_year , 'with an average rating of' , highest_avg_rating )

#The percentage increase in the number of movies made between 2006 and 2016
count_2006 = df[df['Year'] == 2006].shape[0]
count_2016 = df[df['Year'] == 2016].shape[0]
if count_2006 > 0:
    percentage_increase = ((count_2016 - count_2006) / count_2006) * 100
else:
    percentage_increase = float('inf')
print('The percentage increase in the number of movies made between 2006 and 2016 is:', percentage_increase )

#The most common actor in all the movies
actors_split = df['Actors'].str.split(', ') 
exploded_actors = actors_split.explode()
actor_counts = exploded_actors.value_counts()
most_common_actor = actor_counts.idxmax()
most_common_count = actor_counts.max()
print('The most common actor in all the movies is:', most_common_actor , 'with', most_common_count )

#Unique genre 
genres_split = df['Genre'].str.split(',')
exploded_genres = genres_split.explode()
exploded_genres = exploded_genres.str.strip()
unique_genres = exploded_genres.unique()
num_unique_genres = len(unique_genres)
print('There are', num_unique_genres )


