class Evento:
    def __init__(self, nome, data, local, descricao, organizador):
        self.nome = nome
        self.data = data
        self.local = local
        self.descricao = descricao
        self.organizador = organizador

    def adicionar_evento(self, evento):
        self.eventos.append(evento)

        return {
            "nome": self.nome,
            "data": self.data,
            "local": self.local,
            "descricao": self.descricao,
            "organizador": self.organizador
            }