# TODO: build FastAPI service

import os
import uvicorn
from datetime import datetime
from fastapi import FastAPI, Query
from object import schema
from typing import Optional, List
from utilities import tools
from starlette.concurrency import run_in_threadpool


tags_metadata = [
    {
        "name": "selection",
        "description": "Type s_id, s_area_id, p_type, start time, end time and keywords to filter posts. "
                       "'s_id' represents forum sites. 's_area_id' represents forum boards. "
                       "When start_time and end_time are filled, you'll get posts whose post time are in [start, end]. "
                       "If you are willing to select posts with multiple words, hit 'Add string item' to add more keywords. "                       
                       "If there is no condition specified, we'll return the newest 100 posts."

    }
]

app = FastAPI(
    title="MYSQL API: R for CURD ",
    description="fetching data in MySQL database by FastAPI",
    openapi_tags=tags_metadata
)


@app.get('/')
async def home():
    return 'Ready to fetch data by MYSQL API!'


@app.get('/posts', tags=['selection'], response_model=List[schema.TypeHintOut])
async def select_posts(s_id: Optional[str] = None,
                       s_area_id: Optional[str] = None,
                       content_type: str = 'main',
                       start_time: Optional[datetime] = None,
                       end_time: Optional[datetime] = None,
                       keywords: Optional[List[str]] = Query(None),
                       limit: int = 100,
                       offset: int = 0):

    if keywords:
        keywords = [keyword.strip(' ') for keyword in keywords]
        keywords = '%'.join(keywords)

    return await run_in_threadpool(tools.select_posts, s_id=s_id, s_area_id=s_area_id,
                                   content_type=content_type, start_time=start_time,
                                   end_time=end_time, keywords=keywords,
                                   limit=limit, offset=offset)

if __name__ == "__main__":
    uvicorn.run("app:app", host=os.getenv('host'), port=8000, reload=True, debug=True)
