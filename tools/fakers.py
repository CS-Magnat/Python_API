from faker import Faker


class Fake:
    """
    Class for generating random test data using Faker library
    """

    def __init__(self, faker: Faker):
        """
        :param faker: Faker class instance that will be used for data generation
        """
        self.faker = faker

    def text(self) -> str:
        """
        Generates random text

        :return: Random text
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Generates random UUID4

        :return: Random UUID4
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Generates random email

        :param domain: Email domain (e.g., "example.com")
        If not specified, random domain will be used
        :return: Random email
        """
        return self.faker.email(domain=domain)

    def sentence(self) -> str:
        """
        Generates random sentence

        :return: Random sentence
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Generates random password

        :return: Random password
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Generates random last name

        :return: Random last name
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Generates random first name

        :return: Random first name
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Generates random middle name

        :return: Random middle name
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        Generates string with estimated time (e.g., "2 weeks")

        :return: String with estimated time
        """
        return f"{self.integer(1, 10)} weeks"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Generates random integer in specified range.

        :param start: Range start (inclusive)
        :param end: Range end (inclusive)
        :return: Random integer
        """
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """
        Generates random maximum score in range from 50 to 100

        :return: Random score
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Generates random minimum score in range from 1 to 30

        :return: Random score
        """
        return self.integer(1, 30)


fake = Fake(faker=Faker())