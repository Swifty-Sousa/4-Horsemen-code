
var express = require("express"),

    router = express.Router();
    let auth = require('../middleware/authentication');


    // Login route - default page
    router.get("/", function(req, res) {

        res.render("UserLogin", {
            title: "UserLogin",
        });
    });
    router.post('/login',auth.authenticate, async function(req, res, next){
        console.log("ahfjabajfb;dsbfjsabf;sadbf;kabsfsbfjdsafb");
        res.redirect('/');
    });
module.exports = router;
