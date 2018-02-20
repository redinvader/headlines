import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route('/')
@app.route('/<publication>')
def bbc(publication='bbc'):
    return get_news( publication )


def get_news( pub ):
    feed= feedparser.parse( RSS_FEEDS[pub] )
    f = feed['entries'][0]
    return """
        <html><body>
            <h1>Headlines</h1>
            <b>{0}</b>
            <br/>
            <i>{1}</i>
            <br/>
            <p>{2}</p>
            <hr/>
        </body></html>
    """.format( f.get('title'), f.get('published'), f.get('summary') )

if __name__=='__main__':
    app.run( port=5000, debug=True )