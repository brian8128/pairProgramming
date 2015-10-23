
from pairer import Pairer
import nose.tools as n

def test_init():
    p = Pairer(20)
    print type(p)
    n.assert_equal(p.a, 10)
    n.assert_equal(p.b, 2)

    q = Pairer(24)
    n.assert_equal(q.a, 6)
    n.assert_equal(q.b, 4)

def test_f():
    for i in range(1, 200):
        print i
        p = Pairer(i * 2)
        for j in range(1, i * 2):
            n.assert_equal(j, p.finv(p.f(j)))
