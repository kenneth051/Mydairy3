"""validation page"""


class Validate():
    """class to validate diary data"""

    @classmethod
    def validate_updating_duplicates(cls, cur, entryid, user_id1, title1, body1):
        """method to check for duplicate entries when updating"""
        data = False
        cur.execute("""SELECT * FROM Entries where
                    user_id = %s and title = %s or
                    body = %s and user_id = %s """, (user_id1, title1, body1, user_id1))
        affected = cur.rowcount
        if affected > 0:
            data = True
        return data
