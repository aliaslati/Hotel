
class Lavoratori:

    def __init__(self, nome, cognome, ruolo, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.ruolo = ruolo
        self.__stipendio = stipendio

    def dettagli_lavoratore(self):
        # Restituisci le informazioni del lavoratore specificato.
        return f"Nome: {self.nome} {self.cognome}, Ruolo: {self.ruolo}"

    def get_stipendio(self):
        return self.__stipendio

    def set_stipendio(self, nuovo_stipendio):
        self.__stipendio = nuovo_stipendio
