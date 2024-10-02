from fastapi import APIRouter,Depends,HTTPException,Response,Cookie,Request
from .dependencies import cat_service
from schemas.schemas import CatAddSchema,Breed
from services.cat_service import CatService
from fastapi_cache.decorator import cache


router = APIRouter(
    tags=["cats"],
    prefix="/cats"
)

@router.post('')
async def add_cat(
    cat: CatAddSchema,
    cat_service: CatService = Depends(cat_service)
):
    cat_id = await cat_service.add_cat(cat)
    return{'id':cat_id}


@router.get('/breeds')
async def get_all_breeds(
    cat_service: CatService = Depends(cat_service)
):
    cats = await cat_service.get_all_breed()
    return cats

@router.get('/breeds/{breed}')
async def get_cat_by_breed(
    breed: Breed,
    cat_service: CatService = Depends(cat_service)
):
    cats = await cat_service.get_cat_by_breed(breed)
    return cats

@router.get('/{id}')
async def get_cat(
    id: int,
    cat_service: CatService = Depends(cat_service)
):
    cat = await cat_service.get_cat(id)
    return cat

@router.patch('/{id}')
async def patch_cat(
    id: int,
    cat:CatAddSchema,
    cat_service: CatService = Depends(cat_service)
):
    cat = await cat_service.patch_cat(cat,id)
    return cat

@router.delete('/{id}')
async def patch_cat(
    id: int,
    cat_service: CatService = Depends(cat_service)
):
    cat_id = await cat_service.delete_cat(id)
    return {'delete_cat':cat_id}


@router.get('')
@cache(expire=30)
async def get_all_cat(
    cat_service: CatService = Depends(cat_service)
):
    cats = await cat_service.get_all_cats()
    return cats




