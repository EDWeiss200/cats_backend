from typing import Annotated
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import Boolean, ForeignKey, Integer, String, func, select,Column,MetaData
from schemas.schemas import CatReadSchema

intpk = Annotated[int, mapped_column(index = True,primary_key=True)]


metadata = MetaData()

class Base(DeclarativeBase):
    ...

class Cat(Base):
    __tablename__ = 'cats'
    id: Mapped[intpk]
    age: Mapped[int]
    breed: Mapped[str]
    color: Mapped[str]
    description: Mapped[str] 

    def to_read_model(self)->CatReadSchema:
        return CatReadSchema(
            id = self.id,
            age=self.age,
            breed = self.breed,
            color=self.color,
            description=self.description
        )

    