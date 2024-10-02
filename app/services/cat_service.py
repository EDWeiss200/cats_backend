from fastapi import HTTPException
from ..utils.repository import AbstractRepository
from ..schemas.schemas import CatAddSchema,CatReadSchema,CatBreed


class CatService:

    def __init__(self,cat_repo: AbstractRepository):
        self.cat_repo: AbstractRepository = cat_repo()

    async def add_cat(self,cat: CatAddSchema):

        cat_dict = cat.model_dump()

        cat_id = await self.cat_repo.add_one(cat_dict)
        return cat_id

    async def get_all_cats(self):

        cats = await self.cat_repo.find_all()
        return cats

    async def get_cat(self,cat_id):

        filters = [self.cat_repo.model.id == cat_id]
        cat = await self.cat_repo.find_filter(filters)
        return cat

    async def get_all_breed(self):

        collumn = self.cat_repo.model.breed
        breeds = await self.cat_repo.find_unique_value(collumn)
        new_breeds = []
        for i in breeds:
            new_breeds.append(i[0])

        catBreed = CatBreed(breeds=new_breeds)
        return catBreed

    async def get_cat_by_breed(self,breed):
        
        filters = [self.cat_repo.model.breed == breed]
        cats = await self.cat_repo.find_filter(filters)
        if cats:
            return cats
        else:
            raise HTTPException(status_code=404,detail='NOT FOUND CAT WITH SELECT BREED')


    async def patch_cat(self,cat:CatAddSchema,cat_id):
        
        cat_dict = cat.model_dump()

        cat = await self.cat_repo.update(cat_id,cat_dict)
        return cat

    async def delete_cat(self,cat_id):  

        cat_id = await self.cat_repo.delete_one(cat_id)
        return cat_id



    




