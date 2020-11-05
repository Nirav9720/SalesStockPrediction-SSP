from base.com.dao import connection


class Dao:
    def login(self, data):
        conn = connection()
        cursor = conn.cursor()
        sql_admin = """
        select admin_name,admin_email,admin_password from adminData where admin_email='{}' and admin_password='{}'
        """.format(data.user_email, data.user_password)

        sql_wholesaler = """
        select user_full_name,user_email,user_password from user_wholesaler where user_email='{}' and user_password='{}'
        """.format(data.user_email, data.user_password)

        sql_retailer = """
        select user_full_name,user_email,user_password from user_retailer where user_email='{}' and user_password='{}'
        """.format(data.user_email, data.user_password)

        resultadmin = cursor.execute(sql_admin)
        data_admin = cursor.fetchone()
        resultwholesaler = cursor.execute(sql_wholesaler)
        data_wholesaler = cursor.fetchone()
        resultretailer = cursor.execute(sql_retailer)
        data_retailer = cursor.fetchone()

        identify_admin = "admin"
        identify_wholesaler = "wholesaler"
        identify_retailer = "retailer"

        if resultadmin == 1:
            print("From admin...")
            cursor.close()
            conn.close()
            return resultadmin, data_admin, identify_admin
        elif resultwholesaler == 1:
            print("From wholesaler...")
            cursor.close()
            conn.close()
            return resultwholesaler, data_wholesaler, identify_wholesaler
        elif resultretailer == 1:
            print("From retailer...")
            cursor.close()
            conn.close()
            return resultretailer, data_retailer, identify_retailer
        else:
            print("None...")
            cursor.close()
            conn.close()
            return 0, "none", "invalid"

    def register(self, data, user):
        if user == "wholesaler":
            conn = connection()
            cursor = conn.cursor()
            sql = """
            INSERT INTO user_wholesaler
            (user_full_name, user_email, user_password, user_contact, user_company_name, user_org_email, user_org_contact, user_org_address, user_firm_type) 
            VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
            """.format(
                data.user_full_name,
                data.user_email,
                data.user_password,
                data.user_contact,
                data.user_company_name,
                data.user_org_email,
                data.user_org_contact,
                data.user_org_address,
                data.user_firm_type
            )
            result = cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return result
        elif user == "retailer":
            conn = connection()
            cursor = conn.cursor()
            sql = """
            INSERT INTO user_retailer
            (user_full_name, user_email, user_password, user_contact, user_company_name, user_org_email, user_org_contact, user_org_address, user_firm_type) 
            VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
            """.format(
                data.user_full_name,
                data.user_email,
                data.user_password,
                data.user_contact,
                data.user_company_name,
                data.user_org_email,
                data.user_org_contact,
                data.user_org_address,
                data.user_firm_type
            )
            result = cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return result

    def show(self, user):
        if user == "wholesaler":
            conn = connection()
            cursor = conn.cursor()
            sql = """
            select * from user_wholesaler
            """
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
            conn.close()
            return data

        elif user == "retailer":
            conn = connection()
            cursor = conn.cursor()
            sql = """
            select * from user_retailer
            """
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
            conn.close()
            return data
