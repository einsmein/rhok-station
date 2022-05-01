import pg from 'pg';
console.log(process.env.POSTGRES_HOST)
export default new pg.Pool({
  user: 'guest',
  host: process.env.POSTGRES_HOST?process.env.POSTGRES_HOST:'localhost',
  database: 'guest',
  password: 'guest',
  port: 5432,
})