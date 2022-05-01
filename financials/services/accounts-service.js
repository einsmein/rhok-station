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
        const res = await fetch(this.url,{
            method: 'GET',
            headers: {
                'X-AgreementGrantToken': 'demo',
                'X-AppSecretToken': 'demo'
            }
        })
        return await res.json();
    }

    async uploadData(data) {
        
        data.collection.forEach(async(account) => {
            const {
                accountNumber,
                accountType,
                balance,
                blockDirectEntries,
                debitCredit,
                name,
            } = account;    
            const insertScript = `INSERT INTO accounts(
                accountNumber,
                accountType,
                balance,
                blockDirectEntries,
                debitCredit,
                name) VALUES (
                    ${accountNumber},
                    '${accountType}',
                    ${balance},
                    '${blockDirectEntries}',
                    '${debitCredit}',
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

export default AccountsService;
