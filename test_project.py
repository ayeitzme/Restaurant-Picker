import project
from project import action
from project import greeting
from project import get_hour
from unittest.mock import patch
import builtins
import io

def test_get_hour():
    # test that the current hour is returned correctly
    hour = get_hour()
    assert 0 <= hour < 24

def test_greeting():
    # test greetings for different hours
    assert greeting(5) == "Good morning!\n"
    assert greeting(12) == "Good afternoon!\n"
    assert greeting(20) == "Good evening!\n"

@patch('sys.stdout', new_callable=io.StringIO)
def test_action(mock_stdout):
    with patch.object(builtins, 'input', lambda _: 'a'):
        with patch.object(project, 'pick', return_value = None)as mock_pick:
            action()
            mock_pick.assert_called_once()

@patch('project.LibraryInput')
def test_action_input_b(mock_lib_input):
    with patch.object(builtins, 'input', lambda _: 'b'):
        action()
        mock_lib_input.return_value.add_library.assert_called_once()

@patch('sys.stdout', new_callable=io.StringIO)
def test_action_c(mock_stdout):
    with patch.object(builtins, 'input', lambda _: 'c'):
        action()
        assert mock_stdout.getvalue()=='Okay, goodbye! :)\n'

@patch('sys.stdout', new_callable=io.StringIO)
def test_action_d(mock_stdout):
    responses = iter(['d', 'c'])
    with patch.object(builtins, 'input', lambda _: next(responses)):
        action()
        assert mock_stdout.getvalue()=='Try again, please enter \'A\' or \'B\' or \'C\'.\nOkay, goodbye! :)\n'