from base import app, render_template
from base.com.dao.dao_main import Dao


@app.route('/wholesaler')
def wholesaler():
    obj_dao = Dao()
    data = obj_dao.show('wholesaler')
    print(data)
    return render_template('content/wholesaler/wholesaler_db.html', data=data)


@app.route('/retailer')
def retailer():
    obj_dao = Dao()
    data = obj_dao.show('retailer')
    print(data)
    return render_template('content/wholesaler/wholesaler_db.html', data=data)
