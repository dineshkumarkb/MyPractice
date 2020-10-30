from myexcept import User,addnum,subnum,add_user
import pytest


@pytest.mark.parametrize('user',[User("dinesh",1),
                                 User("kumar",2)])
class TestMyUser(object):

    def test_add_user_1(self, user):
        assert User(user.name, user.empid) == add_user(user.name, user.empid)
