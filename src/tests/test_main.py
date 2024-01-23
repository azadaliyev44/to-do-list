import unittest
from unittest.mock import patch
from io import StringIO
from main import main

class TestMainModule(unittest.TestCase):
    @patch("builtins.input", side_effect=["add 'Task 1' '2023-01-01' '1' 'Work'", "list", "exit"])
    def test_add_task_and_list(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()

        output = mock_stdout.getvalue().strip()
        self.assertIn("[1] Task 1 (Due: 2023-01-01, Priority: 1, Category: Work)", output)

    @patch("builtins.input", side_effect=["add 'Task 1' '2023-01-01' '1' 'Work'", "edit '1' 'New Task' '-' '2' 'Personal'", "list", "exit"])
    def test_edit_task(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()

        output = mock_stdout.getvalue().strip()
        self.assertIn("[1] New Task (Due: 2023-01-01, Priority: 2, Category: Personal)", output)

    @patch("builtins.input", side_effect=["add 'Task 1' '2023-01-01' '1' 'Work'", "delete '1'", "list", "exit"])
    def test_delete_task(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()

        output = mock_stdout.getvalue().strip()
        self.assertTrue("Task list is empty." in output)

    @patch("builtins.input", side_effect=["add 'Task 1' '2023-01-01' '1' 'Work'", "filter 'Work'", "list", "exit"])
    def test_filter_tasks(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()

        output = mock_stdout.getvalue().strip()
        self.assertIn("[1] Task 1 (Due: 2023-01-01, Priority: 1, Category: Work)", output)

    @patch("builtins.input", side_effect=["add 'Task 1' '2023-01-01' '1' 'Work'", "complete '1'", "list", "archive", "exit"])
    def test_complete_task_and_archive(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()

        output = mock_stdout.getvalue().strip()
        self.assertIn("Task at index 1 moved to archive: Task 1", output)

    @patch("builtins.input", side_effect=["add 'Task 1' '2023-01-01' '1' 'Work'", "email 'test@example.com'", "exit"])
    def test_send_email(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()

        output = mock_stdout.getvalue().strip()
        self.assertIn("Email sent successfully to test@example.com", output)

    @patch("builtins.input", side_effect=["add 'Task 1' '2023-01-01' '1' 'Work'","complete '1'", "archive", "exit"])
    def test_archive_show(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()

        output = mock_stdout.getvalue().strip()
        self.assertIn("[0] Task 1 (Due: 2023-01-01, Priority: 1, Category: Work)", output)

if __name__ == "__main__":
    unittest.main()
