const request = require("request"),
  xml2js = require("xml2js");

module.exports = (req, res) => {
  request("https://medium.com/feed/@Cryptacular", function(
    error,
    response,
    body
  ) {
    if (!error) {
      xml2js.parseString(body, function(error, result) {
        console.log("/posts called at " + new Date());
        res.json(result.rss.channel);
      });
    } else {
      return res.status(err.status || 500).send();
    }
  });
};
