import pandas as pd

# Data for top 10 similar movies for "The Lord of the Rings: The Fellowship of the Ring"
lotr_data = {
    "Title": [
        "The Lord of the Rings: The Two Towers", "The Lord of the Rings: The Return of the King",
        "Dark Sky Blue", "Gladiator", "Avengers: Endgame", "Kantara", "Kingdom of Heaven",
        "The Revenant", "Letters from Iwo Jima", "The Wilderness Night"
    ],
    "Genres": [
        "Adventure, Drama", "Adventure, Drama", "Drama", "Action, Drama, Historical", 
        "Action, Sci-Fi", "Drama", "Action, Historical", "Adventure, Drama", 
        "War, Drama", "Drama, Mystery"
    ],
    "Actors": [
        "Elijah Wood, Ian McKellen, others", "Viggo Mortensen, Ian McKellen, others", 
        "Unknown", "Russell Crowe, Joaquin Phoenix", "Robert Downey Jr., Chris Evans", 
        "Unknown", "Orlando Bloom, Eva Green", "Leonardo DiCaprio, Tom Hardy", 
        "Ken Watanabe, Kazunari Ninomiya", "Unknown"
    ],
    "Average Rating": [8.8, 9.0, 8.8, 8.5, 8.4, 8.4, 7.2, 8.0, 7.9, 7.8]
}

# Data for top 10 similar movies for "Inception"
inception_data = {
    "Title": [
        "Avengers: Infinity War", "Mad Max: Fury Road", "Iron Man", 
        "Edge of Tomorrow", "Star Trek", "X-Men: Days of Future Past", 
        "Captain America: The Winter Soldier", "Star Wars: Episode VII - The Force Awakens", 
        "Serenity", "Star Trek Into Darkness"
    ],
    "Genres": [
        "Action, Sci-Fi", "Action, Adventure", "Sci-Fi, Adventure", 
        "Sci-Fi, Action", "Sci-Fi, Action", "Sci-Fi, Action", 
        "Sci-Fi, Action", "Sci-Fi, Fantasy", "Sci-Fi, Action", "Sci-Fi, Action"
    ],
    "Actors": [
        "Robert Downey Jr., Chris Evans", "Tom Hardy, Charlize Theron", 
        "Robert Downey Jr., Gwyneth Paltrow", "Tom Cruise, Emily Blunt", 
        "Chris Pine, Zachary Quinto", "James McAvoy, Michael Fassbender", 
        "Chris Evans, Scarlett Johansson", "Daisy Ridley, John Boyega", 
        "Nathan Fillion, Gina Torres", "Chris Pine, Zachary Quinto"
    ],
    "Average Rating": [8.4, 8.1, 7.9, 7.9, 7.9, 7.9, 7.8, 7.8, 7.8, 7.7]
}

# Data for top 10 similar movies for "Shrek"
shrek_data = {
    "Title": [
        "Shrek 2", "Shrek Forever After", "Shrek the Third", 
        "Puss in Boots: The Last Wish", "Fantastic Mr. Fox", "Zootopia", 
        "Soul", "Isle of Dogs", "Tangled", "Wreck-It Ralph"
    ],
    "Genres": [
        "Adventure, Animation, Comedy", "Adventure, Animation, Comedy", 
        "Adventure, Animation, Comedy", "Adventure, Animation, Comedy", 
        "Adventure, Animation, Comedy", "Adventure, Animation, Comedy", 
        "Adventure, Animation, Comedy", "Adventure, Animation, Comedy", 
        "Adventure, Animation, Comedy", "Adventure, Animation, Comedy"
    ],
    "Actors": [
        "Mike Myers, Eddie Murphy", "Mike Myers, Cameron Diaz", 
        "Mike Myers, Cameron Diaz", "Antonio Banderas, Salma Hayek", 
        "George Clooney, Meryl Streep", "Ginnifer Goodwin, Jason Bateman", 
        "Jamie Foxx, Tina Fey", "Bryan Cranston, Edward Norton", 
        "Mandy Moore, Zachary Levi", "John C. Reilly, Jack McBrayer"
    ],
    "Average Rating": [7.3, 6.3, 6.1, 7.9, 7.9, 8.0, 8.0, 7.8, 7.7, 7.7]
}

# Creating DataFrames for each movie's top 10 similar movies
lotr_df = pd.DataFrame(lotr_data)
inception_df = pd.DataFrame(inception_data)
shrek_df = pd.DataFrame(shrek_data)

# Saving each DataFrame to a separate sheet in an Excel file
with pd.ExcelWriter('movie_similarity_analysis.xlsx') as writer:
    lotr_df.to_excel(writer, sheet_name='LOTR Similarity', index=False)
    inception_df.to_excel(writer, sheet_name='Inception Similarity', index=False)
    shrek_df.to_excel(writer, sheet_name='Shrek Similarity', index=False)

'/mnt/data/movie_similarity_analysis.xlsx'
