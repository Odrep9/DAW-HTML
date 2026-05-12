class Movie:

# Método construtor da classe, chamado automaticamente quando e criado um novo objeto Movie
    def __init__ (self, title, year=None):
        # Guarda o título do filme no objeto
        self.title = title
        # Guarda o ano do filme no objeto
        self.year = year