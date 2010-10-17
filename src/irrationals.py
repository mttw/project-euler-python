# Originally contributed by Sjoerd Mullender.
# Significantly modified by Jeffrey Yasskin <jyasskin at gmail.com>.

"""Rational, infinite-precision, real numbers."""

from __future__ import division
import math
import numbers
import operator
import re

__all__ = ['Fraction', 'gcd']

Rational = numbers.Rational



class Fraction(Rational):
    """This class implements rational numbers.

    Fraction(8, 6) will produce a rational number equivalent to
    4/3. Both arguments must be Integral. The numerator defaults to 0
    and the denominator defaults to 1 so that Fraction(3) == 3 and
    Fraction() == 0.

    Fractions can also be constructed from strings of the form
    '[-+]?[0-9]+((/|.)[0-9]+)?', optionally surrounded by spaces.

    """

    __slots__ = ('_numerator', '_denominator')

    # We're immutable, so use __new__ not __init__
    def __new__(cls, numerator=0, denominator=1):
        """Constructs a Fraction.

        Takes a string like '3/2' or '1.5', another Fraction, or a
        numerator/denominator pair.

        """
        self = super(Fraction, cls).__new__(cls)



        if denominator == 0:
            raise ZeroDivisionError('Fraction(%s, 0)' % numerator)
        numerator = operator.index(numerator)
        denominator = operator.index(denominator)
        g = gcd(numerator, denominator)
        self._numerator = numerator // g
        self._denominator = denominator // g
        return self

    def __repr__(self):
        """repr(self)"""
        return ('Fraction(%s, %s)' % (self._numerator, self._denominator))

    def __str__(self):
        """str(self)"""
        if self._denominator == 1:
            return str(self._numerator)
        else:
            return '%s/%s' % (self._numerator, self._denominator)

    def _operator_fallbacks(monomorphic_operator, fallback_operator):
        """Generates forward and reverse operators given a purely-rational
        operator and a function from the operator module.

        Use this like:
        __op__, __rop__ = _operator_fallbacks(just_rational_op, operator.op)

        In general, we want to implement the arithmetic operations so
        that mixed-mode operations either call an implementation whose
        author knew about the types of both arguments, or convert both
        to the nearest built in type and do the operation there. In
        Fraction, that means that we define __add__ and __radd__ as:

            def __add__(self, other):
                # Both types have numerators/denominator attributes,
                # so do the operation directly
                if isinstance(other, (int, long, Fraction)):
                    return Fraction(self.numerator * other.denominator +
                                    other.numerator * self.denominator,
                                    self.denominator * other.denominator)
                # float and complex don't have those operations, but we
                # know about those types, so special case them.
                elif isinstance(other, float):
                    return float(self) + other
                elif isinstance(other, complex):
                    return complex(self) + other
                # Let the other type take over.
                return NotImplemented

            def __radd__(self, other):
                # radd handles more types than add because there's
                # nothing left to fall back to.
                if isinstance(other, Rational):
                    return Fraction(self.numerator * other.denominator +
                                    other.numerator * self.denominator,
                                    self.denominator * other.denominator)
                elif isinstance(other, Real):
                    return float(other) + float(self)
                elif isinstance(other, Complex):
                    return complex(other) + complex(self)
                return NotImplemented


        There are 5 different cases for a mixed-type addition on
        Fraction. I'll refer to all of the above code that doesn't
        refer to Fraction, float, or complex as "boilerplate". 'r'
        will be an instance of Fraction, which is a subtype of
        Rational (r : Fraction <: Rational), and b : B <:
        Complex. The first three involve 'r + b':

            1. If B <: Fraction, int, float, or complex, we handle
               that specially, and all is well.
            2. If Fraction falls back to the boilerplate code, and it
               were to return a value from __add__, we'd miss the
               possibility that B defines a more intelligent __radd__,
               so the boilerplate should return NotImplemented from
               __add__. In particular, we don't handle Rational
               here, even though we could get an exact answer, in case
               the other type wants to do something special.
            3. If B <: Fraction, Python tries B.__radd__ before
               Fraction.__add__. This is ok, because it was
               implemented with knowledge of Fraction, so it can
               handle those instances before delegating to Real or
               Complex.

        The next two situations describe 'b + r'. We assume that b
        didn't know about Fraction in its implementation, and that it
        uses similar boilerplate code:

            4. If B <: Rational, then __radd_ converts both to the
               builtin rational type (hey look, that's us) and
               proceeds.
            5. Otherwise, __radd__ tries to find the nearest common
               base ABC, and fall back to its builtin type. Since this
               class doesn't subclass a concrete type, there's no
               implementation to fall back to, so we need to try as
               hard as possible to return an actual value, or the user
               will get a TypeError.

        """
        def forward(a, b):
            if isinstance(b, (int, long, Fraction)):
                return monomorphic_operator(a, b)
            elif isinstance(b, float):
                return fallback_operator(float(a), b)
            elif isinstance(b, complex):
                return fallback_operator(complex(a), b)
            else:
                return NotImplemented
        forward.__name__ = '__' + fallback_operator.__name__ + '__'
        forward.__doc__ = monomorphic_operator.__doc__

        def reverse(b, a):
            if isinstance(a, Rational):
                # Includes ints.
                return monomorphic_operator(a, b)
            elif isinstance(a, numbers.Real):
                return fallback_operator(float(a), float(b))
            elif isinstance(a, numbers.Complex):
                return fallback_operator(complex(a), complex(b))
            else:
                return NotImplemented
        reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
        reverse.__doc__ = monomorphic_operator.__doc__

        return forward, reverse

    def _add(a, b):
        """a + b"""
        return Fraction(a.numerator * b.denominator +
                        b.numerator * a.denominator,
                        a.denominator * b.denominator)

    __add__, __radd__ = _operator_fallbacks(_add, operator.add)

    def _sub(a, b):
        """a - b"""
        return Fraction(a.numerator * b.denominator -
                        b.numerator * a.denominator,
                        a.denominator * b.denominator)

    __sub__, __rsub__ = _operator_fallbacks(_sub, operator.sub)

    def _mul(a, b):
        """a * b"""
        return Fraction(a.numerator * b.numerator, a.denominator * b.denominator)

    __mul__, __rmul__ = _operator_fallbacks(_mul, operator.mul)

    def _div(a, b):
        """a / b"""
        return Fraction(a.numerator * b.denominator,
                        a.denominator * b.numerator)

    __truediv__, __rtruediv__ = _operator_fallbacks(_div, operator.truediv)
    __div__, __rdiv__ = _operator_fallbacks(_div, operator.div)

    def __floordiv__(a, b):
        """a // b"""
        # Will be math.floor(a / b) in 3.0.
        div = a / b
        if isinstance(div, Rational):
            # trunc(math.floor(div)) doesn't work if the rational is
            # more precise than a float because the intermediate
            # rounding may cross an integer boundary.
            return div.numerator // div.denominator
        else:
            return math.floor(div)

    def __rfloordiv__(b, a):
        """a // b"""
        # Will be math.floor(a / b) in 3.0.
        div = a / b
        if isinstance(div, Rational):
            # trunc(math.floor(div)) doesn't work if the rational is
            # more precise than a float because the intermediate
            # rounding may cross an integer boundary.
            return div.numerator // div.denominator
        else:
            return math.floor(div)


    def __hash__(self):
        """hash(self)

        Tricky because values that are exactly representable as a
        float must have the same hash as that float.

        """
        # XXX since this method is expensive, consider caching the result
        if self._denominator == 1:
            # Get integers right.
            return hash(self._numerator)
        # Expensive check, but definitely correct.
        if self == float(self):
            return hash(float(self))
        else:
            # Use tuple's hash to avoid a high collision rate on
            # simple fractions.
            return hash((self._numerator, self._denominator))

    def __eq__(a, b):
        """a == b"""
        if isinstance(b, Rational):
            return (a._numerator == b.numerator and
                    a._denominator == b.denominator)
        if isinstance(b, numbers.Complex) and b.imag == 0:
            b = b.real
        if isinstance(b, float):
            return a == a.from_float(b)
        else:
            # XXX: If b.__eq__ is implemented like this method, it may
            # give the wrong answer after float(a) changes a's
            # value. Better ways of doing this are welcome.
            return float(a) == b

    def _subtractAndCompareToZero(a, b, op):
        """Helper function for comparison operators.

        Subtracts b from a, exactly if possible, and compares the
        result with 0 using op, in such a way that the comparison
        won't recurse. If the difference raises a TypeError, returns
        NotImplemented instead.

        """
        if isinstance(b, numbers.Complex) and b.imag == 0:
            b = b.real
        if isinstance(b, float):
            b = a.from_float(b)
        try:
            # XXX: If b <: Real but not <: Rational, this is likely
            # to fall back to a float. If the actual values differ by
            # less than MIN_FLOAT, this could falsely call them equal,
            # which would make <= inconsistent with ==. Better ways of
            # doing this are welcome.
            diff = a - b
        except TypeError:
            return NotImplemented
        if isinstance(diff, Rational):
            return op(diff.numerator, 0)
        return op(diff, 0)

    def __lt__(a, b):
        """a < b"""
        return a._subtractAndCompareToZero(b, operator.lt)

    def __gt__(a, b):
        """a > b"""
        return a._subtractAndCompareToZero(b, operator.gt)

    def __le__(a, b):
        """a <= b"""
        return a._subtractAndCompareToZero(b, operator.le)

    def __ge__(a, b):
        """a >= b"""
        return a._subtractAndCompareToZero(b, operator.ge)

    def __nonzero__(a):
        """a != 0"""
        return a._numerator != 0

    # support for pickling, copy, and deepcopy

    def __reduce__(self):
        return (self.__class__, (str(self),))

    def __copy__(self):
        if type(self) == Fraction:
            return self     # I'm immutable; therefore I am my own clone
        return self.__class__(self._numerator, self._denominator)

    def __deepcopy__(self, memo):
        if type(self) == Fraction:
            return self     # My components are also immutable
        return self.__class__(self._numerator, self._denominator)
