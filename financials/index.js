import AccountsService from "./services/accounts-service.js"


async function main(){
    await new AccountsService('https://apis.e-conomic.com/api/v12.0.0/projects').insertData()
}

main()