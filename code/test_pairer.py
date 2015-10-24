from pairer import *
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
    for b in range(1, 200):
        for k in range(1, 200):
            n.assert_equal(k, finv(f(k, b)[0], f(k, b)[1], b))


def test_get_pairing_power_of_2():
    n.assert_equal(get_pairing_power_of_2(1,4), [(0, 1), (1, 0), (2, 3), (3, 2)])


def test_combine_pairings():
    p1 = get_pairing_power_of_2(3, 4)
    p2 = get_pairing_power_of_2(1, 4)
    n.assert_equal(combine_pairings(p1, p2, 4), [(0, 13), (1, 12), (2, 15), (3, 14), (4, 9), (5, 8), (6, 11), (7, 10), (8, 5), (9, 4), (10, 7), (11, 6), (12, 1), (13, 0), (14, 3), (15, 2)])