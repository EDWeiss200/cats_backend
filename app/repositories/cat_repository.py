from ..utils.repository import SQLAlchemyRepository

from ..models.models import Cat

class CatRepository(SQLAlchemyRepository):

    model = Cat
