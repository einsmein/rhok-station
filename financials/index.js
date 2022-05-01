import ProjectsService from "./services/projects-service.js"
import AccountsService from "./services/accounts-service.js"
import DepartmentsService from "./services/departments-service.js"
import DistributionsService from "./services/distributions-service.js"
async function main(){
    await new DepartmentsService('https://restapi.e-conomic.com/departments').insertData()
    await new ProjectsService('https://apis.e-conomic.com/api/v12.0.0/projects').insertData()
    await new DistributionsService('https://restapi.e-conomic.com/departmental-distributions').insertData()
    await new AccountsService('https://restapi.e-conomic.com/accounts').insertData()

}

main()