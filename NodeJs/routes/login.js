
var express = require("express"),

    router = express.Router();
    let auth = require('../middleware/authentication');

    router.get("/", function(req, res) {
        res.render("UserLogin", {
            title: "UserLogin",
        });
    });
    router.post('/login',auth.authenticate, async function(req, res, next){
        res.redirect('/');
    });
module.exports = router;
