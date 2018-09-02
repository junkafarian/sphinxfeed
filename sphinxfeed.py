# This application is derived from Dan Mackinlay's sphinxcontrib.feed package.
# The original can be found at http://bitbucket.org/birkenfeld/sphinx-contrib/src/tip/feed/

doc_trees = []  # for atelier

import unittest

import time

def parse_pubdate(pubdate):
    fmt = '%Y-%m-%d %H:%M'
    try:
        date = time.strptime(pubdate, fmt)
    except ValueError:
        date = time.strptime(pubdate + " 23:59", fmt)
    return date


def setup(app):
    """ see: http://sphinx.pocoo.org/ext/appapi.html
        this is the primary extension point for Sphinx
    """
    from sphinx.application import Sphinx
    if not isinstance(app, Sphinx): return
    app.add_config_value('feed_base_url', '', '')
    app.add_config_value('feed_description', '', '')
    app.add_config_value('feed_author', '', '')
    app.add_config_value('feed_field_name', 'Publish Date', '')
    app.add_config_value('feed_filename', 'rss.xml', 'html')
    
    app.connect('html-page-context', create_feed_item)
    app.connect('build-finished', emit_feed)
    app.connect('builder-inited', create_feed_container)
    
    #env.process_metadata deletes most of the docinfo, and dates
    #in particular.

def create_feed_container(app):
    from feedformatter import Feed
    feed = Feed()
    feed.feed['title'] = app.config.project
    feed.feed['link'] = app.config.feed_base_url
    feed.feed['author'] = app.config.feed_author
    feed.feed['description'] = app.config.feed_description
    
    if app.config.language:
        feed.feed['language'] = app.config.language
    if app.config.copyright:
        feed.feed['copyright'] = app.config.copyright
    app.builder.env.feed_feed = feed
    if not hasattr(app.builder.env, 'feed_items'):
        app.builder.env.feed_items = {}

def create_feed_item(app, pagename, templatename, ctx, doctree):
    """ Here we have access to nice HTML fragments to use in, say, an RSS feed.
    """
    
    env = app.builder.env
    metadata = app.builder.env.metadata.get(pagename, {})

    pubDate = metadata.get(app.config.feed_field_name, None)
    if not pubDate:
        return

    pubDate = parse_pubdate(pubDate)

    if pubDate > time.gmtime():
        return

    item = {
      'title': ctx.get('title'),
      'link': app.config.feed_base_url + '/' + ctx['current_page_name'] + ctx['file_suffix'],
      'description': ctx.get('body'),
      'pubDate': pubDate
    }
    if 'author' in metadata:
        item['author'] = metadata['author']
    env.feed_items[pagename] = item
    #Additionally, we might like to provide our templates with a way to link to the rss output file
    ctx['rss_link'] = app.config.feed_base_url + '/' + app.config.feed_filename
  
def emit_feed(app, exc):
    import os.path
    ordered_items = app.builder.env.feed_items.values()
    feed = app.builder.env.feed_feed
    ordered_items.sort(
      cmp=lambda x,y: cmp(x['pubDate'],y['pubDate']),
      reverse=True)
    for item in ordered_items:
        feed.items.append(item)
    
    path = os.path.join(app.builder.outdir,
                        app.config.feed_filename)
    feed.format_rss2_file(path)
    
    return
    # 20180204 The following code (pickle the environment and check
    # consistency at this point) caused an error when also bibtex was
    # installed. I deactivated it since I don't know why it's needed.
    
    from os import path
    from sphinx.application import ENV_PICKLE_FILENAME
    from sphinx.util.console import bold
    # save the environment
    builder = app.builder
    builder.info(bold('pickling environment... '), nonl=True)
    builder.env.topickle(path.join(builder.doctreedir, ENV_PICKLE_FILENAME))
    builder.info('done')
    
    # global actions
    builder.info(bold('checking consistency... '), nonl=True)
    builder.env.check_consistency()
    builder.info('done')

## Tests

# ... TODO

if __name__ == '__main__':
    unittest.main()
