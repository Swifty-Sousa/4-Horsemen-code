var express = require("express"),
    router = express.Router();

    // Login route - default page
    router.get("/", function(req, res) {
        res.render("Profile", {
            title: "Profile",
        });
    });
module.exports = router;
