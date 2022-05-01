import fetch from "node-fetch";
import pool from "../db/pgPool.js";

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
        data.collection.forEach(async(account) => {
            const {
                departmentNumber,
                name,
                distributions
            } = account;
            const insertScript = `INSERT INTO departments(
                number,
                name
                ) VALUES (
                    ${departmentNumber},
                    '${name}'
                )`;
        
            return await pool.query(insertScript,[])

        });
        
    }

    async insertData() {
        const savePullData = await this.pullData()
        const saveUploadData = await this.uploadData(savePullData)
        //return saveUploadData
    }

}

export default DepartmentsService;
