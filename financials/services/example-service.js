import fetch from "node-fetch";
import pg from 'pg';
const pool = new pg.Pool({
  user: 'guest',
  host: 'localhost',
  database: 'guest',
  password: 'guest',
  port: 5432,
})

class ExampleService {

    constructor(url) {
        this.url = url
    }

    async pullData() {

    }

    async uploadData(data) {

    }

    async insertData() {
        const savePullData = await this.pullData()
        const saveUploadData = await this.uploadData(savePullData)
        return saveUploadData
    }

}

export default ExampleService;
