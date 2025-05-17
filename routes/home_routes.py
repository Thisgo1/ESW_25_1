from flask import Blueprint

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return {
        "message": "Bem-vindo ao Sistema de Feiras",
        "endpoints": {
            "feiras": "/feiras",
            "expositores": "/expositores" 
        }
    }