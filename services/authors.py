class Author:
    def __init__(self) -> None:
        pass

    def getAllAuthors(self, db):
        return list(db.authors.find({}, {"_id": 0}))
