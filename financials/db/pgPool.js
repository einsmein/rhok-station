import pg from 'pg';
console.log(process.env.POSTGRES_HOST)
export default new pg.Pool({
  user: 'postgres',
  host: process.env.POSTGRES_HOST?process.env.POSTGRES_HOST:'localhost',
  database: process.env.POSTGRES_DB,
  password: process.env.POSTGRES_PASSWORD,
  port: 5432,
})
