Feature: Buscar un artista en last.fm y validar la fecha de su último release
    Scenario: Validar la fecha del último release de Michael Jackson
        Given el usuario está en el home page de last.fm
        When el usuario busca al artista "Michael Jackson"
        And presiona el link del primer resultado
        Then la fecha del último release debe ser "30 September 2025"