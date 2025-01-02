from django.test import TestCase

from rsoi_rating_app.models import Rating

class RatingTestCase(TestCase):
    def test_rating_creation(self):
        rating = Rating.objects.create(username="test-user", stars=50)
        self.assertEqual(rating.username, "test-user")
        self.assertEqual(rating.stars, 50)
