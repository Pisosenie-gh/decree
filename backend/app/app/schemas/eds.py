from itertools import count
from typing import Optional, List



from pydantic import BaseModel, Field, validator
from datetime import date, datetime
from .eds_provider_type import EdsProviderTypeForModels


from datetime import datetime, timezone


# Shared properties


class EdsBase(BaseModel):
    signDate: datetime
    certStartDate: datetime
    certEndDate: datetime
    certOwner: str
    PUID: str
    cert: str
    content: str
    signedFieldsSequence: list
    signedFilesIdSequence: List[int]
    providerType: EdsProviderTypeForModels




# Properties to receive on item creation
class EdsCreate(EdsBase):
    signDate: datetime
    certStartDate: datetime
    certEndDate: datetime
    certOwner: str
    PUID: str
    cert: str
    content: str
    signedFieldsSequence: list
    signedFilesIdSequence: List[int]
    providerType: EdsProviderTypeForModels
    
    class Config:
        orm_mode = True



# Properties to receive on item update
class EdsUpdate(EdsBase):
    signDate: datetime
    certStartDate: datetime
    certEndDate: datetime
    certOwner: str
    PUID: str
    cert: str
    content: str
    signedFieldsSequence: list
    signedFilesIdSequence: List[int]
    providerType: EdsProviderTypeForModels



    class Config:
        orm_mode = True
   




# Properties shared by models stored in DB
class EdsInDBBase(EdsBase):
    id: int
    signDate: datetime
    certStartDate: datetime
    certEndDate: datetime
    certOwner: str
    PUID: str
    cert: str
    content: str
    signedFieldsSequence: list
    signedFilesIdSequence: List[int]
    providerType: EdsProviderTypeForModels
    
    class Config:
        orm_mode = True




# Properties to return to client
class Eds(EdsInDBBase):
    pass


# Properties properties stored in DB
class EdsInDB(EdsInDBBase):
    pass

