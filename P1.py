import pandas as pd
import matplotlib.pyplot as plt

#Load the IMDb dataset into a pandas DataFrame.
df=pd.read_csv(r"/Users/Garima/Downloads/IMDB-Movie-Data.csv")
print(df)

#First 5 rows of the dataset
print("First 5 rows of the dataset:",df.head(5))

#Overveiw of Columns
print("Overview of column data types")
print(df.info())
print("Missing values:")
print(df.isnull())

#Average runtime of movies
print("Average runtime of movies:",df["Runtime (Minutes)"].mean())

#Count the number of movies in each genre
print("Count the number of movies in each genre:")
print(df["Genre"].value_counts())

# The top 5 directors with the most movies
print("The top 5 directors with the most movies:")
a=df["Director"].value_counts()
print(a.head(5))

#The correlation coefficient between movie ratings and runtimes
print("The correlation coefficient between movie ratings and runtimes:")
print(df["Rating"].corr(df["Runtime (Minutes)"]))

#The 3 most frequent actors
print("The 3 most frequent actors:")
b=df["Actors"].value_counts()
print(b.head(3))

#Relationship between box office earnings and movie ratings
print("Relationship between box office earnings and movie ratings:")
print(df["Revenue (Millions)"].corr(df["Rating"]))

#Trends in average ratings over the years
print("Trends in average ratings over the years:")
print(df["Rating"].mean())

#The most common director-actor pairs
print("The most common director-actor pairs:")
df2=df[["Director","Actors"]]
print(df2)

#The relationship between the number of votes and movie ratings
print("The relationship between the number of votes and movie ratings")
print(df["Votes"].corr(df["Rating"]))

#A line plot showing the number of movies released each year
plt.title("Title & Year")
plt.plot(df["Title"], df["Year"])
plt.show()

#A histogram depicting the distribution of movie runtimes
x=df[["Runtime (Minutes)"]].copy()
plt.hist(x)
plt.title("Runtime (Minutes)")
plt.show()

#A histogram showcasing the distribution of movie ratings
y=df[["Rating"]].copy()
plt.hist(y)
plt.title("Rating")
plt.show()

#A histogram of movie budgets to understand their distribution
z=df[["Revenue (Millions)"]].copy()
plt.hist(z)
plt.title("Revenue (Millions)")
plt.show()

#A word cloud visualization using movie titles or keywords from descriptions
df.plot.bar(x="Title",y="Runtime (Minutes)")
plt.title("Title V/S Runtime (Minutes)")
plt.show()

#The average movie ratings over the years to identify trends
df.plot.bar(x="Rating",y="Year")
plt.title("Rating V/S Year")
plt.show()

#The trends of different genres over the years
df.plot.bar(x="Genre",y="Year")
plt.title("Genre V/S Year")
plt.show()

#The distribution of ratings for different genres
df.plot.bar(x="Genre",y="Rating")
plt.title("Genre V/S Rating")
plt.show()

#Any outliers in the movie runtime data
w=df.describe()
plt.hist(w)
plt.title("Outliers")
plt.show()

#Movie budgets relate to their earnings
df.plot.bar(x="Revenue (Millions)",y="Year")
plt.title("Revenue (Millions) V/S Year")
plt.show()

#Movie runtimes have changed over the years
df.plot.bar(x="Revenue (Millions)",y="Runtime (Minutes)")
plt.title("Revenue (Millions) V/S Runtime (Minutes)")
plt.show()

#Movie runtimes have changed over the years
df.plot.bar(x="Year",y="Runtime (Minutes)")
plt.title("Year V/S Runtime (Minutes)")
plt.show()

