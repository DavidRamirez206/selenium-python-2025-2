Feature: Buscar una película en imdb.com, validar el título de la película y su calificación
    Scenario: Validar el titulo y la calificación de la película Inception
        Given el usuario está en el home page de imdb.com
        When el usuario busca la película "El origen"
        And presiona el nombre del primer resultado
        Then el titulo de la película debe ser "El origen" y la calificación de la película debe ser "8.8"