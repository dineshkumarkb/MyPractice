import pytest
from myexcept import User, add_user, addnum,subnum,mulnum,divnum


def test_add_user():
    user = User("dinesh", 123)
    assert user == add_user("dinesh", 123)

# Paramterize using user object
@pytest.mark.parametrize('user',[User("dinesh",1),
                                 User("kumar",2),
                                 User("user3",3)])
def test_add_param_user_1(user):
    print(" The user value is ", user)
    assert user == add_user(user.name, user.empid)


@pytest.mark.parametrize('name,empid',[("dinesh",1),
                                         ("kumar",2),
                                         ("user3",3),
                                         ("user4",4)])
def test_add_param_user_2(name,empid):
    user = User(name,empid)
    assert user == add_user(name,empid)



test_args = (User("dinesh",1),
             User("kumar",2),
             User("user3",3),
             User("user4",4),
             User("user5",5))

test_ids = ['User({}, {})'.format(t.name,t.empid) for t in test_args]
sample_ids = [x for x in range(len(test_args))]

@pytest.mark.parametrize('user',test_args,ids=test_ids)
def test_add_user_params_id(user):
    name, empid = user.name, user.empid
    assert User(name,empid) ==  add_user(name,empid)

@pytest.mark.parametrize("x,y",[(4,5),
                                (6,9),
                                (-1,-5),
                                (100000,7)]
                         )
def test_add_num(x,y):
    result = x + y
    assert result == addnum(x, y)


values_to_try = ((1,2),(7,8))
value_ids = ['{},{}'.format(x,y) for x, y in values_to_try]

@pytest.mark.parametrize("x,y",values_to_try,ids=value_ids)
def test_add_num_ids(x,y):
    assert (x+y) == addnum(x,y)


