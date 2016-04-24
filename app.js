var FeedParser = require('feedparser'),
    request = require('request');

var URL = 'XXXXXX',
    Webhook = 'XXXXXXX';

var req = request(URL),
    feedparser = new FeedParser();


req.on('response', function (res) {

  var stream = this;

  if (res.statusCode != 200) {
    return this.emit('error', new Error('Bad status code'));
  }
  stream.pipe(feedparser);
});

var weathers = [];

feedparser.on('readable', function() {

  var stream = this,
      meta = this.meta,
      item;

  while (item = stream.read()) {

    var data = item.title
                   .replace(/- Yahoo!天気・災害/g, "");
    weathers.push(data);
  }
});

feedparser.on('end', function() {

  var forecast =  weathers;
  console.log(forecast[0]);

  var options = {
    url: Webhook,
    form: 'payload={"text": "'+ forecast[0] +'"}',
    json: true
  };

  request.post(options, function (error, response, body) {
    if (!error && response.statusCode == 200) {
      console.log(body);
    } else{
      console.log('error: '+ response.statusCode);
    }
  });

});
