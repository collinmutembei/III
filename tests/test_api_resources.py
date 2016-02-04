from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Bucketlist, Item

class APIResourcesTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('tester', password='test')
        self.user.save()
        token_response = self.client.post('/auth/login/', {'username': 'tester', 'password': 'test'})

        self.client = APIClient()
        self.token = token_response.data['token']

    def test_bucketlists_api_endpoint(self):
        response = self.client.get('/api/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['bucketlists'], 'http://testserver/api/bucketlists/')

    def test_bucketlists_resource_requires_auth(self):
        post_response = self.client.post('/api/bucketlists/', {'name': 'test bucketlist'})
        get_response = self.client.get('/api/bucketlists/')

        self.assertEqual(post_response.status_code, 403)
        self.assertEqual(get_response.status_code, 403)

    def test_get_bucketlists_when_autheticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        response = self.client.get('/api/bucketlists/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_crud_operations_on_bucketlist_when_autheticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        response = self.client.post('/api/bucketlists/', {'name': 'test bucketlist'})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'test bucketlist')
        created_bucketlist = Bucketlist.objects.filter(name='test bucketlist')
        print("{0} created".format(created_bucketlist.__str__()))

        bucketlist_id = response.data['id']

        # Test getting single bucketlists
        single_bucketlist = self.client.get('/api/bucketlists/' + str(bucketlist_id) + '/')

        self.assertEqual(single_bucketlist.status_code, 200)
        self.assertEqual(single_bucketlist.data['id'], bucketlist_id)

        # Test updating bucketlist
        updated_bucketlist = self.client.put('/api/bucketlists/' + str(bucketlist_id) + '/', {'name': 'new bucketlist'})

        self.assertEqual(updated_bucketlist.status_code, 200)
        self.assertEqual(updated_bucketlist.data['name'], 'new bucketlist')

        # Test deleting bucketlist
        another_item = self.client.post('/api/bucketlists/' + str(bucketlist_id) + '/items/', {'name': 'another item', 'parent_bucketlist': bucketlist_id})
        delete_bucketlist = self.client.delete('/api/bucketlists/' + str(bucketlist_id) + '/')
        bucketlist_item = self.client.get('/api/bucketlists/' + str(bucketlist_id) + '/items/' + str(another_item.data['id']) + '/')

        self.assertEqual(delete_bucketlist.status_code, 204)
        self.assertEqual(bucketlist_item.status_code, 404)

    def test_crud_operations_on_item_in_bucketlist_when_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        another_bucketlist = self.client.post('/api/bucketlists/', {'name': 'another test bucketlist'})
        bucketlist_id = another_bucketlist.data['id']

        # Creating item in bucketlist
        response = self.client.post('/api/bucketlists/' + str(bucketlist_id) + '/items/', {'name': 'test item', 'parent_bucketlist': bucketlist_id})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'test item')

        created_item = Item.objects.filter(name='test item')
        print("{0} created".format(created_item.__str__()))

        item_id = response.data['id']

        # Test getting added item
        created_item = self.client.get('/api/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/')

        self.assertEqual(created_item.status_code, 200)
        self.assertEqual(created_item.data['id'], item_id)

        # Test updating item
        updated_item = self.client.put('/api/bucketlists/' + str(bucketlist_id) + '/items/' + str(item_id) + '/', {'name': 'new item', 'parent_bucketlist': bucketlist_id})

        self.assertEqual(updated_item.status_code, 200)
        self.assertEqual(updated_item.data['name'], 'new item')
