"""validation page"""


class Validate():
    """class to validate diary data"""

    @classmethod
    def validate_entry(cls, entries, entry):
        """method to check for duplicate entries"""
        for data in entries:
            if (data['title'] == entry.title and
                    data['body'] == entry.body):
                return True
