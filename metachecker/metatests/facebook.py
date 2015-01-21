
tests = {
	'fb:app_id': (lambda head: head.select('meta[property="fb:app_id"]')[0]['content'] != ''),
	'og:url': (lambda head: head.select('meta[property="og:url"]')[0]['content'] != ''),
	'og:title': (lambda head: head.select('meta[property="og:title"]')[0]['content'] != ''),
	'og:description': (lambda head: head.select('meta[property="og:description"]')[0]['content'] != ''),
	'og:image': (lambda head: head.select('meta[property="og:image"]')[0]['content'] != ''),
}
