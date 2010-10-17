from fractions import Fraction
import math
from copy import copy
import itertools
from number import is_square, lsqrt
class Irrational:
    
    def __init__(self, p=Fraction(0), q=Fraction(0), ext=2):
        self.p = p
        self.q = q
        self.ext = ext
        if is_square(ext):
            self.p += lsqrt(ext)
            self.q = 0
            while is_square(self.ext):
                self.ext = lsqrt(self.ext)

    def __repr__(self):
        """repr(self)"""
        return ('Irrational(%s, %s*sqrt(%s))' % (self.p, self.q, self.ext))

    def __str__(self):
        """str(self)"""
        if self.q == 0:
            return '%s' % (self.p)
        else:
            return '%s + %s*sqrt(%s)' % (self.p, self.q, self.ext)


    def conjugate(self):
        return Irrational(self.p, -self.q, self.ext)

    def invert(self):
        conjugated = self.conjugate()
        rationalized = self * conjugated
        return Irrational(conjugated.p / rationalized.p, conjugated.q / rationalized.p, self.ext)

    def __add__(self, other):
        """a + b"""
        if self.ext != other.ext:
            raise ValueError("Different extensions not allowed")
        return Irrational(self.p + other.p, self.q + other.q, self.ext)

    def __sub__(self, other):
        """a - b"""
        if self.ext != other.ext:
            raise ValueError("Different extensions not allowed")
        return Irrational(self.p - other.p, self.q - other.q, self.ext)

    def __mul__(self, other):
        if self.ext != other.ext:
            raise ValueError("Different extensions not allowed")
        return Irrational(self.p * other.p + self.q * other.q * Fraction(self.ext),
                          self.p * other.q + self.q * other.p,
                          self.ext
                          )

    def __div__(self, other):
        if self.ext != other.ext:
            raise ValueError("Different extensions not allowed")
        return self * other.invert()

    def __float__(self):
        return float(self.p) + float(self.q) * math.sqrt(self.ext)

    def __hash__(self):
        """hash(self)

        Tricky because values that are exactly representable as a
        float must have the same hash as that float.

        """
        return hash((self.p, self.q, self.ext))

    def __eq__(self, other):
        """a == b"""
        if isinstance(self, Irrational):
            return (self.p == other.p and
                    self.q == other.q and self.ext == other.ext)
        else:
            return False

    def __trunc__(self):
        return int(float(self))

        
class ContinuousFraction:
    def __init__(self, start=[0], period=[]):
        
        self.start = start
        self.period = period

    def __repr__(self):
        """repr(self)"""
        return ('ContinuousFraction%s' % (str(self)))

    def __str__(self):
        """str(self)"""
        if len(self.period) == 0:
            return '(%s;%s)' % (self.start[0], ",".join([str(d) for d in self.start[1:]]))
        else:
            return '(%s;%s,(%s))' % (self.start[0], ",".join([str(d) for d in self.start[1:]]), ",".join([str(d) for d in self.period]))

    @classmethod
    def from_sqrt(cls, N):
        prev = (0, Irrational(0, 1, N))
        l = []
        mp = {}
        for i in itertools.count():
            f = int(prev[1])
            if f == 0:
                return ContinuousFraction(l)

            prev = (f, (prev[1] - Irrational(f,0,N)).invert())
            l.append(prev[0])
            if prev[1] in mp:
                index = mp[prev[1]]
                return ContinuousFraction(l[:index+1], l[index+1:])
            
            mp[prev[1]] = i
            

    def to_fraction(self, limit=1):
        l = copy(self.start)
        remaining = limit - len(self.start)
        if(len(self.period) > 0):
            l += self.period*(remaining/len(self.period)) 
            l += self.period[:remaining % len(self.period)]
        length = min(limit, len(l))
        f = Fraction(l[length - 1])
        for i in range(length -2, -1, -1):
            f = Fraction(l[i]) + Fraction(1)/f
        return f

    def __hash__(self):
        """hash(self)

        Tricky because values that are exactly representable as a
        float must have the same hash as that float.

        """
        return hash((self.start, self.period))

    def __eq__(self, other):
        """a == b"""
        if isinstance(other, ContinuousFraction):
            return (self.start == other.start and
                    self.period == other.period)
        else:
            return False