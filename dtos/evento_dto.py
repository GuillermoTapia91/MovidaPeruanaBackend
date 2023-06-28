from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.eventos_model import EventoModel

class EventoResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        model= EventoModel
        include_fk=True
