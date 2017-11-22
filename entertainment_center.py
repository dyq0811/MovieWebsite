import fresh_tomatoes
import media

#The following are specific information for each movie.
interstellar = media.Movie(
"Interstellar",
"A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",# flake8: noqa
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",# flake8: noqa
"https://www.youtube.com/watch?v=zSWdZVtXT7E")

passengers = media.Movie(
"Passengers",
"The story depicts three people who are awakened some 90 years too soon from an induced hibernation on a spaceship bound for a new planet.",# flake8: noqa
"https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4MjU3MDIzOF5BMl5BanBnXkFtZTgwMjM2MzY2MDI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",# flake8: noqa
"https://www.youtube.com/watch?v=7BWWWQzTpNU")

hidden_figures = media.Movie(
"Hidden Figures",
"The story of a team of female African-American mathematicians who served a vital role in NASA during the early years of the U.S. space program.",# flake8: noqa
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjQxOTkxODUyN15BMl5BanBnXkFtZTgwNTU3NTM3OTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",# flake8: noqa
"https://www.youtube.com/watch?v=RK8xHq6dfAo")

the_martian = media.Movie(
"The Martian",
"An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive.",# flake8: noqa
"https://images-na.ssl-images-amazon.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",# flake8: noqa
"https://www.youtube.com/watch?v=Ue4PCI0NamI")

allegiant = media.Movie(
"Allegiant",
"After the earth-shattering revelations of Insurgent, Tris must escape with Four beyond the wall that encircles Chicago, to finally discover the shocking truth of the world around them.",# flake8: noqa
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjEyOTI3NDQwN15BMl5BanBnXkFtZTgwNjExOTIwODE@._V1_SY1000_CR0,0,647,1000_AL_.jpg",# flake8: noqa
"https://www.youtube.com/watch?v=tE8LEPSTK6A")

the_hunger_games = media.Movie(
"The Hunger Games",
"As the war of Panem escalates to the destruction of other districts, Katniss Everdeen, the reluctant leader of the rebellion, must bring together an army against President Snow, while all she holds dear hangs in the balance.",# flake8: noqa
"https://images-na.ssl-images-amazon.com/images/M/MV5BNjQzNDI2NTU1Ml5BMl5BanBnXkFtZTgwNTAyMDQ5NjE@._V1_SY1000_CR0,0,657,1000_AL_.jpg",# flake8: noqa
"https://www.youtube.com/watch?v=EAzGXqJSDJ8")



movies = [interstellar, passengers, hidden_figures, the_martian, allegiant, the_hunger_games]
fresh_tomatoes.open_movies_page(movies)
