from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host(r'en', 'core.en_urls', name='en'),
    host(r'pt', 'core.pt_urls', name='pt'),
    host(r'www', 'core.www_urls', name='www'),
    # host(r'admin', settings.ROOT_URLCONF, name='admin'),
)
