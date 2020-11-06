from django.test import TestCase
from django.urls import reverse, resolve

from boards.views import home, board_topics
from boards.models import Board


class HomeTests(TestCase):

    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    # A simple test to testing the status code response 200 (success)
    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    # test to verify URL / -> is returning the home view
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))


class BoardTopicTests(TestCase):
    # SetUp method is going to create a Board instance to use in the tests.
    # Because Django doesn't run test against the current Database.
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    # testing if Django returns status code 200(sucess) for an existing Board
    def test_board_topics_view_sucess_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        assert response.status_code == 200

    # testing if Django returns status code 404(page not found)
    # for a Board that doesn't exist in the database
    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        assert response.status_code == 404

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        assert view.func == board_topics

    def test_board_topics_view_contains_link_to_homepage(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
