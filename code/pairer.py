

class Pairer(object):

    def __init__(self, n):
        '''
        '''
        self.n = n

        if (n % 2 == 1 or n == 0 or n < 0):
            raise ValueError("N={0} IS BAD I CANT EVEN".format(n))
        a = n
        b = 1
        while (a % 4 == 0):
            a /= 2
            b *= 2
        self.a = a
        self.b = b


    def f(self, k):
        """
        INPUT: integer between 0 and n
        Canonical translation from k -> (r,s)
        Finds (r, s) such that s < self.a and r * self.b + s = k
        """
        return (k/self.b, k%self.b)

    def finv(self, t):
        """
        INPUT: (r,s) as above
        OUTPUT: k as above
        Canonical translation (r,s) -> k
        """
        r, s = t
        return r * self.b + s


    # TODO 
    # Jack's model to find what to do on day r with a students
    # Brian's model to find what to do on day s with b students
    # Combine using f and finv function to combine
