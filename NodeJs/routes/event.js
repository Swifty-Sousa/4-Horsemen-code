var express = require("express"),
    router = express.Router();

    // event route - default page
    router.get("/", function(req, res) {
        res.render("Event", {
            title: "Event",
        });
    });
module.exports = router;
