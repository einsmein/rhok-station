import fetch from "node-fetch";
import pg from 'pg';
const pool = new pg.Pool({
  user: 'guest',
  host: 'localhost',
  database: 'guest',
  password: 'guest',
  port: 5432,
})

class AccountsService {

    constructor(url) {
        this.url = url
    }

    async pullData() {
        const res = await fetch('https://apis.e-conomic.com/api/v12.0.0/projects',{
            method: 'GET',
            headers: {
                'X-AgreementGrantToken': 'demo',
                'X-AppSecretToken': 'demo'
            }
        })
        return await res.json();
    }

    async uploadData(data) {
        data.forEach(async (account) => {
            const {
                number,
                name,
                projectGroupNumber,
                customerNumber,
                isClosed,
                mileage,
                isBarred,
                isMainProject,
                isMileageInvoiced,
                lastUpdated,
                description,
                deliveryDate,
                contactPersonId,
                objectVersion
            } = account

            const insertScript = `INSERT INTO projects(
                number,
                name,
                projectGroupNumber,
                customerNumber,
                isClosed,
                mileage,
                isBarred,
                isMainProject,
                isMileageInvoiced,
                lastUpdated,
                description,
                deliveryDate,
                contactPersonId,
                objectVersion
            ) VALUES (
                ${number},
                '${name}',
                '${projectGroupNumber}',
                ${customerNumber},
                '${isClosed}',
                ${mileage},
                '${isBarred}',
                '${isMainProject}',
                '${isMileageInvoiced}',
                '${lastUpdated}',
                '${description}',
                '${deliveryDate}',
                ${contactPersonId},
               ' ${objectVersion}'
            );`
            console.log(insertScript)
            await pool.query(insertScript,[])
        })
    }

    async insertData() {
        const savePullData = await this.pullData()
        const saveUploadData = await this.uploadData(savePullData)
        return saveUploadData
    }

}

export default AccountsService;
