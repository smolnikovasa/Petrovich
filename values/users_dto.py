import random
from dataclasses import dataclass

from mimesis import Person, locales
from mimesis.enums import Gender


@dataclass
class UserDTO:
    """Объект с данными пользователей"""

    _person = Person(locales.RU)
    _rand = str(random.randint(1000000, 9999999))

    username: str = f"test-{_rand}"
    first_name = _person.first_name(Gender.MALE)
    last_name = _person.last_name(Gender.MALE)
    user_email = f"{_rand}@user.test"
    user_phone = _person.telephone("+7-(###)-###-####")
    password: str = "123456789"
