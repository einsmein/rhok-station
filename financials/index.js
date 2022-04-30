import ProjectsService from "./services/projects-service.js"
import AccountsService from "./services/accounts-service.js"

async function main(){
    await new AccountsService('https://restapi.e-conomic.com/accounts').insertData()
    //await new ProjectsService('https://apis.e-conomic.com/api/v12.0.0/projects').insertData()
}

main()