import ProjectsService from "./services/projects-service.js"
import AccountsService from "./services/accounts-service.js"
import DepartmentsService from "./services/departments-service.js"
import DistributionsService from "./services/distributions-service.js"
const REST_URL = 'https://restapi.e-conomic.com/'
const REST_V12_URL = 'https://apis.e-conomic.com/api/v12.0.0/'
async function main(){
    await new DepartmentsService(REST_URL+'departments').insertData()
    await new ProjectsService(REST_V12_URL+'projects').insertData()
    await new DistributionsService(REST_URL+'departmental-distributions').insertData()
    await new AccountsService(REST_URL+'accounts').insertData()

}

main()