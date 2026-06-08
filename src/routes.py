from flask import Blueprint, request, jsonify
from src.handlers.product_handler import read_prodotti
from src.handlers.product_handler import aggiungi_prodotto
from src.handlers.product_handler import aggiorna_prodotto
from src.handlers.product_handler import elimina_prodotto
from src.handlers.product_handler import conta_prodotti
from src.handlers.product_handler import conta_prodotti_categoria
import pandas as pd

magazzino_bp = Blueprint("magazzino", __name__, url_prefix='/magazzino')

@magazzino_bp.route('/read', methods=['GET'])
def read_db(): 
    try:
        lista_dizionari = read_prodotti()
        return jsonify({"Message": "Success", "Data": lista_dizionari}), 200
    except FileNotFoundError as e:
        return jsonify({'Error': str(e)}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@magazzino_bp.route('/add', methods=['POST'])
def add_db():
    try:
        dati_ricevuti = request.get_json()
        for field in ["name", "quantity"]:
            if field not in dati_ricevuti:
                return jsonify({"Errore": f"Parametro {field} mancante."}), 400
            else:
                risultato = aggiungi_prodotto(dati_ricevuti)
                if risultato:
                    return jsonify({"Message": "Success"}), 201
    except FileNotFoundError as e:
        return jsonify({'Error': str(e)}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
        
@magazzino_bp.route('/update', methods=['PUT'])
def update_product_db():
    try:
        dati_ricevuti = request.get_json()
        for field in ["name", "quantity"]:
            if field not in dati_ricevuti:
                return jsonify({"Errore": f"Parametro {field} mancante."}), 400
            else:
                risultato = aggiorna_prodotto(dati_ricevuti)
                if risultato:
                    return jsonify({"Message": risultato}), 201
    except FileNotFoundError as e:
        return jsonify({'Error': str(e)}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@magazzino_bp.route('/delete/<string:prodotto>', methods=['DELETE'])
def delete_product_db(prodotto):
    try:
        risultato = elimina_prodotto(prodotto)
        if risultato:
            return jsonify({"Message": risultato}), 200
        else:
            return jsonify({"Errore": f"Prodotto {prodotto} non presente in magazzino."}), 404
    except FileNotFoundError as e:
        return jsonify({'Error': str(e)}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@magazzino_bp.route('/total-count', methods=['GET'])
def count_product_db():
    try:
        risultato = conta_prodotti()
        if risultato:
            return jsonify({"Message": f"Il magazzino contiene {risultato} prodotti."}), 200
    except FileNotFoundError as e:
        return jsonify({'Error': str(e)}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
@magazzino_bp.route('/count-categoria', methods=['GET'])
def count_product_categoria_db():
    try:
        categoria = request.args.get('categoria', default=None, type=str)
        if not categoria:
            risultato = conta_prodotti()
            if risultato:
                return jsonify({"Message": f"Il magazzino contiene {risultato} prodotti."}), 200
        try:
            risultato_bis = conta_prodotti_categoria(categoria)
            if risultato_bis:
                return jsonify({"Message": f"Il magazzino contiene {risultato_bis} prodotti nella categoria {categoria}."}), 200
        except Exception as e:
            return jsonify({'Error': str(e)}), 400
    except FileNotFoundError as e:
        return jsonify({'Error': str(e)}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}), 500