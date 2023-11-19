import csv
import os
my_games=[]


class game:
    def __init__(self,name):
        self.name=name
        self.rating=0
        self.duration=0
        self.genre=""
        self.platforms=[]
    def add_rating(self,rating):
        self.rating=rating 
    def get_rating(self):
        if self.rating!=None:
            return self.rating
        print("Rating hasn't been added yet")
    def update_duration(self,duration):
        self.duration=duration
    def get_duration(self):
        if self.duration:
            return self.duration
        print("Duration Unknown")
    def update_platforms(self,*the_platforms):
        for platform in the_platforms:
            self.platforms.append(platform)
    def get_platforms(self):
        if self.platforms:
            return self.platforms
        print("Not available on any platforms, if you know the platforms you can add it by typing \" add platforms\"")
    def update_genre(self,genre):
        self.genre=genre
    def get_genre(self):
        if self.genre:
            return self.genre
        print("Genre Unkown, you can add it by typing \" add genre\"")
        # Print Bold and Italic Text
my_file=input("please enter the name of the file;\n Note: Please add the extension and make sure it's in csv \n")

with open(my_file,'r') as file:
    my_file=csv.DictReader(file)
    for row in my_file:
        init_games=game(row['Name'])
        init_games.update_platforms(row['platforms'])
        init_games.update_genre(row['genre'])
        init_games.add_rating(row['rating'])
        my_games.append(init_games)
#now to have my function which searches
def search_name(name):
    titles=[]
    for title in my_games:
        
        if title.name.lower()==name.lower():
            return title
        elif title.name[:len(name)].lower()==name.lower():
            titles.append(title.name)
    return titles
def search_genre(genre):
    titles=[]
    for title in my_games:
        try:
           if title.get_genre().lower()==genre.lower():
            title.append(title.name)
           elif title.genre[:len(genre)].lower()==genre.lower():
            titles.append(title.name)
        except:
           return "Genre Not Found, Please check the input or check the file"
    return titles

while True:
    print("Please enter the function you'd like to do")
    my_choice=input("Search Genre: SerGen \n Search name: title\n Quit to quit")
    my_choice.strip().lower()
    if my_choice=="sergen":
        genre=input("please enter the genre you'd like to search\n")
        genre.strip()
        print(search_genre(genre))
    elif my_choice=="title":
        title=input("Please enter the title or the first letters of the title\n")
        title.strip()
        print(search_name(title))
    elif my_choice=="quit":
        break
    else:
        print("Please enter a valid input!")
            
        
        