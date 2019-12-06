var express = require("express"),
    router = express.Router();

    // homepage route - default page
    router.get("/", function(req, res) {
        res.render("Homepage", {
            title: "Homepage",
        });
    });
module.exports = router;
