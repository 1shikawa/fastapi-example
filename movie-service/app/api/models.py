from pydantic import BaseModel
from typing import List, Optional

# Pydanticを用いたAPIに渡されるデータの定義
# ValidationやDocumentationの機能が追加される

# insert用のrequest model id(自動採番)は入力不要のため未定義
class MovieIn(BaseModel):
    name: str
    plot: str
    genres: str
    casts: str

# response model
class MovieOut(MovieIn):
    id: int

# update用のrequest model
class MovieUpdate(MovieIn):
    # name: Optional[str] = None
    # plot: Optional[str] = None
    # genres: Optional[str] = None
    # casts: Optional[str] = None
    name: str
    plot: str
    genres: str
    casts: str
