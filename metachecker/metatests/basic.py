
tests = {
    'title': (lambda head: head.title.string != ''),
    'description': (
        lambda head:
            head.select('meta[name="description"]')[0]['content'] != ''
    ),
    'keywords': (
        lambda head:
            head.select('meta[name="keywords"]')[0]['content'] != ''
    ),
}
