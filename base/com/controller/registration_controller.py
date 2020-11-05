from base import app, request, render_template
from base.com.dao.dao_main import Dao
from base.com.vo.vo_main import wholesalerVo, retailerVo


@app.route('/register', methods=['POST'])
def register():
    obj_dao = Dao()
    obj_vo_wholesaler = wholesalerVo()
    obj_vo_retailer = retailerVo()
    if request.form.get('user') == "wholesaler":
        obj_vo_wholesaler.user_full_name = request.form.get('full_name')
        obj_vo_wholesaler.user_email = request.form.get('user_email')
        obj_vo_wholesaler.user_password = request.form.get('user_password')
        obj_vo_wholesaler.user_contact = request.form.get('user_contact')
        obj_vo_wholesaler.user_company_name = request.form.get('org_name')
        obj_vo_wholesaler.user_org_email = request.form.get('org_email')
        obj_vo_wholesaler.user_org_contact = request.form.get('org_contact')
        obj_vo_wholesaler.user_org_address = request.form.get('org_address')
        obj_vo_wholesaler.user_firm_type = request.form.get('org_firm_type')
        result = obj_dao.register(obj_vo_wholesaler, "wholesaler")
        if result == 1:
            return render_template('home/index.html')
        else:
            print("Error...!!!")
            return "Check console....!error dected...!"

    elif request.form.get('user') == "retailer":
        obj_vo_retailer.user_full_name = request.form.get('full_name')
        obj_vo_retailer.user_email = request.form.get('user_email')
        obj_vo_retailer.user_password = request.form.get('user_password')
        obj_vo_retailer.user_contact = request.form.get('user_contact')
        obj_vo_retailer.user_company_name = request.form.get('org_name')
        obj_vo_retailer.user_org_email = request.form.get('org_email')
        obj_vo_retailer.user_org_contact = request.form.get('org_contact')
        obj_vo_retailer.user_org_address = request.form.get('org_address')
        obj_vo_retailer.user_firm_type = request.form.get('org_firm_type')

        result = obj_dao.register(obj_vo_retailer, "retailer")
        if result == 1:
            return render_template('home/index.html')
        else:
            print("Error...!!!")
            return "Check console....!error dected...!"
