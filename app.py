# TODO: build FastAPI service

import uvicorn
from fastapi import FastAPI
from object import schema
from typing import Optional, List
from utilities import tools

# from utilities.database import SessionLocal

tags_metadata = [
    {
        "name": "selection",
        "description": "Type a s_id, s_area_id, start and end datetime to filter posts. "
                       "e.g. s_id refers to forum sites. s_area_id refers to forum boards."
                       "When start_time and end_time are filled, you'll get posts whose post time are in [start, end]."

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
                       start_time: Optional[str] = None,
                       end_time: Optional[str] = None,
                       limit: Optional[int] = None,
                       offset: Optional[int] = None):
    return tools.select_posts(s_id=s_id, s_area_id=s_area_id, start_time=start_time, end_time=end_time,
                              limit=limit, offset=offset)


# @app.get('/posts/post-time', tags=['post_time'], response_model=List[schemas.TypeHintOut])
# async def select_posts_by_post_time(start_time: Optional[str] = '2019-09-01 00:00:00',
#                                     end_time: Optional[str] = '2019-09-30 23:59:59',
#                                     limit: int = 1000,
#                                     offset: int = 0):
#     def string_to_datetime(datetime_string: str):
#         try:
#             if len(datetime_string.split()) == 2:
#                 datetime_obj = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')
#                 return datetime.strftime(datetime_obj, '%Y-%m-%d %H:%M:%S')
#             elif len(datetime_string.split()) == 1:
#                 datetime_obj = datetime.strptime(datetime_string + ' 23:59:59', '%Y-%m-%d %H:%M:%S')
#                 return datetime.strftime(datetime_obj, '%Y-%m-%d %H:%M:%S')
#         except:
#             return False
#
#     start_time = string_to_datetime(start_time)
#     end_time = string_to_datetime(end_time)
#     if start_time and end_time:
#         return tools.select_posts(s_id=s_id, s_area_id=s_area_id, start_time=start_time, end_time=end_time,
#                                   limit=limit, offset=offset)
#     else:
#         return {'Status': 'Error Occurred'}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True, debug=True)
