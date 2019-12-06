let loginDAL = require('../dal/login');
var passport = require('passport');
var LocalStrategy = require('passport-local').Strategy;
var bcrypt = require('bcryptjs');


function isAuthenticated (req, res, next) {


    if (req.isAuthenticated()) {
        let name = req.user.fName + ' ' + req.user.lName;

        res.cookie('FirstName', req.user.fName);
        res.cookie('LastName', req.user.lName);
        return next();
    } else {

        res.redirect('/');
    }
}

passport.serializeUser(function(user, done){

    done(null, user);
});

passport.deserializeUser(function(user, done){

    done(null, user);
});

passport.use(new LocalStrategy({passReqToCallback : true},
    async function(req, username, password, done)  {

        let user = await loginDAL.getLoginInfo(username);
        console.log(user);

        const userData = user[0];

        if (userData === null || userData === undefined) {

            return done(new Error ('Incorrect Email'));

        }


        if (userData.verifiedInd === 0){


            return done(new Error ('The account has not yet been verified.'));
        }
        if(userData.password===password){
          return done(null, userData);
        }
        else{
          return done(new Error('incorrect password'));
        }
        // bcrypt.compare(password, userData.password, function (err, isMatch) {
        //
        //     if (isMatch) {
        //         return done(null, userData);
        //     } else {
        //         return done(new Error ('Incorrect password'));
        //     }
        // });
    })
);

var authenticate = passport.authenticate('local', {
    successRedirect:'./homepage',
    failureRedirect:'./login',
    failureFlash: true
});

module.exports = {
    authenticate,
    isAuthenticated
};
