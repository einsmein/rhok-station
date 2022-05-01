import fetch from "node-fetch";
import pool from "../db/pgPool.js";

class AccountsService {

    constructor(url) {
        this.url = url
    }

    async pullData() {
        const res = await fetch(this.url,{
            method: 'GET',
            headers: {
                'X-AgreementGrantToken': 'demo',
                'X-AppSecretToken': 'demo'
            }
        })
        return await res.json();
    }


    async pullEntries(accountNumber,url){
        const resYears = await this.pullAccountYears(accountNumber)
        const years = resYears.collection.map(({year})=>year)
        years.forEach(async(year)=>{
            const res = await fetch('https://restapi.e-conomic.com/accounts/'+accountNumber+'/accounting-years/'+year+'/entries',{
            method: 'GET',
            headers: {
                'X-AgreementGrantToken': 'demo',
                'X-AppSecretToken': 'demo'
            }
            })
            const entries = (await res.json()).collection
            entries.forEach(async(entry)=>{
                const {
                    account
                    ,amount
                    ,amountInBaseCurrency
                    ,currency
                    ,date
                    ,dueDate
                    ,departmentalDistribution
                    ,entryNumber
                    ,text
                    ,entryType
                    ,vatAccount
                    ,voucherNumber
                    ,quantity1
                    ,quantity2
                    ,bookedInvoice
                    ,invoiceNumber  
                } = entry;
               
                const insertScript = `INSERT INTO entries(
                    account,
                    amount,
                    amountInBaseCurrency,
                    currency,
                    date,
                    dueDate,
                    departmentalDistribution,
                    entryNumber,
                    text,
                    entryType,
                    vatAccount,
                    voucherNumber,
                    quantity1,
                    quantity2,
                    bookedInvoice,
                    invoiceNumber
                ) VALUES (
                    ${account.accountNumber}
                        ,${amount}
                        ,${amountInBaseCurrency}
                        ,'${currency}'
                        ,${date?"'"+date+"'":'NULL'}
                        ,${dueDate?"'"+dueDate+"'":'NULL'}
                        ,${departmentalDistribution?departmentalDistribution.departmentalDistributionNumber:'NULL'}
                        ,${entryNumber}
                        ,'${text}'
                        ,'${entryType}'
                        ,'${vatAccount?vatAccount.vatCode:'NULL'}'
                        ,${voucherNumber}
                        ,${quantity1?quantity1:'NULL'}
                        ,${quantity2?quantity2:'NULL'}
                        ,${bookedInvoice?bookedInvoice.bookedInvoiceNumber:'NULL'}
                        ,${invoiceNumber?invoiceNumber:'NULL'}
                );`
                return await pool.query(insertScript,[])

            })
        })
        
    }

    async pullAccountYears(accountNumber){
        const res = await fetch('https://restapi.e-conomic.com/accounts/'+accountNumber+'/accounting-years',{
            method: 'GET',
            headers: {
                'X-AgreementGrantToken': 'demo',
                'X-AppSecretToken': 'demo'
            }
        })
        return await res.json();
    }

    async uploadData(data) {
        
        data.collection.forEach(async(account) => {
            const {
                accountNumber,
                accountType,
                balance,
                blockDirectEntries,
                debitCredit,
                name,
            } = account;
            
            const insertScript = `INSERT INTO accounts(
                accountNumber,
                accountType,
                balance,
                blockDirectEntries,
                debitCredit,
                name) VALUES (
                    ${accountNumber},
                    '${accountType}',
                    ${balance},
                    '${blockDirectEntries}',
                    '${debitCredit}',
                    '${name}'
                )`;
            const response = await pool.query(insertScript,[])
            this.pullEntries(accountNumber,'').catch(err=>{console.log(err)})

            return response

        });
        
    }

    async insertData() {
        const savePullData = await this.pullData()
        const saveUploadData = await this.uploadData(savePullData)
        //return saveUploadData
    }

}

export default AccountsService;
