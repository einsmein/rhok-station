import json
import requests

from sqlalchemy.orm import Session

from models.project import Project
from helpers.helpers import getKeyValue
class ProjectsService:

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
        print(data)
        with Session(self.engine) as session:
            for project in data:
                print(project)
                query = session.query(Project).where(
                    Project.number == project['number']
                )
                existing_project = query.first()
                if existing_project:
                    existing_project.number = project['number']
                    existing_project.name = project['name']
                    existing_project.project_group_number = project['projectGroupNumber']
                    existing_project.closed_date = project['closedDate']
                    existing_project.contact_person_id = project['contactPersonId']
                    existing_project.cost_price = project['cost_price']
                    existing_project.customer_number = getKeyValue(project, 'customerNumber')
                    existing_project.delivery_date = project['deliveryDate']
                    existing_project.delivery_location_number = project['deliveryLocationNumber']
                    existing_project.department_number = getKeyValue(project, 'departmentNumber')
                    existing_project.description = project['description']
                    existing_project.fixed_price = project['fixed_price']
                    existing_project.invoiced_total = project['invoiceTotal']
                    existing_project.is_barred = project['isBarred']
                    existing_project.is_closed = project['isClosed']
                    existing_project.is_main_project = project['isMainProject']
                    existing_project.is_mileage_invoiced = project['isMileageInvoiced']
                    existing_project.last_updated = project['lastUpdated']
                    existing_project.main_project_number = project['mainProjectNumber']                    
                    existing_project.is_closed = project['isClosed']
                    existing_project.mileage = project['mileage']
                    
                    
                    existing_project.object_version = project['objectVersion']
                    session.add(existing_project)
                else:
                    new_project = Project(
                        number = project['number'],
                        name = project['name'],
                        project_group_number = project['projectGroupNumber'],
                        customer_number = getKeyValue(project, 'customerNumber'),
                        is_closed = project['isClosed'],
                        mileage = project['mileage'],
                        is_barred = project['isBarred'],
                        is_main_project = project['isMainProject'],
                        is_mileage_invoiced = project['isMileageInvoiced'],
                        last_updated = project['lastUpdated'],
                        description = project['description'],
                        delivery_date = project['deliveryDate'],
                        contact_person_id = project['contactPersonId'],
                        object_version = project['objectVersion']
                    )
                    session.add(new_project)
            session.commit()
            
    def insert_data(self):
        data = self.pull_data()
        self.upload_data(data)
