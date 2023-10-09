import os
import psycopg2

def get_time():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    with conn.cursor() as cur:
        cur.execute("SELECT now()")
        res = cur.fetchall()
        conn.commit()
        print("Here is the time: ", res)
        
def get_companies():
    try:
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
        with conn.cursor() as cur:
            cur.execute("SELECT id, company_name, erp_code, address, web_address, status FROM company;")
            res = cur.fetchall()
            conn.commit()
            count = cur.rowcount
            return (res, count)
    except (Exception, psycopg2.Error) as error:
        error_str = ("Failed to get records from company table:", error)
        print(error_str)
        return error_str
    finally:
        if conn:
            conn.close()
            print("PostgreSQL connection is closed")
            
def get_company(id):
    try:
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
        with conn.cursor() as cur:
            cur.execute("SELECT id, company_name, erp_code, address, web_address, status FROM company WHERE id = %s;", (id,))
            res = cur.fetchone()
            conn.commit()
            return res
    except (Exception, psycopg2.Error) as error:
        error_str = ("Failed to get records from company table:", error)
        print(error_str)
        return error_str
    finally:
        if conn:
            conn.close()
            print("PostgreSQL connection is closed")
    
def add_company(company_name, erp_code, address, web_address):
    try:
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
        with conn.cursor() as cur:
            isvalid = True
            cur.execute("SELECT * FROM company WHERE company_name = %s;", (company_name,))
            cur.fetchall()
            conn.commit()
            if cur.rowcount != 0:
                return "There is a company with this name"
            cur.execute("SELECT * FROM company WHERE web_address = %s;", (web_address,))
            cur.fetchall()
            conn.commit()
            if cur.rowcount != 0:
                return "There is a company with this email address"
            cur.execute("SELECT * FROM company WHERE erp_code = %s;", (erp_code,))
            cur.fetchall()
            conn.commit()
            if cur.rowcount != 0:
                return "There is a company with this ERP code"
            cur.execute("INSERT INTO company (company_name,erp_code,address,web_address) VALUES (%s,%s,%s,%s);", (company_name, erp_code, address, web_address))
            conn.commit()
            count = cur.rowcount
            return "New company inserted successfully"
    except (Exception, psycopg2.Error) as error:
        error_str = ("Failed to insert record into company table:",error)
        print(error_str)
        return error_str
    finally:
        if conn:
            conn.close()
            print("PostgreSQL connection is closed")
        
def update_company(id, company_name, erp_code, address, web_address):
    try:
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
        with conn.cursor() as cur:
            cur.execute("UPDATE company SET company_name = %s, erp_code = %s, address = %s, web_address = %s WHERE id = %s;", (company_name, erp_code, address, web_address, id))
            conn.commit()
            return "Company updated successfully"
    except (Exception, psycopg2.Error) as error:
        error_str = ("Failed to update record into company table:",error)
        print(error_str)
        return error_str
    finally:
        if conn:
            conn.close()
            print("PostgreSQL connection is closed")