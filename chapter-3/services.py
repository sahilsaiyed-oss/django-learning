from datetime import datetime


class TextService:
    """
    Service class for text processing operations.
    """

    @staticmethod
    def word_count(text):
        if not text:
            return 0
        return len(text.split())

    @staticmethod
    def character_count(text):
        if not text:
            return 0
        return len(text)

    @staticmethod
    def to_uppercase(text):
        return text.upper()

    @staticmethod
    def to_lowercase(text):
        return text.lower()

    @staticmethod
    def generate_slug(text):
        """
        Generates URL-friendly slug
        Example: "Hello Django World" -> "hello-django-world"
        """
        return text.strip().lower().replace(" ", "-")


class DateTimeService:
    """
    Service class for date & time related operations.
    """

    @staticmethod
    def current_datetime():
        return datetime.now()

    @staticmethod
    def formatted_datetime():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
