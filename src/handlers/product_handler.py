import pandas as pd
import os
#from dotenv import load_dotenv
#load_dotenv()
PATH_CSV = os.getenv("PATH_CSV")

def read_prodotti():
    try:
        product_db = pd.read_csv(PATH_CSV)
        lista_dizionari = product_db.to_dict(orient='records')
        return lista_dizionari
    except FileNotFoundError:
        raise FileNotFoundError("Attenzione: il file magazzino.csv non è stato trovato!")
    except Exception as e:
        raise e
    
def aggiungi_prodotto_old(dati_ricevuti):
    try:
        db_nuova_riga = pd.DataFrame([dati_ricevuti])
        db_nuova_riga.to_csv(PATH_CSV, index=False, mode='a', header=False)
        return True
    except FileNotFoundError:
        raise FileNotFoundError("Attenzione: il file magazzino.csv non è stato trovato!")
    except Exception as e:
        raise e

def aggiungi_prodotto(dati_ricevuti):
    try:
        product_db = pd.read_csv(PATH_CSV)
        lista_dizionari = product_db.to_dict(orient='records')
        for dizionario in lista_dizionari:
            if dati_ricevuti["name"].lower() == dizionario["name"].lower():
                raise ValueError(f"Il prodotto {dati_ricevuti['name']} è già presente in magazzino!")
            else:
                continue
        lista_dizionari_completa = lista_dizionari + [dati_ricevuti]
        product_db_rinnovato = pd.DataFrame(lista_dizionari_completa)
        product_db_rinnovato.to_csv("data/products.csv", index=False)
        return True
    except FileNotFoundError:
        raise FileNotFoundError("Attenzione: il file magazzino.csv non è stato trovato!")
    except Exception as e:
        raise e
    
def aggiorna_prodotto(dati_ricevuti):
    try:
        product_db = pd.read_csv(PATH_CSV)
        lista_dizionari = product_db.to_dict(orient='records')
        check = False
        for dizionario in lista_dizionari:
            if dati_ricevuti["name"] == dizionario["name"]:
                dizionario["quantity"] = dati_ricevuti["quantity"]
                check = True
                break
        if check == False:
            raise ValueError(f"Il prodotto {dati_ricevuti['name']} non è presente in magazzino!")
        product_db_rinnovato = pd.DataFrame(lista_dizionari)
        product_db_rinnovato.to_csv("data/products.csv", index=False)
        return f"Il prodotto {dati_ricevuti['name']} è stato aggiornato!"
    except FileNotFoundError:
        raise FileNotFoundError("Attenzione: il file magazzino.csv non è stato trovato!")
    except Exception as e:
        raise e

def elimina_prodotto(prodotto):
    try:
        product_db = pd.read_csv(PATH_CSV)
        lista_dizionari = product_db.to_dict(orient='records')
        check = False
        for dizionario in lista_dizionari:
            if prodotto.lower() == dizionario["name"].lower():
                lista_dizionari.remove(dizionario)
                check = True
                break
        if check == False:
            raise ValueError(f"Il prodotto {prodotto} non è presente in magazzino!")
        product_db_rinnovato = pd.DataFrame(lista_dizionari)
        product_db_rinnovato.to_csv("data/products.csv", index=False)
        return f"Il prodotto {prodotto} è stato cancellato!"
    except FileNotFoundError:
        raise FileNotFoundError("Attenzione: il file magazzino.csv non è stato trovato!")
    except Exception as e:
        raise e

def conta_prodotti():
    try:
        product_db = pd.read_csv(PATH_CSV)
        lista_dizionari = product_db.to_dict(orient='records')
        if lista_dizionari:
            totale_prodotti = 0
            for dizionario in lista_dizionari:
                totale_prodotti += dizionario["quantity"]
        else:
            raise ("Il magazzino non contiene prodotti.")
        return totale_prodotti
    except Exception as e:
        raise e

def conta_prodotti_categoria(categoria):
    try:
        product_db = pd.read_csv(PATH_CSV)
        lista_dizionari = product_db.to_dict(orient='records')
        check = False
        if lista_dizionari:
            totale_prodotti = 0
            for dizionario in lista_dizionari:
                if dizionario["category"].lower() == categoria.lower():
                    totale_prodotti += dizionario["quantity"]
                    check=True
            if check == False:
                raise ValueError("Non hai inserito un categoria valida.")    
        else:
            raise ValueError("Il magazzino non contiene prodotti.")
        return totale_prodotti
    except Exception as e:
        raise e