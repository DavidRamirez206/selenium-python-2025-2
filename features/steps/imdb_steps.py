from behave import given, when, then
from pages.imdb_home_page import ImdbHomePage
from pages.imdb_results_page import ImdbResultPage
from pages.imdb_movie_page import ImdbMoviePage

@given('el usuario está en el home page de imdb.com')
def step_home_page(context):
    context.driver.get("https://www.imdb.com/")
    context.imdb_home = ImdbHomePage(context.driver)

@when('el usuario busca la película "{movie_name}"')
def step_search_page(context, movie_name):
    context.imdb_home.search_movie(movie_name)
    context.imdb_result = ImdbResultPage(context.driver)

@when('presiona el nombre del primer resultado')
def step_press_movie(context):
    context.imdb_result.press_movie()
    context.imdb_movie = ImdbMoviePage(context.driver)


@then('el titulo de la película debe ser "{expected_title}" y la calificación de la película debe ser "{expected_rating}"')
def step_compare_title_and_rating(context, expected_title, expected_rating):
    actual_title = context.imdb_movie.get_Title()
    actual_rating = context.imdb_movie.get_rating()
    assert actual_title == expected_title, f"Expected title: {expected_title}, but got: {actual_title}"
    assert actual_rating == expected_rating, f"Expected rating: {expected_rating}, but got: {actual_rating}"
