from flask_restful import Resource, request
from models.establecimiento_model import EstablecimientoModel
from dtos.establecimiento_dto import EstablecimientoResponseDto

class EstablecimientoController(Resource):
    def post(Request):
        data = request.json
        
