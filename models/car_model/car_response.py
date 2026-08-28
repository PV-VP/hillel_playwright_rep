from pydantic import Field
from datetime import datetime
from models.base_pydantic import BaseResponseSchema

# {
#     "id": 94,
#     "carBrandId": 1,
#     "carModelId": 1,
#     "initialMileage": 11,
#     "updatedMileageAt": "2021-05-17T15:26:36.000Z",
#     "mileage": 111,
#     "brand": "Audi",
#     "model": "TT",
#     "logo": "audi.png"
# },


class CarResponse(BaseResponseSchema):
    id: int
    car_brand_id:int  = Field(alias='carBrandId')
    carModelId: int
    initialMileage: int
    updatedMileageAt: datetime
    mileage: int
    brand: str
    model: str
    logo: str