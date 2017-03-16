# -*- coding: utf-8 -*-

import requests
from dragnet import content_extractor, content_comments_extractor

# fetch HTML
url = 'http://news.ifeng.com/a/20160930/50050292_0.shtml'
r = requests.get(url)

# get main article without comments
content = content_extractor.analyze(r.content)
print content

# get article and comments
content_comments = content_comments_extractor.analyze(r.content)

print content_comments