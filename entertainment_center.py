# entertainment_center.py executes code found in the following files
import media
import fresh_tomatoes

# The following 6 instances are movies to be displayed on the web-site.
beavis_and_butthead = media.Movie("Beavis and Butthead do America",
                                  "Beavis and Butthead lose their television",
                                  "http://www.gstatic.com/tv/thumb/movieposters/18853/p18853_p_v8_aa.jpg",  # noqa
                                  "https://youtu.be/jRnVQ4NBXko")

fight_club = media.Movie("Fight Club",
                         "Ed Norton confronts an existential crisis with a bare knuckle fighting ring",  # noqa
                         "http://www.gstatic.com/tv/thumb/movieposters/23069/p23069_p_v8_ad.jpg",  # noqa
                         "https://youtu.be/SUXWAEX2jlg")

tron_legacy = media.Movie("Tron: Legacy",
                          "Some guy finds his dad in an alternative digital \
                          universe",
                          "http://t1.gstatic.com/images?q=tbn:ANd9GcSchLICLsn0n_GlVBYmaIZjwcYDuqvb1fg4nVvr8WAh3FN8EqfY",  # noqa
                          "https://youtu.be/L9szn1QQfas")

zombie_land = media.Movie("Zombie Land",
                          "Woody Harrilson kills lots of zombies with that kid \
                          from social network, and some other people",
                          "http://www.gstatic.com/tv/thumb/movieposters/3532040/p3532040_p_v8_ae.jpg",  # noqa
                          "http://www.youtube.com/watch?v=pYVQgsYb9gY")

war_games = media.Movie("War Games",
                        "Some hacker kid saves the world by playing \
                        tic-tac-toe",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcTsqaGEcvep6oEDEPWXHihceN4VWNH7n9O9gKMaDyTJeWFdlN3r",  # noqa
                        "https://youtu.be/tAcEzhQ7oqA")

the_matrix = media.Movie("The Matrix",
                         "You know what this movie is about",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle",  # noqa
                         "https://youtu.be/vKQi3bBA1y8")

movies = [war_games, the_matrix, beavis_and_butthead, fight_club, tron_legacy,
          zombie_land, ]
fresh_tomatoes.open_movies_page(movies)
