from studente import Studente

ins_nome=input("inserisci il nome dello studente: ")
ins_classe=input("inserisci la classe dello studente:: ")

studente1 = Studente(ins_nome, ins_classe)
messaggio=input("vuoi aggiungere de voti allo studente?? si/no: ")
if messaggio == "si":
    while True:
        voto=int(input(aggiung un voto: ))
        aggiungi_voto()
        studente1.aggiungi_voto(voto)
        messaggio1=input("devi inserire unaltro voto?? si/no: ")
        if messaggio1 != "si":
            break