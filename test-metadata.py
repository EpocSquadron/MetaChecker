#!/usr/bin/python

from metachecker.SEOMetadataChecker import SEOMetadataChecker
from metachecker.metatests import basic, twitter

html_doc = """
<!DOCTYPE html>
<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js ie8 oldie" lang="en"> <![endif]-->
<!--[if IE 9]>    <html class="no-js ie9" lang="en"> <![endif]-->
<!--[if gt IE 9]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">

	{exp:ce_cache:it id="head-metadata"}
	<title>{exp:surgeeo:title}</title>
	<meta name="description" content="{exp:surgeeo:description}" />
	<meta name="author" content="Thingy">

	{!-- Facebook Metadata /--}
	{!-- <meta property="fb:app_id" content="" /> --}
	<meta property="og:url" content="{if '{exp:surgeeo:og_url}'}{exp:surgeeo:og_url}{if:else}{current_url}/{/if}" />
	<meta property="og:title" content="{exp:surgeeo:title}"/>
	<meta property="og:description" content="{if '{exp:surgeeo:og_description}'}{exp:surgeeo:og_description}{if:else}{exp:surgeeo:description}{/if}"/>
	<meta property="og:image" content="{exp:surgeeo:og_img}" />

	{!-- Google+ Metadata /--}
	<meta itemprop="name" content="{exp:surgeeo:title}">
	<meta itemprop="description" content="{if '{exp:surgeeo:og_description}'}{exp:surgeeo:og_description}{if:else}{exp:surgeeo:description}{/if}">
	<meta itemprop="image" content="{exp:surgeeo:og_img}">

	{!-- Twitter Card Metadata /--}
	<meta name="twitter:card" content="summary" />
	<meta name="twitter:site" content="@epocsquadron" />
	<meta name="twitter:title" content="{if '{exp:surgeeo:twtr_title}'}{exp:surgeeo:twtr_title}{if:else}{exp:surgeeo:title}{/if}" />
	<meta name="twitter:description" content="{if '{exp:surgeeo:twtr_description}'}{exp:surgeeo:twtr_description}{if:else}{exp:surgeeo:description}{/if}" />
	<meta name="twitter:image"  content="{exp:surgeeo:twtr_img}" />
	{/exp:ce_cache:it}

	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">

	<link rel="icon" href="/favicon-16x16.png" sizes="16x16" />
	<link rel="icon" href="/favicon-32x32.png" sizes="32x32" />
	<link rel="icon" href="/favicon-96x96.png" sizes="96x96" />
	<link rel="icon" href="/favicon-160x160.png" sizes="160x160" />
	<link rel="icon" href="/favicon-192x192.png" sizes="192x192" />
	<link rel="apple-touch-icon" href="/apple-touch-icon-57x57.png" sizes="57x57">
	<link rel="apple-touch-icon" href="/apple-touch-icon-60x60.png" sizes="60x60">
	<link rel="apple-touch-icon" href="/apple-touch-icon-72x72.png" sizes="72x72">
	<link rel="apple-touch-icon" href="/apple-touch-icon-76x76.png" sizes="76x76">
	<link rel="apple-touch-icon" href="/apple-touch-icon-114x114.png" sizes="114x114">
	<link rel="apple-touch-icon" href="/apple-touch-icon-120x120.png" sizes="120x120">
	<link rel="apple-touch-icon" href="/apple-touch-icon-144x144.png" sizes="144x144">
	<link rel="apple-touch-icon" href="/apple-touch-icon-152x152.png" sizes="152x152">
	<meta name="msapplication-TileColor" content="#603cba">
	<meta name="msapplication-TileImage" content="/mstile-144x144.png">

	{exp:ce_cache:it id="head-rels"}
	{if layout:has_rss}
	<link rel="alternate" href="{structure:page:url}rss/" type="application/atom+xml" title="Thingy" charset="utf-8">
	{/if}

	{if paginated || layout:archive == 'true'}<link rel="canonical" href="{structure:page:url}">{/if}
	{if layout:pagination_prev}<link rel="prev" href="{layout:pagination_prev}">{/if}
	{if layout:pagination_next}<link rel="next" href="{layout:pagination_next}">{/if}
	{/exp:ce_cache:it}


	<link href='http://fonts.googleapis.com/css?family=Lato:400,700|Montserrat:400,700|Crimson+Text:600italic' rel='stylesheet' type='text/css'>
	<link href="/dist/css/main.css" rel="stylesheet" type="text/css">
	<link href="/dist/css/gigya.css" rel="stylesheet" type="text/css">

	<!--[if lt IE 9]>
		<link href="/dist/css/shame.css" rel="stylesheet" type="text/css">
		<script src="/bower_components/respond/dest/respond.min.js"></script>
		<script src="/dist/js/polyfill.js"></script>
		<script>
			svgeezy.init('nocheck', 'png');
		</script>
	<![endif]-->

</head>
<body>

{if layout:use_header != 'n'}
	{snip-header}
{/if}

{layout:contents}

{if layout:use_footer != 'n'}
	{snip-footer}
{/if}

{snip-scripts}

{layout:after_js}

</body>
</html>

"""


try:
	checker = SEOMetadataChecker(html_doc)
	checker.register_tests(basic.tests)
	checker.register_tests(twitter.tests)
	checker.test_all()

except Exception as e:
	print('Error while running tests: ', e)
