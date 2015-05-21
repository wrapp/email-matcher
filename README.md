email-matcher
-------------

Matches emails using glob-like email patterns

```python
>>> matcher = EmailMatcher.from_pattern_string('*@example.com,surveillance@*')
>>> matcher.matches('user@example.com')
True
>>> matcher.matches('surveillance@security.net')
True
>>> matcher.matches('henchman@evil.org')
False
```
