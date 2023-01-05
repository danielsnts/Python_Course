# Criar classe Apartamento com atributos (título-endereço-preço-condomínio-IPTU-
# metros_quadrados-quartos-banheiros-vagas)
class Apartamento(object):
    def __init__(self, titulo, endereco, preco, condominio, iptu, metros_quadrados, quartos, banheiros, vagas):  # Toda
        # s as variaveis da classe Apartamento
        self.titulo = titulo
        self.endereco = endereco
        self.preco = preco
        self.condominio = condominio
        self.iptu = iptu
        self.metros_quadrados = metros_quadrados
        self.quartos = quartos
        self.banheiros = banheiros
        self.vagas = vagas

# Criaar Método display para projetar os dados da propriedade
    def display(self):
        print()
        print("DETALHES DA PROPRIEDADE")
        print("=======================")
        print(f"{self.titulo}")
        print(f"Endereço da propriedade: {self.endereco}")
        print(f"Preço: R$ {self.preco}")
        print(f"Condomínio: {self.condominio}")
        print(f"IPTU: R$ {self.iptu}")
        print(f"Metros quadrados: {self.metros_quadrados} m^2")
        print(f"Quartos: {self.quartos}")
        print(f"Banheiro: {self.banheiros}")
        print(f"Vagas: {self.vagas}")
        print("=======================")
        print()

# Criar Método prompt_init() para completar dados
    def prompt_init():  # Estático, inerente a classe
        return dict(titulo=input("Insira o título do seu anúncio "),
                    endereco=input("Qual é o endereço do seu apartamento: "),
                    preco=float(input("Qual é o preço? ")),
                    condomínio=input("Qual é o valor do condomínio"),
                    iptu=float(input("Qual o valor do IPTU? ")),
                    metros_quadrados=input("Quantos metros quadrados tem"),
                    quartos=input("Quantos quartos têm? "),
                    banheiros=input("Quantos banheiros? "),
                    vagas=input("Quantas vagas de garagem? ")
                    )
    prompt_init = staticmethod(prompt_init)  # Definindo esse método como método estático
