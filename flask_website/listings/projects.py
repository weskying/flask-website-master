# -*- coding: utf-8 -*-
from urlparse import urlparse
from flask import Markup


class Project(object):
    def __init__(self, name, url, description, source=None):
        self.name = name
        self.url = url
        self.description = Markup(description)
        self.source = source

    @property
    def host(self):
        if self.url is not None:
            return urlparse(self.url)[1]

    @property
    def sourcehost(self):
        if self.source is not None:
            return urlparse(self.source)[1]

    def to_json(self):
        rv = vars(self).copy()
        rv['description'] = unicode(rv['description'])
        return rv


projects = {
    'websites': [
        Project('Flask Website', 'http://flask.pocoo.org/', '''
            <p>
              The website of the Flask microframework itself including the
              mailinglist interface, snippet archive and extension registry.
        '''),
        Project('Brightonpy', 'http://brightonpy.org/', '''
            <p>
              The website of the Brighton Python User Group
        ''', source='http://github.com/j4mie/brightonpy.org/'),
        Project(u's h o r e … software development', 'http://shore.be/', '''
            <p>Corporate website of Shore Software Development.
        '''),
        Project(u'ROCKYOU.fm', 'https://www.rockyou.fm/', '''
            <p>
              ROCKYOU.fm is a german internet radio station and webzine
              featuring mostly metal and hard rock. Since 2012 the DJs and
              reporters provide their listeners with news, reviews, feature
              shows and interviews.
        '''),
        Project(u'MetalSpy', 'https://www.metalspy.de/', '''
            <p>
              MetalSpy.de is the portfolio website of a german hobby
              photographer featuring mainly photos of metal bands,
              festivals, fantasy conventions and cosplay.
        '''),
        Project('ThadeusB\'s Website', 'http://thadeusb.com/', u'''
            <p>
              Personal website of ThadeusB.
        '''),
        Project('Blueslug', 'http://blueslug.com/', u'''
            <p>
              A flask-powered anti-social delicious clone
        '''),
        Project('DotShare', 'http://dotshare.it/', u'''
            <p>
              Socially driven website for sharing Linux/Unix dot files.
        '''),
        Project(
            'sopython', 'http://sopython.com/',
            '<p>Site of the Python chat room on Stack Overflow. '
            'Includes OAuth authentication, a wiki, and a growing, '
            'searchable list of "canonical" answers to Python '
            'questions on SO.</p>',
            source='https://github.com/sopython/sopython-site'
        )
    ],
    'apps': [
        Project('hg-review', None, '''
            <p>
              hg-review is a code review system for Mercurial.  It is available
              GPL2 license.
        ''', source='http://bitbucket.org/sjl/hg-review/'),
        Project('Ryshcate', None, '''
            <p>
              Ryshcate is a Flask powered pastebin with sourcecode
              available.
        ''', source='http://bitbucket.org/leafstorm/ryshcate/'),
        Project(u'Übersuggest Keyword Suggestion Tool', None, u'''
            <p>
              Übersuggest is a free tool that exploit the Google
              suggest JSON API to get keyword ideas for your search marketing
              campaign (PPC or SEO).
        ''', source='http://bitbucket.org/esaurito/ubersuggest'),
        Project('Have they emailed me?', None, '''
            <p>
              A mini-site for checking Google's GMail feed with Oauth.
        ''', source='http://github.com/lincolnloop/emailed-me'),
        Project('Remar.kZ', None, '''
            <p>
               Sometimes you use someone else's computer and find something
               neat and interesting.  Store it on Remar.kZ without having
               to enter your credentials.
        ''', source='http://bitbucket.org/little_arhat/remarkz'),
        Project('Domination', None, u'''
            <p>
              Domination is a clone of a well-known card game.
        ''', source='https://bitbucket.org/xoraxax/domination/'),
        Project('jitviewer', None, '''
            <p>
              web-based tool to inspect the output of PyPy JIT log
        ''', source='https://bitbucket.org/pypy/jitviewer'),
        Project('blohg', 'http://blohg.org/', '''
            <p>
              A mercurial based blog engine.
        ''', source='https://github.com/rafaelmartins/blohg'),
        Project('pidsim-web', None, '''
            <p>
              PID Controller simulator.
        ''', source='https://github.com/rafaelmartins/pidsim-web'),
        Project('HTTPBin', 'http://httpbin.org/', u'''
            <p>
              An HTTP request & response service.
        ''', source='https://github.com/kennethreitz/httpbin'),
        Project('Flask-Pastebin', None, u'''
            <p>
              Pastebin app with Flask and a few extensions that does Facebook
              connect as well as realtime push notifications with socket.io
              and juggernaut.
        ''', source='https://github.com/mitsuhiko/flask-pastebin'),
        Project('newsmeme', None, u'''
            <p>
              A hackernews/reddit clone written with Flask and
              various Flask extensions.
        ''', source='https://bitbucket.org/danjac/newsmeme'),
        Project('Indico', 'https://getindico.io/', u'''
            <p>
              Indico is a full-fledged meeting and conference management
              system developed at CERN. It includes advanced features such
              as integration with collaborative systems, a plugin system
              and support for SSO-based authentication.
        ''', source='https://github.com/indico/indico/'),
        Project('SayHello', 'http://sayhello.helloflask.com', u'''
            <p>
              A simple message board.
        ''', source='https://github.com/greyli/sayhello'),
        Project('Bluelog', 'http://bluelog.helloflask.com', u'''
            <p>
              A blog engine that supports category and resource management.
        ''', source='https://github.com/greyli/bluelog'),
        Project('Albumy', 'http://albumy.helloflask.com', u'''
            <p>
              A full-featured photo-sharing social networking.
        ''', source='https://github.com/greyli/albumy'),
        Project('Todoism', 'http://todoism.helloflask.com', u'''
            <p>
              A to-do application implements as SPA, it supports 
              i18n (Flask-Babel) and provides web APIs.
        ''', source='https://github.com/greyli/todoism'),
        Project('CatChat', 'http://catchat.helloflask.com', u'''
            <p>
              A chat room based on WebSocket (Flask-Socket-IO), fetured 
              with Markdown support and code syntax highlighting.
        ''', source='https://github.com/greyli/catchat'),
    ]

}

# order projects by name
for _category in projects.itervalues():
    _category.sort(key=lambda x: x.name.lower())
del _category
