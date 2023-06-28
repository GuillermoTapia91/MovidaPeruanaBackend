from flask_restful import Resource, request
from models.usuario_model import UsuarioModel
from dtos.usuario_dto import UsuarioResponseDto, UsuarioRequestDto
from config import conexion

class UsuariosController(Resource):
    def post(self):
        data=request.json
        
        try:
            dto= UsuarioRequestDto()
            dataValidada= dto.load(data)
            nuevoUsuario = UsuarioModel(**dataValidada)
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()
            return{
                "message":"Usuario creado exitosamente"
            },201
        except Exception as err:
            conexion.session.rollback()
            return {
                "message":"Error al crear un usuario",
                "content": err.args
            },400
    
    def get(self):
        try:
            resultado= conexion.session.query(UsuarioModel).all()
            dto= UsuarioResponseDto(many=True)
            data=dto.dump(resultado)
            return{
                "content":data
            }
        except Exception as err:
            return{
                "message": "Error al Listar los usuarios",
                "content": err.args
            }
        
    def put(self):
        try:
            pass
        except Exception as err:
            return{
                "message":" Error al modificar el usuario"
            }
        
    def delete(self):
        try:
            pass
        except Exception as err:
            return{
                "message":"Error al eliminar el usuario"
            }
