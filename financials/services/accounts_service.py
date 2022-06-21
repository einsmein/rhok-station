import json
import requests

from sqlalchemy.orm import Session

from models.account import Account

class AccountsService:
    """
    Class handling the pulling of data from
    e-conomic and saving it to db
    """
    def __init__(self,url,engine):
        self.url = url
        self.engine = engine

    def pull_data(self):
        """
        fetches data
        """
        res = requests.get(
            self.url,
            headers={
                'X-AgreementGrantToken': 'demo',
                'X-AppSecretToken': 'demo'
            }
        )
        return json.loads(res.text)

    def upload_data(self,data):
        """
        Uploads data in case of conflict of PK it updates
        """
        with Session(self.engine) as session:
            for account in data['collection']:
                query = session.query(Account).where(
                    Account.account_number == account['accountNumber']
                )
                existing_account = query.first()
                if existing_account:
                    existing_account.account_type = account['accountType']
                    existing_account.balance = account['balance']
                    existing_account.block_direct_entries = account['blockDirectEntries']
                    existing_account.debit_credit = account['debitCredit']
                    existing_account.name = account['name']
                    session.add(existing_account)
                else:
                    new_account = Account(
                        account_number = account['accountNumber'],
                        account_type = account['accountType'],
                        balance = account['balance'],
                        block_direct_entries= account['blockDirectEntries'],
                        debit_credit = account['debitCredit'],
                        name = account['name'],
                    )
                    session.add(new_account)
            session.commit()

    def insert_data(self):
        """
        calls sub routines for fetching and storing
        """
        data = self.pull_data()
        self.upload_data(data)
