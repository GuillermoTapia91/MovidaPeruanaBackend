from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.usuario_model import UsuarioModel

class UsuarioResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        model = UsuarioModel
        
class UsuarioRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model= UsuarioModel