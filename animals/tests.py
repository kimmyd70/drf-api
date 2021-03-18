from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Animal

class AnimalTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username = 'testuser1',
        password = 'pass')
        testuser1.save()
        
        test_animal = Animal.objects.create(
            added_by = testuser1,
            name = 'Green Tree Frog',
            description = 'The American green tree frog (Dryophytes cinereus) is a common species of New World tree frog belonging to the family Hylidae. A common backyard species, it is popular as a pet, and is the state amphibian of Georgia and Louisiana.',
            category = 'amphibian',
        )
        test_animal.save()
        
    def test_animal_content(self):
        animal = Animal.objects.get(id=1)
        actual_added_by = str(animal.added_by)
        actual_name = str(animal.name)
        actual_description = str(animal.description)
        actual_category = str(animal.category)
        self.assertEqual(actual_added_by, 'testuser1')
        self.assertEqual(actual_name, 'Green Tree Frog')
        self.assertEqual(actual_description, 'The American green tree frog (Dryophytes cinereus) is a common species of New World tree frog belonging to the family Hylidae. A common backyard species, it is popular as a pet, and is the state amphibian of Georgia and Louisiana.')
        self.assertEqual(actual_category, 'amphibian')
        
            
