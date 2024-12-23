from django.test import SimpleTestCase
from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OPsycopgpError

@patch('django.db.utils.ConnectionHandler.__getitem__')
class CommandsTests(SimpleTestCase):

    # DB가 준비되었을 때 wait_for_db가 잘 동작하는지 체크하는 함수
    def test_wait_for_db_ready(self, patched_getitem):
        patched_getitem.return_value = True

        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 1)

    # db연결에 오류가 발생한다고 가정을 하고 테스트
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_getitem):
        patched_getitem.side_effect = [Psycopg2OPsycopgpError] + \
            [OperationalError] * 5 + [True]
        
        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 7)