
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