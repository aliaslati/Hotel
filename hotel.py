

class Hotel:
    capitale_iniziale = 100000

    def __init__(self, nome):
        self.nome = nome
        self.clienti = []
        self.lavoratori = []
        self.costi_fissi = 0
        self.costi_variabli = 0
        self.profitti = 0
        self.spesa_totale = 0

    def dettagli_hotel(self):
        return self.nome

    def aggiungi_lavoratore(self, lavoratore):
        try:
            personale_necessario, personale_mancante, personale_in_eccesso = self.calcola_personale_necessario()

            # Controlla se è necessario assumere ulteriori lavoratori
            if personale_mancante["cuochi"] > 0 or personale_mancante["camerieri"] > 0 \
                    or personale_mancante["lavapiatti"] > 0 or personale_mancante["tuttofare"] > 0:
                self.lavoratori.append(lavoratore)
                return f"Ora il numero di dipendenti nell'hotel è {len(self.lavoratori)}"
            else:
                raise Exception("Non è necessario assumere ulteriori lavoratori al momento.")
        except Exception as e:
            print(f"Errore: {e}")

    def rimuovi_lavoratore(self, lavoratore):
        try:
            if lavoratore in self.lavoratori:
                self.lavoratori.remove(lavoratore)
                return f"Ora il numero di dipendenti nell'hotel è {len(self.lavoratori)}"
            else:
                raise ValueError("Il lavoratore specificato non è presente nella lista dei lavoratori")
        except ValueError as errore:
            print(f"Errore: {errore}")

    def modifica_stipendio_lavoratore(self, lavoratore, nuovo_stipendio):
        # Verifica se il lavoratore è presente nell'elenco
        try:
            if lavoratore in self.lavoratori:
                lavoratore.set_stipendio(nuovo_stipendio)
                return f"{lavoratore.nome} {lavoratore.cognome} ha un nuovo stipendio"
            else:
                raise ValueError("Il lavoratore specificato non è presente nella lista dei lavoratori")
        except ValueError as err:
            print(f"Errore: {err}")

    def len_lavoratori(self):
        return len(self.lavoratori)

    def elenca_lavoratori(self):
        return [lavoratore.dettagli_lavoratore() for lavoratore in self.lavoratori]

    def totale_stipendi(self):
        stipendi = sum([lavoratore.get_stipendio() for lavoratore in self.lavoratori])
        return stipendi

    def aggiungi_cliente(self, cliente):
        self.clienti.append(cliente)

    def rimuovi_cliente(self, cliente):
        try:
            if cliente in self.clienti:
                self.clienti.remove(cliente)
                return f"Ora il numero di clienti nell'hotel è {len(self.clienti)}"
            else:
                raise ValueError("Il cliente specificato non è presente nella lista dei clienti")
        except ValueError as error:
            print(f"Errore: {error}")

    def len_clienti(self):
        return len(self.clienti)

    def spesa_cliente(self, cliente):
        # In base alla scelta della pensione il cliente ha una spesa diversa
        if cliente.pensione == "FB":
            pagamento = 30
            self.spesa_totale += pagamento
            return pagamento
        elif cliente.pensione == "HB":
            pagamento = 20
            self.spesa_totale += pagamento
            return pagamento
        elif cliente.pensione == "BB":
            pagamento = 14
            self.spesa_totale += pagamento
            return pagamento

    def calcola_personale_necessario(self):
        personale_necessario = {
            "cuochi": 0,
            "camerieri": 0,
            "lavapiatti": 0,
            "tuttofare": 0,
        }

        # In base al numero di cliente viene richiesto un determinato personale
        if len(self.clienti) <= 30:
            personale_necessario["cuochi"] = 2
            personale_necessario["camerieri"] = 1
            personale_necessario["lavapiatti"] = 1
            personale_necessario["tuttofare"] = 0
        elif 30 < len(self.clienti) <= 60:
            personale_necessario["cuochi"] = 3
            personale_necessario["camerieri"] = 2
            personale_necessario["lavapiatti"] = 1
            personale_necessario["tuttofare"] = 1
        elif len(self.clienti) > 60:
            personale_necessario["cuochi"] = 3
            personale_necessario["camerieri"] = 3
            personale_necessario["lavapiatti"] = 2
            personale_necessario["tuttofare"] = 1

        personale_presente = {
            "cuochi": 0,
            "camerieri": 0,
            "lavapiatti": 0,
            "tuttofare": 0,
        }

        # Conta quanti cuochi e camerieri si ha nell'elenco dei lavoratori dell'hotel
        for lavoratore in self.lavoratori:
            if lavoratore.ruolo == "cuoco":
                personale_presente["cuochi"] += 1
            elif lavoratore.ruolo == "cameriere":
                personale_presente["camerieri"] += 1
            elif lavoratore.ruolo == "lavapiatti":
                personale_presente["lavapiatti"] += 1
            elif lavoratore.ruolo == "tuttofare":
                personale_presente["tuttofare"] += 1

        personale_mancante = {
            "cuochi": max(0, personale_necessario["cuochi"] - personale_presente["cuochi"]),
            "camerieri": max(0, personale_necessario["camerieri"] - personale_presente["camerieri"]),
            "lavapiatti": max(0, personale_necessario["lavapiatti"] - personale_presente["lavapiatti"]),
            "tuttofare": max(0, personale_necessario["tuttofare"] - personale_presente["tuttofare"]),
        }

        personale_in_eccesso = {
            "cuochi": max(0, personale_presente["cuochi"] - personale_necessario["cuochi"]),
            "camerieri": max(0, personale_presente["camerieri"] - personale_necessario["camerieri"]),
            "lavapiatti": max(0, personale_presente["lavapiatti"] - personale_necessario["lavapiatti"]),
            "tuttofare": max(0, personale_presente["tuttofare"] - personale_necessario["tuttofare"]),
        }

        return personale_necessario, personale_mancante, personale_in_eccesso

    def guadagno_giornaliero_clienti(self):
        guadagno = 0
        for cliente in self.clienti:
            if cliente.pensione == "FB":
                guadagno += 30
            elif cliente.pensione == "HB":
                guadagno += 20
            elif cliente.pensione == "BB":
                guadagno += 14
        return guadagno

    def analisi_guadagni(self, mese):
        entrata_uscita = 0
        giorni = 1
        if mese == "giugno" or mese == "luglio" or mese == "agosto":
            for cliente in self.clienti:
                if cliente.mese == mese:
                    spesa = self.totale_stipendi()
                    guadagno = self.guadagno_giornaliero_clienti()
                    guadagno_rel = guadagno
                    while giorni != 30:
                        giorni += 1
                        guadagno += guadagno_rel
                        if guadagno > spesa:
                            entrata_uscita += (30 - giorni) * guadagno_rel
                            self.capitale_iniziale += entrata_uscita
                            return entrata_uscita
                    entrata_uscita = guadagno - spesa
                    self.capitale_iniziale += entrata_uscita
                    return entrata_uscita
        else:
            return entrata_uscita
