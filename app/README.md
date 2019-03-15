# BOOKS API #
### Test task for JustApp team ###

## Installing ##

```
git clone
pip install -r requirements.txt
python main.py
```

## URLS ##

**Creating books**
POST /books/

Responses: 
201 With created books array, in case at least one created successful.
400 If none created 


```
Correct request schema:
[
  {
    "data": {
      "type": "books",
      "id": 15,
      "attributes": {
        "pages_count": 252,
        "datetime_added": "2019-03-15T09:26:08.376593Z",
        "author": "Mark Lutz",
        "year": 2003,
        "name": "Python"
      }
    }
  }]
  
  OR
  [{
    "data": {
      "type": "books",   
      "attributes": {
        "pages_count": 152,        
        "author": "Mark Twain",
        "year": 2009,
        "name": "Blue Book"
      }
    }
  }
]
```

Notes:

- Request must be array, even if one book is sended
- After request, response returns array of all created books.
- ID and DATETIME_ADDED fields is autogenerated and would be ignored even they exist in request .
- Errors on creating is silenced if at least one created successful, so number of returned books in response must be checked. 

**Retrieving book**
GET /books/:id

:id - primary key of object

Responses: 
- 200 Returns all books array in response body, in case at least one created successful.
- 404 Not found 

**Retrieving all books**
GET /books/

Responses: 
- 200 Returns all books array in response body, in case at least one created successful.

**Retrieving a specific set of books(filtering, search)**
GET /books/?*queryparam*=***value***

Available queryparams:
- *name* Response will contain only books that have given substring in NAME field 
- *author* Response will contain only books that have given substring in AUTHOR field 
- *before* Response will contain only books that have timestamp earlier(less) than given number of secs back from time now, in DATETIME_ADDED field 
- *after* Response will contain only books that have timestamp later(greater) than given number of secs back from time now, in DATETIME_ADDED field
```
Examples of using:
/books/?before=300 - Books, added earlier than 5 min back(300 seconds)
/books/?after=3600 - Books, added in last hour
/books/?author=Mark - Books, contain Mark in AUTHOR field 

```


Query can contain all queryparams or none, order isn't important

Responses:
- 200 Returns all books array


**Updating**
PATCH /books/:id

Responses 

- 204 OK
- 404 Not found

Response contains updated book

:id - primary key of object



Request for updating must be an array with one element
ID, DATETIME_ADDED fields makes no sense to send, because of its immutability. 

**Deleting**
DELETE /books/:id

:id - primary key of object

- 204 OK
- 404 Not found 

 

