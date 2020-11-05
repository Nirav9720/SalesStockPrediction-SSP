from wtforms import StringField, IntegerField


class adminVo:
    admin_name = StringField
    admin_contact = IntegerField
    admin_email = StringField
    admin_password = StringField


class wholesalerVo:
    user_full_name=StringField
    user_email = StringField
    user_password = StringField
    user_contact = IntegerField
    user_company_name = StringField
    user_org_email = StringField
    user_org_contact = StringField
    user_org_address = StringField
    user_firm_type = StringField


class retailerVo:
    user_full_name = StringField
    user_email = StringField
    user_password = StringField
    user_contact = IntegerField
    user_company_name = StringField
    user_org_email = StringField
    user_org_contact = StringField
    user_org_address = StringField
    user_firm_type = StringField

class loginVo:
    user_email = StringField
    user_password = StringField
