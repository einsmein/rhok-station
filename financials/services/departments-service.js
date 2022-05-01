import fetch from "node-fetch";
import pg from 'pg';
const pool = new pg.Pool({
  user: 'guest',
  host: 'localhost',
  database: 'guest',
  password: 'guest',
  port: 5432,
})

class DepartmentsService {

    constructor(url) {
        this.url = url
    }

    async pullData() {
        const res = await fetch(this.url,{
            method: 'GET',
            headers: {
                "x-appsecrettoken": "demo",
                "x-agreementgranttoken": "demo"
            }
        })
        //console.log(await res.json())
        return await res.json();
    }

    async uploadData(data) {
        console.log(data)
        data.collection.forEach(async(account) => {
            const {
                departmentNumber,
                name,

            } = account;    
            const insertScript = `INSERT INTO departments(
                number,
                name
                ) VALUES (
                    ${departmentNumber},
                    '${name}'
                )`;
        
            return await pool.query(insertScript,[])

            console.log(insertScript)
        });
        
    }

    async insertData() {
        const savePullData = await this.pullData()
        const saveUploadData = await this.uploadData(savePullData)
        //return saveUploadData
    }

}

export default DepartmentsService;
