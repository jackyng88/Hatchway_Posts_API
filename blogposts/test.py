from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

# POSTS_URL calls our own API endpoint
POSTS_URL = reverse('external-api-view')


class PostsAPITests(TestCase):
    # test the posts API

    def setUp(self):
        # overriding the TestCase setup function
        self.client = APIClient()

    def test_no_params(self):
        # test our API when no query parameters are provided.
        res = self.client.get(POSTS_URL)
        error = { "error": "The tag parameter is required"}

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, error)

    def test_single_tag(self):
        # tests the API when a single tag is provided. 
        tag = 'tech'
        res = self.client.get(POSTS_URL + '?tags=' + tag)
        #print(res)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # Two assertIn to check first and last objects to see if our provided
        # tag ('tech') exists in their tags list.
        self.assertIn(tag, res.data['posts'][0].get('tags'))
        self.assertIn(tag, res.data['posts'][-1].get('tags'))
    
    def test_plural_tags(self):
        # tests the API with multiple tags.
        tags = ['science', 'history']
        data = {}
        
        for tag in tags:
            res = self.client.get(POSTS_URL + '?tags=' + tag)
            data.update(res.json())
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
        # The following assertTrue's check if any of the elements in the tags
        # list are present in the tags list from the first, 15th, and last 
        # returned returned JSON objects.
        self.assertTrue(any(tag in tags for tag in data['posts'][0].get('tags')))
        self.assertTrue(any(tag in tags for tag in data['posts'][15].get('tags')))
        self.assertTrue(any(tag in tags for tag in data['posts'][-1].get('tags')))