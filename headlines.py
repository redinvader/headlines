import feedparser
from flask import Flask, render_template, request


app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route('/')
def get_news():
    
    print request.args
    query = request.args.get('publication')
    print query 
    
    if not query or query.lower() not in RSS_FEEDS:
        pub = 'bbc'
    else:
        pub = query.lower()
    print 'pub is ', pub
    feed = feedparser.parse( RSS_FEEDS[pub] )
    
    return render_template('home.html', articles = feed['entries'] )


if __name__=='__main__':
    app.run( port=5000, debug=True )