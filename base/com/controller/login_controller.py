from base import app, render_template, request,flash,redirect,url_for
from base.com.dao.dao_main import Dao
from base.com.vo.vo_main import loginVo


@app.route('/verified', methods=["POST"])
def verified():
    obj_dao = Dao()
    obj_vo = loginVo()

    obj_vo.user_email = request.form.get('user_email')
    obj_vo.user_password = request.form.get('user_password')

    result, data, identify = obj_dao.login(obj_vo)

    if "admin_name" in data:
        if result == 1 and identify == "admin":
            return render_template('content/admin/adminHome.html', data=data['admin_name'])
    else:
        if result == 1 and identify == "wholesaler":
            main = data['user_full_name']
            return render_template('content/wholesaler/wholesalerHome.html', data=main)
        elif result == 1 and identify == "retailer":
            main = data['user_full_name']
            return render_template('content/retailer/retailerHome.html', data=main)
        elif result == 0 and data == "none" and identify == "invalid":
            flash("Invalid crendtial kindly check email or password...")
            return redirect(url_for('reroute'))
