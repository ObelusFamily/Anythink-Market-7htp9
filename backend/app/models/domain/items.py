from typing import List, Optional


from models.common import DateTimeModelMixin, IDModelMixin
from models.domain.profiles import Profile
from models.domain.rwmodel import RWModel


class Item(IDModelMixin, DateTimeModelMixin, RWModel):
    slug: str
    title: str
    description: str
    tags: List[str]
    seller: Profile
    favorited: bool
    favorites_count: int
    image: Optional[str]
    body: Optional[str]
