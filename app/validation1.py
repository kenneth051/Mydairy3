"""validation page"""


class Validate():
    """class to validate diary data"""

    @classmethod
    def validate_updating_duplicates(cls, cur, entryid,user_id1,title1,body1):
        """method to check for duplicate entries when updating"""
        cur.execute("SELECT * FROM Entries where id = %s and user_id = %s and title = %s or body = %s",(entryid, user_id1, title1, body1))
        affected=cur.rowcount
        if affected >0:
            return True
