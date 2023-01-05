from website.propriedade import Apartamento


class Corretor(object):
    def __init__(self, nome):
        self.nome = nome
        self.portfolio = []

    def display_portfolio(self):
        print(f"Portfólio do Corretor: {self.nome}")
        for apartamento in self.portfolio:
            apartamento.display()

    def anunciar(self):
        init_args = Apartamento.prompt_init()
        self.portfolio.append(Apartamento(**init_args))
