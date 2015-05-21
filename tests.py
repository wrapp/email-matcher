from emailmatcher import EmailMatcher


class TestEmailMatcherNull(object):
    def setup(self):
        self.matcher = EmailMatcher()

    def test_empty_str(self):
        assert self.matcher.matches('') is False

    def test_None(self):
        assert self.matcher.matches(None) is False

    def test_user(self):
        assert self.matcher.matches('user@example.com') is False



class TestEmailMatcherSinglePattern(object):
    def setup(self):
        self.matcher = EmailMatcher.from_pattern_string('*@example.com')

    def test_user(self):
        assert self.matcher.matches('user@example.com') is True

    def test_surveillance(self):
        assert self.matcher.matches('surveillance@security.net') is False

    def test_henchman(self):
        assert self.matcher.matches('henchman@evil.org') is False



class TestEmailMatcherMultiplePatterns(object):
    def setup(self):
        self.matcher = EmailMatcher.from_pattern_string(
                '*@example.com,surveillance@*')

    def test_user(self):
        assert self.matcher.matches('user@example.com') is True

    def test_surveillance(self):
        assert self.matcher.matches('surveillance@security.net') is True

    def test_henchman(self):
        assert self.matcher.matches('henchman@evil.org') is False
