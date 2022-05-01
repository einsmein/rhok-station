import pg from 'pg';
export default new pg.Pool({
  user: 'guest',
  host: 'localhost',
  database: 'guest',
  password: 'guest',
  port: 5432,
})