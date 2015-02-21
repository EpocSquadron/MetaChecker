
tests = {
    'twitter:card': (
        lambda head:
            head.select('meta[name="twitter:card"]')[0]['content'] != ''
    ),
    'twitter:site': (
        lambda head:
            head.select('meta[name="twitter:site"]')[0]['content'] != ''
    ),
    'twitter:title': (
        lambda head:
            head.select('meta[name="twitter:title"]')[0]['content'] != ''
    ),
    'twitter:description': (
        lambda head:
            head.select('meta[name="twitter:description"]')[0]['content'] != ''
    ),
    'twitter:image': (
        lambda head:
            head.select('meta[name="twitter:image"]')[0]['content'] != ''
    ),
}
