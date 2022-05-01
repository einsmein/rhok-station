import fetch from "node-fetch";
import pool from "../db/pgPool.js";

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
        data.collection.forEach(async(distribution) => {
            const {
                departmentalDistributionNumber,
                name,
                barred,
                distributionType,
                distributions,
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
        
            const result = await pool.query(insertScript,[])
            distributions.forEach(async(department)=>{
                const {percentage} = department;
                const {departmentNumber} = department.department

                const insertScript = `INSERT INTO department_distribution(
                    department,
                    distribution,
                    percentage
                    ) VALUES (
                        ${departmentNumber},
                        ${departmentalDistributionNumber},
                        ${percentage}
                    )`;
                console.log(insertScript)
                await pool.query(insertScript,[])
            })
            
            return result

        });
    }

    async insertData() {
        const savePullData = await this.pullData()
        const saveUploadData = await this.uploadData(savePullData)
        return saveUploadData
    }

}

export default DistributionsService;
