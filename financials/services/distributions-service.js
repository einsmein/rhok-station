import fetch from "node-fetch";
import pg from 'pg';
const pool = new pg.Pool({
  user: 'guest',
  host: 'localhost',
  database: 'guest',
  password: 'guest',
  port: 5432,
})

class DistributionsService {

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
        return await res.json();
    }

    async uploadData(data) {
        console.log(data)
        data.collection.forEach(async(distribution) => {
            const {
                departmentalDistributionNumber,
                name,
                barred,
                distributionType,
            } = distribution;    
            const insertScript = `INSERT INTO distributions(
                departmentalDistributionNumber,
                name,
                barred,
                distributionType
                ) VALUES (
                    ${departmentalDistributionNumber},
                    '${name}',
                    '${barred}',
                    '${distributionType}'
                )`;
        
            return await pool.query(insertScript,[])

        });
    }

    async insertData() {
        const savePullData = await this.pullData()
        const saveUploadData = await this.uploadData(savePullData)
        return saveUploadData
    }

}

export default DistributionsService;
