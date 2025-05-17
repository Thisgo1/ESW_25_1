from flask import Blueprint, jsonify
from extentions import db  # Importa do arquivo compartilhado
from models.feiras import Feira

feira_bp = Blueprint('feira', __name__, url_prefix='/feiras')

@feira_bp.route('', methods=['GET'])
def listar_feiras():
    feiras = Feira.query.all()
    return jsonify([f.to_dict() for f in feiras])

@feira_bp.route('', methods=['POST'])
def criar_feira():
    data = request.json
    try:
        feira = Feira.criar_feira(data)
        return jsonify(feira.to_dict()), 201
    except ValueError as e:
        abort(400, str(e))