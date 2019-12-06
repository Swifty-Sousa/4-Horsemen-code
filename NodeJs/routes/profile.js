var express = require("express"),
    router = express.Router();

    // profile route
    router.get("/", function(req, res) {
        res.render("Profile", {
            title: "Profile",
        });
    });
    router.post('/update',function(req, res){
      console.log(req.body);
      // we need to update our database with profile submission data here! need new sequelize stuff
      res.status(200).send(req.body);
    });
module.exports = router;
