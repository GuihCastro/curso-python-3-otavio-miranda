"""# json.dumps e json.loads com strings + typing.TypedDict"""

import json
from typing import TypedDict


class Book(TypedDict):
    title: str
    title_pt_br: str
    author: str
    pages: int
    main_characters: list[str]
    dragons: list[str]
    is_read: bool


string_json = '''
{
    "title": "A Song of Ice and Fire: A Game of Thrones",
    "title_pt_br": "As Crônicas de Gelo e Fogo: A Guerra dos Tronos",
    "author": "George R. R. Martin",
    "pages": 694,
    "main_characters": [
        "Jon Snow",
        "Daenerys Targaryen",
        "Ned Stark",
        "Cersei Lannister",
        "Robert Baratheon"
    ],
    "dragons": [
        "Drogon",
        "Rhaegal",
        "Viserion"
    ],
    "is_read": true
}
'''

book: Book = json.loads(string_json)
json_string = json.dumps(book, indent=2)
print(json_string)
