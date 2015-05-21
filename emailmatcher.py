from fnmatch import fnmatch


class EmailMatcher(object):
    ''' Matches emails using glob-like email patterns.

    >>> matcher = EmailMatcher.from_pattern_string('*@example.com,surveillance@*')
    >>> matcher.matches('user@example.com')
    True
    >>> matcher.matches('surveillance@security.net')
    True
    >>> matcher.matches('henchman@evil.org')
    False

    '''

    def __init__(self, _email_patterns=[]):
        self.email_patterns = _email_patterns

    @classmethod
    def from_pattern_string(cls, pattern_string):
        email_patterns = [x for x in pattern_string.split(',')]
        return cls(email_patterns)

    def matches(self, email):
        return any(fnmatch(email, pattern) for pattern in self.email_patterns)
