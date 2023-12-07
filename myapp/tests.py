from django.contrib.auth.models import User
from django.test import TestCase
from myapp.models import Clue

class ClueTestClass(TestCase):

    def setUp(self):
        # Create a user
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a Clue with the user as the submitted_by
        Clue.objects.create(
            clue_text="clue_test",
            hint_text="hint",
            multiple_choice="mc",
            created_by="me",
            submitted_by=user  # Assign the user to submitted_by
        )

    def tearDown(self):
        Clue.objects.filter(clue_text="clue_test").delete()

    def test_clue(self):
        d_clue = Clue.objects.get(clue_text="clue_test")
        self.assertEqual(d_clue.clue(), 'clue_test')

    def test_hint(self):
        d_clue = Clue.objects.get(clue_text="clue_test")
        self.assertEqual(d_clue.hint(), 'hint')

    def test_mult(self):
        d_clue = Clue.objects.get(clue_text="clue_test")
        self.assertEqual(d_clue.mult(), 'mc')

    def test_status(self):
        d_clue = Clue.objects.get(clue_text="clue_test")
        self.assertFalse(d_clue.status())