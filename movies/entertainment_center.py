# Python 3 coding=utf-8

import fresh_tomatoes
from media import Movie


# Instantiate 6 movie titles
fifth_element = Movie(
    "The Fifth Element",
    '''In the colorful future, a cab driver unwittingly becomes the central figure
    in the search for a legendary cosmic weapon
    to keep Evil and Mr Zorg at bay.''',
    "https://images-na.ssl-images-amazon.com/images/M/MV5BZWFjYmZmZGQtYzg4YS00ZGE5LTgwYzAtZmQwZjQ2NDliMGVmXkEyXkFqcGdeQXVyNTUyMzE4Mzg@._V1_UY268_CR2,0,182,268_AL_.jpg",
    "https://youtu.be/fQ9RqgcR24g")

titanic = Movie(
    "Titanic",
    '''A seventeen-year-old aristocrat falls in love with a kind
    but poor artist aboard the luxurious,
    ill-fated R.M.S. Titanic.''',
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY1200_CR88,0,630,1200_AL_.jpg",
    "https://youtu.be/ZQ6klONCq4s")
    
labyrinth = Movie(
    "Labyrinth",
    '''A 16-year-old girl is given 13 hours to solve a
    labyrinth and rescue her
    baby brother when her wish for him to be taken
    away is granted by the Goblin King.''',
    "http://www.gstatic.com/tv/thumb/movieposters/9355/p9355_p_v8_ae.jpg",
    "https://youtu.be/XRcOZZDvMv4")

leon = Movie(
    "Leon: The Professional",
    '''Mathilda, a 12-year-old girl, is reluctantly taken in by Léon,
    a professional assassin,
    after her family is murdered.
    Léon and Mathilda form an unusual relationship, as she becomes
    his protégée and learns the assassins trade.''',
    "http://t3.gstatic.com/images?q=tbn:ANd9GcREMk53JJK7tX9ZUA_8WRlcMc6yI9CJeeLMOdxQaBCJd5RCInHZ", "https://youtu.be/aNQqoExfQsg")

goonies = Movie(
    "Goonies",
    '''In order to save their home from foreclosure,
    a group of misfits set out to find a
    pirates ancient valuable treasure.''',
    "http://t1.gstatic.com/images?q=tbn:ANd9GcQCU6KKioQ8YpG1SykOlK59aubmkSiJ2cLhbiX6R0yiRAqdRrpg",
    "https://youtu.be/5qA2s_Vh0uE")

harry_potter_prisoner = Movie(
    "Harry Potter and the Prisoner of Azkaban",
    '''It's Harry's third year at Hogwarts;
    not only does he have a new Defense Against the Dark Arts teacher,
    but there is also trouble brewing.
    Convicted murderer Sirius Black has escaped the Wizards'
    Prison and is coming after Harry.''',
    "http://www.gstatic.com/tv/thumb/movieposters/34483/p34483_p_v8_ap.jpg",
    "https://youtu.be/lAxgztbYDbs")

movies = [fifth_element, titanic, labyrinth, leon, goonies, harry_potter_prisoner]
# open html code to run webpage
fresh_tomatoes.open_movies_page (movies)
