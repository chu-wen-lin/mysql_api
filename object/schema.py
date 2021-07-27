# TODO: use Pydantic to define schemas for working with the API request/response

from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class TypeHintOut(BaseModel):
    id: str
    identify: Optional[str] = None
    p_type: Optional[str] = None
    s_id: Optional[str] = None
    s_area_id: Optional[str] = None
    main_id: Optional[str] = None
    title: Optional[str] = None
    author: Optional[str] = None
    page_url: Optional[str] = None
    post_time: Optional[datetime] = None
    content: Optional[str] = None
