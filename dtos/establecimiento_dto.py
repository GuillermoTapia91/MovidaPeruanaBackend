from models.establecimiento_model import EstablecimientoModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class EstablecimientoResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        model= EstablecimientoModel
        include_fk=True