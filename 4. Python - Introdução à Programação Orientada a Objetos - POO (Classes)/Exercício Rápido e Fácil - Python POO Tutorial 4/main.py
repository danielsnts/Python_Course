from website.usuário import Corretor
from website.propriedade import Apartamento


def main():
    correto_1 = Corretor('Luciano')
    correto_1.anunciar()
    correto_1.anunciar()
    correto_1.display_portifolio()


if __name__ == '__main__':
    main()
