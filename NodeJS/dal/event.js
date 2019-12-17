const sequelize = require("../utilities/sequelize").sequelize;

async function getPreviousEvents(username) {
    var query="SELECT ev.title, ev.discription, ev.date FROM combination com inner join events ev on ev.id=com.eventId inner join students st on st.id=com.userId AND st.username = :userEmail LIMIT 2"
      return await sequelize.query(query, {
        replacements: {
            userEmail: username,
        },
      type: sequelize.QueryTypes.SELECT,
    });
}
module.exports = {
    getPreviousEvents
};
