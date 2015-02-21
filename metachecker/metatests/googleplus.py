
tests = {
    'name': (
        lambda head:
            head.select('meta[itemprop="name"]')[0]['content'] != ''
    ),
    'description': (
        lambda head:
            head.select('meta[itemprop="description"]')[0]['content'] != ''
    ),
    'image': (
        lambda head:
            head.select('meta[itemprop="image"]')[0]['content'] != ''
    ),
}
