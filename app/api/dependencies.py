from ..services.cat_service import CatService
from ..repositories.cat_repository import CatRepository

def cat_service() -> CatService:
    return CatService(CatRepository)