# ls listings_app/tests.py | entr -pc python manage.py test
# coverage run --source="." manage.py test
# coverage report -m
from django.test import TestCase, Client
from .models import Listing


class ListingTestCase(TestCase):

    def setUp(self):
        Listing.create(title="a", text="some text")
        Listing.create(title="b", text="some text")
        Listing.create(title="c", text="some text")
        Listing.create(title="video", text="make video")
        Listing.create(title="", text="make video")
        Listing.create(title="", text="make video")
        Listing.create(title="s", text="make video")
        Listing.create(title="r", text="make video")
        Listing.create(title="Hello", text="some text")

    def test_default_order(self):
        listing_a = Listing.objects.get(title="a")
        listing_b = Listing.objects.get(title="b")
        assert listing_a.rank < listing_b.rank

    def test_highest_rank(self):
        highest_rank = Listing.objects.get(title="Hello")
        assert highest_rank.rank == Listing.highest_rank

    def test_rerank_up(self):
        rerank_listing = Listing.objects.get(title="video")
        rerank_listing.rerank(1)
        rerank_listing.refresh_from_db()
        listing_a = Listing.objects.get(title="a")
        assert rerank_listing.rank == 1 and listing_a.rank == 2

    def test_rerank_down(self):
        listing_a = Listing.objects.get(title="a")
        listing_a.rerank(4)
        listing_a.refresh_from_db()
        assert listing_a.rank == 4
        listing_c = Listing.objects.get(title="c")
        assert listing_c.rank == 2

    def test_rerank_by_list(self):
        reranked = [9, 1, 2, 3, 4, 5, 6, 7, 8]
        Listing.rerank_by_list(reranked)
        assert Listing.objects.get(pk=9).rank == 1
        assert Listing.objects.get(pk=2).rank == 3
        # assert Listing.objects.get(pk=5).rank == 3

    def test_empty_fields(self):
        empty_title = Listing.objects.filter(title="")[0]
        assert empty_title.text == "make video"

    def test_load_index(self):
        c = Client()
        response = c.get("/")
        self.assertTemplateUsed(response, 'listings_app/index.html')
        assert response.status_code == 200
        assert response['content-type'] == 'text/html; charset=utf-8'

    def test_load_item(self):
        c = Client()
        response = c.get("/listing_details_partial/2/")
        assert b'b' in response.content
        assert response.status_code == 200

    def test_add_item(self):
        c = Client(HTTP_HX_CURRENT_URL="/")
        response = c.post('/create', {"title": "new", "text": "Test todo"})
        assert response.status_code == 200
        response = c.get("/listing_details_partial/10/")
        assert b'new' in response.content
