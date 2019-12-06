var express = require("express"),
    router = express.Router();

    // profile route
    router.get("/", function(req, res) {
        res.render("Profile", {
            title: "Profile",
        });
    });
module.exports = router;
