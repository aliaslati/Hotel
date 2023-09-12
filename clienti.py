
class Clienti:

    def __init__(self, nome, cognome, documento, pensione, mese):
        self.nome = nome
        self.cognome = cognome
        self.documento = documento
        self.pensione = pensione
        self.mese = mese

    def dettagli_cliente(self):
        # Restituisci le informazioni del lavoratore specificato.
        return f"Nome: {self.nome} {self.cognome}, Documento: {self.documento}, tipo di soggiorno: {self.pensione}"
