from pydantic import BaseModel,EmailStr,Field
from enum import Enum
from typing import Optional


class Color(str,Enum):
    black = "black"
    white = "white"
    red = "red"
    green = "green"
    yellow =  "yellow"
    blue = "blue"
    pink = "pink"
    gray = "gray"
    brown = "brown"
    orange = "orange"

class Breed(str,Enum):
    ragdoll = 'ragdoll'
    persian = 'persian'
    sphynx = 'sphynx'
    abyssinian = 'abyssinian'
    oriental = 'oriental'
    siamese = 'siamese'





class CatReadSchema(BaseModel):
    id: int
    age: int
    breed: Breed
    color: Color
    description: str

    class Config:
        from_attributes = True

class CatAddSchema(BaseModel):
    age: int = Field(default=0,gt=0,description='Укажите возраст в месяцах,больше 0')
    breed: Breed
    color: Color
    description: str = Field(max_length=150,description='Описание не может быть больше 50 символов')


class CatBreed(BaseModel):
    breeds: list[Breed]






