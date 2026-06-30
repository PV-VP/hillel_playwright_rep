"""пробую через unittest"""
import unittest
from pathlib import Path

from homework_13 import log_event

class TestLogEvent(unittest.TestCase):

    def setUp(self):
        Path('login_system.log').write_text('')

    def test_success(self):
        log_event('Pasha', 'success')

        content = Path("login_system.log").read_text()
        self.assertIn("Login event - Username: Pasha, Status: success", content)

    def test_expired(self):

        log_event('Ivan', 'expired')

        content = Path("login_system.log").read_text()

        self.assertIn("Login event - Username: Ivan, Status: expired", content)

    def test_failed(self):

        log_event('Sasha', 'failed')

        content = Path("login_system.log").read_text()

        self.assertIn("Login event - Username: Sasha, Status: failed", content)


"""
    * success - успішний, логується на рівні інфо - Pasha
    * expired - пароль застаріває і його слід замінити, логується на рівні warning - Ivan
    * failed  - пароль невірний, логується на рівні error - Sasha
"""