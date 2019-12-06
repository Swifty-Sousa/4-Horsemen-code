
var express = require('express');
var path = require('path');
var app = express();
const bodyParser = require('body-parser');
const passport = require('passport');


app.set('views', path.join(__dirname, 'views'));
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');

app.use(express.static(path.join(__dirname,'public')));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(passport.initialize());
app.use(passport.session());

const routes = require("./routes/login");
const homepage=require("./routes/homepage");
const profile=require("./routes/profile");
const events=require("./routes/event");

app.use("/login", routes);
app.use("/homepage", homepage);
app.use("/profile", profile);
app.use("/event", events);

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});

module.exports.app = app;
