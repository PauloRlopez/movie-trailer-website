import media
import fresh_tomatoes

Matrix = media.Movie(
"Matrix",
"A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
"https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
"https://www.youtube.com/watch?v=m8e-FF8MsqU")


Thor_ragnarok = media.Movie(
"Thor: Ragnorok",
"Imprisoned, the mighty Thor finds himself in a lethal gladiatorial contest against the Hulk, his former ally. Thor must fight for survival and race against time to prevent the all-powerful Hela from destroying his home and the Asgardian civilization.",
"https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
"https://www.youtube.com/watch?v=v7MGUNV8MxU"
)

Robocop = media.Movie("Robocop",
"In 2028 Detroit, when Alex Murphy - a loving husband, father and good cop - is critically injured in the line of duty, the multinational conglomerate OmniCorp sees their chance for a part-man, part-robot police officer.",
"https://upload.wikimedia.org/wikipedia/en/b/b1/Robocop_poster.jpg",
"https://www.youtube.com/watch?v=jBeSfnIT_Bw"
)

Justice_league = media.Movie("Justice League",
"Fueled by his restored faith in humanity and inspired by Superman's selfless act, Bruce Wayne enlists the help of his newfound ally, Diana Prince, to face an even greater enemy.",
"https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",
"https://www.youtube.com/watch?v=lQpjPTCaCGk"
)


Alien_covenant = media.Movie(
"Aline Convenant",
"The crew of a colony ship, bound for a remote planet, discover an uncharted paradise with a threat beyond their imagination, and must attempt a harrowing escape.",
"https://upload.wikimedia.org/wikipedia/en/3/33/Alien_Covenant_Teaser_Poster.jpg",
"https://www.youtube.com/watch?v=H0VW6sg50Pk"
)


Valerian = media.Movie(
"Valerian",
"A dark force threatens Alpha, a vast metropolis and home to species from a thousand planets. Special operatives Valerian and Laureline must race to identify the marauding menace and safeguard not just Alpha, but the future of the universe.",
"https://upload.wikimedia.org/wikipedia/en/0/07/Valerian_and_the_City_of_a_Thousand_Planets.jpg",
"https://www.youtube.com/watch?v=vZsG7WJVZv8"
)

movies = [Matrix, Thor_ragnarok, Robocop, Justice_league, Alien_covenant, Valerian]
fresh_tomatoes.open_movies_page(movies)
