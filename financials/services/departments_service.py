import json
import requests

from sqlalchemy.orm import Session

from models.department import Department

class DepartmentsService:

    def __init__(self, url, engine):
        self.url = url
        self.engine = engine

    def pull_data(self):
        res = requests.get(self.url,
            headers= {
                "x-appsecrettoken": "demo",
                "x-agreementgranttoken": "demo"
            }
        )
        return json.loads(res.text)

    def upload_data(self,data):
        
        with Session(self.engine) as session:
            for department in data['collection']:
                query = session.query(Department).where(
                    Department.department_number == department['departmentNumber']
                )
                existing_department = query.first()
                if existing_department:
                    existing_department.name = department['name']
                    session.add(existing_department)
                else:
                    new_account = Department(
                        department_number = department['departmentNumber'],
                        name = department['name'],
                    )
                    session.add(new_account)
            session.commit()
            
    def insert_data(self):
        data = self.pull_data()
        self.upload_data(data)
