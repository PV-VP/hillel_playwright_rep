from pydantic import BaseModel, Field

from models.base_pydantic import BaseResponseSchema


class CarPost(BaseResponseSchema):
    car_brand_id:int = Field(alias='carBrandId')
    car_model_id:int = Field(alias='carModelId')
    mileage: int | None

