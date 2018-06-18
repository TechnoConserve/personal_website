import pytest

from django.contrib.auth import get_user_model


class TestCustomUser(object):
    @pytest.fixture(scope='module')
    def django_db_setup(self, django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
            get_user_model().objects.create(username='a')
        yield
        with django_db_blocker.unblock():
            get_user_model().objects.filter(username='a').delete()

    @pytest.mark.django_db
    def test_user_creation(self):
        assert get_user_model().objects.count() == 1
        assert get_user_model().objects.get(username='a').username == 'a'
