import fresh_tomatoes
import media

"""Defines the instances of the class Movie"""
inside_out = media.Movie(
    "Inside Out",
    "American 3D computer-animated buddy fantasy "
    "comedy-drama adventure film",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcTtZdvrahQxfjGkSBJCS-uiZKUfJNH4ddsqgCbV5oFkQiQ-tszE",  # noqa
    "https://youtu.be/seMwpP0yeu4")
despicable = media.Movie(
    "Despicable Me",
    "Meet The Minions",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcStk75A_FacVc2kXVb8vdTAU6x-fmRjV2X0-6yxHF5iksQmzKwB",  # noqa
    "https://youtu.be/j2bAEnBQWvM")
finding_nemo = media.Movie(
    "Finding Nemo",
    "Nemo, a young clownfish is captured and taken to a dentist's ",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcSoStMb2jeN136xQhf2g3ROpTB9Dker9IlfGbMbwYB3ruC9VcOj",  # noqa
    "https://youtu.be/nui7akStMfU")
up = media.Movie(
    "Up",
    "Seventy-eight year old Carl Fredricksen travels to Paradise Falls "
    "in his home",
    "http://www.gstatic.com/tv/thumb/movieposters/190662/p190662_p_v8_aq.jpg",  # noqa
    "https://youtu.be/qas5lWp7_R0")
avatar = media.Movie(
    "Avatar",
    "Fictional movie",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",  # noqa
    "https://youtu.be/d1_JBMrrYw8")
shrek = media.Movie(
    "Shrek",
    "The Shrek franchise from DreamWorks Animation, based on "
    "William Steig's picture book Shrek!",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcS_OkJKQ6ZpDV_xhC0L9zyHEcKMlV9x3Q30LF6MOE0nV1U6r09p",  # noqa
    "https://youtu.be/IlsMVMENn_0")

# prints the storyline of the movie 'up'
# print(up.storyline)

# appending movies into a list
list_of_movies = [inside_out, despicable, finding_nemo, up, avatar, shrek]
# calling the external rendering function 'open_movies_page'
fresh_tomatoes.open_movies_page(list_of_movies)
