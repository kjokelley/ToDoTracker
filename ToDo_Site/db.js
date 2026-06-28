const {Pool} = require('pg');

const pool = new Pool({
    user:'kyle',
    host:'192.168.254.83',
    database:'taskdb',
    password:'password',
    port:'5432'
});

module.exports = {
    query: (text, params) => pool.query(text,params),
}
