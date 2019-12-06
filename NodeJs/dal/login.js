const sequelize = require("../utilities/sequelize").sequelize;

async function getLoginInfo(username) {
    const sp = "sp_get_login_info";

    return await sequelize.query('SELECT * FROM ${sp}(:username)', {
        type: sequelize.QueryTypes.SELECT,
        replacements: {
            username: username,

        },
    });
}

module.exports = {
    getLoginInfo
};
