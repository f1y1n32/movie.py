class Movie:
    def __init__(self,title,director,duration,watched = False,rating =None ):
        self.title = title
        self.director = director
        self.duration = duration
        self.rating = rating
        self.watched = watched
      
    def __str__(self): 
        status = "Watched" if self.watched else "Not watched yet"
        rating_display = self.rating if self.watched and self.rating is not None else "N/A"
        return f"Movie: {self.title}, directed by {self.director}, Duration: {self.duration} minutes, Status: {status}, Rating: {rating_display}"

    def mark_as_watched(self, rating):
        if 0 <= rating <= 10:
            self.watched = True
            self.rating = rating
        else:
            print("Rating must be between 0 and 10.")

    def is_long_movie(self):
        return self.duration > 135

    def update_rating(self, new_rating):
        if self.watched:
            if 0 <= new_rating <= 10:
                self.rating = new_rating
            else:
                print("New rating must be between 0 and 10.")
        else:
            print("Can't update rating — movie has not been watched yet.")

    def reset_watch_status(self):
        self.watched = False
        self.rating = None
        
movie1 = Movie("Interstellar", "Christopher Nolan", 169)
movie2 = Movie("The Lion King", "Roger Allers", 88)
movie3 = Movie("Avengers: Endgame", "Anthony Russo", 181)


print("Before watching:")
print(movie1)
print(movie2)
print(movie3)
print()

# Mark some as watched
movie1.mark_as_watched(9)
movie3.mark_as_watched(8.5)

# Update rating
movie1.update_rating(9.5)

# Check if a movie is long
print(f"\nIs '{movie1.title}' a long movie? {movie1.is_long_movie()}")
print(f"Is '{movie2.title}' a long movie? {movie2.is_long_movie()}")

# Reset one movie's watch status
movie3.reset_watch_status()

# Print again after changes
print("\nAfter updates:")
print(movie1)
print(movie2)
print(movie3)

