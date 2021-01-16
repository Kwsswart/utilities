from tika import parser
from pymongo import MongoClient
from pprint import pprint


def tika_parser(fpath, database_name, collection_name):
    """ 
    Function to pass PDF Files and store in database.
    """

    #Extract data
    content = parser.from_file(fpath)
    if 'content' in content:
        text = content['content']
        metadata = content['metadata']
    else: 
        return
    
    #Convert content to string
    text = str(text)
    # Connect to db and open/create new db
    client = MongoClient("mongodb://localhost:27017/")
    db = client[database_name]
    col = db[collection_name]
    x = col.insert_one({
        "Author": metadata['Author'],
        "Content_Type": metadata['Content-Type'],
        "Creation_Date": metadata['Creation-Date'],
        "Content" : text.lstrip('\n')
    })

    print(x.inserted_id)
    