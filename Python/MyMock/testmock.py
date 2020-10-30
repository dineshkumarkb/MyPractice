from mock import Mock



m = Mock(side_effect=KeyError('Test'))
#m(1,4,foo='bar')
print m()


