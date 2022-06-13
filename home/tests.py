from urllib import response
from django.test import TestCase, Client
from .models import Inventory


class InventoryTestCase(TestCase):
    def setUp(self):
        Inventory.objects.create(name="Paper", quantity=100, unit_price=0.5)
        Inventory.objects.create(name="Pens", quantity=1000, unit_price=0.1)
        Inventory.objects.create(
            name="Folders", quantity=50,
            unit_price=1.5, deleted=True,
            delete_comment='Item Deleted'
        )

    def test_display_items(self):
        """
        Test that the homepage is correctly displaying
        both deleted and undeleted items.
        """
        c = Client()
        response = c.get("/")
        string = response.content.decode("utf-8")
        self.assertInHTML("<td>Paper</td>", string)
        self.assertInHTML("<td>Folders</td>", string)
        self.assertEqual(response.status_code, 200)

    def test_delete_item(self):
        """
        Test POST requests to delete inventory view.
        Deletes item, adds comment and then checks
        item against list of deleted items.
        """
        c = Client()
        item = Inventory.objects.get(id=1)
        response = c.post("/delete/1", {"delete_comment": "Item Deleted"})
        del_items = Inventory.objects.filter(deleted=True)
        self.assertIn(item, del_items)
        self.assertEqual(response.status_code, 302)

    def test_create_item(self):
        """
        Tests the add inventory view.
        Creates an instance of the Inventory class, and
        then confirms it is present in the db.
        """
        c = Client()
        data = {
            "name": "Binders",
            "quantity": 500,
            "unit_price": 1.00,
        }
        response = c.post("/add/", data)
        item = Inventory.objects.get(name="Binders")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(item)

    def test_edit_inventory(self):
        """
        Tests edit inventory view.
        Updates "quantity" and "unit price" of item in db
        and checks that the new values are present.
        """
        c = Client()
        data = {
            "name": "Pens",
            "quantity": 500,
            "unit_price": 1.25
        }
        response = c.post('/edit/2', data)
        item = Inventory.objects.get(id=2)
        self.assertEqual(item.quantity, 500)
        self.assertEqual(item.unit_price, 1.25)
        self.assertEqual(response.status_code, 302)

    def test_restore_inventory(self):
        """
        Tests the restore inventory view.
        Tests that view takes a deleted item, 
        undeletes it and removes the delete comment.
        """
        c = Client()
        response = c.post('/restore/3')
        item = Inventory.objects.get(id=3)
        items = Inventory.objects.filter(deleted=False)
        self.assertIn(item, items)
        self.assertEqual(item.delete_comment, '')
        self.assertEqual(response.status_code, 302)
