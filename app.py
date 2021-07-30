# TODO: build FastAPI service

import uvicorn
from datetime import date
from fastapi import FastAPI
from object import schema
from typing import Optional, List
from utilities import tools


tags_metadata = [
    {
        "name": "selection",
        "description": "Type a s_id, s_area_id, start and end datetime to filter posts. "
                       "'s_id' represents forum sites. 's_area_id' represents forum boards. "
                       "When start_time and end_time are filled, you'll get posts whose post time are in [start, end]. "
                       "If there is no condition specified, MYSQL API will return newest 100 posts."

    }
]

app = FastAPI(
    title="MYSQL API: R for CURD ",
    description="fetching data in MySQL database by FastAPI",
    openapi_tags=tags_metadata
)


@app.get('/')
async def home():
    return 'Ready to fetch data by MYSQL CRUD API!'


@app.get('/posts', tags=['selection'], response_model=List[schema.TypeHintOut])
async def select_posts(s_id: Optional[str] = None,
                       s_area_id: Optional[str] = None,
                       start_time: Optional[date] = None,
                       end_time: Optional[date] = None,
                       limit: int = 100,
                       offset: int = 0):

    return tools.select_posts(s_id=s_id, s_area_id=s_area_id, start_time=start_time,
                              end_time=end_time, limit=limit, offset=offset)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True, debug=True)
