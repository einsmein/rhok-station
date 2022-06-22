import os

from sqlalchemy import create_engine

from services.departments_service import DepartmentsService
from services.accounts_service import AccountsService

REST_URL = 'https://restapi.e-conomic.com/'
REST_V12_URL = 'https://apis.e-conomic.com/api/v12.0.0/'

def main():
    PG_USER = os.environ.get('PG_USER')
    PG_PASSWORD = os.environ.get('PG_PASSWORD')
    url = f'postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@localhost:5432/'
    engine = create_engine(url)

    DepartmentsService(REST_URL+'departments',engine).insert_data()

    AccountsService(REST_URL+'accounts',engine).insert_data()

main()
"""
    await new DepartmentsService(REST_URL+'departments').insertData()
    await new ProjectsService(REST_V12_URL+'projects').insertData()
    await new DistributionsService(REST_URL+'departmental-distributions').insertData()


}

import ProjectsService from "./services/projects-service.js"

import DepartmentsService from "./services/departments-service.js"
import DistributionsService from "./services/distributions-service.js"
const REST_URL = 'https://restapi.e-conomic.com/'
const REST_V12_URL = 'https://apis.e-conomic.com/api/v12.0.0/'
async function main(){
    await new DepartmentsService(REST_URL+'departments').insertData()
    await new ProjectsService(REST_V12_URL+'projects').insertData()
    await new DistributionsService(REST_URL+'departmental-distributions').insertData()


}

main()
"""