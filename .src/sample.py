from datetime import datetime

# Date difference sample
fecha_instalacion = '1972-09-14'
fecha_suspension = '2019-07-02'
diff_date = datetime.strptime(fecha_suspension, '%Y-%m-%d') - datetime.strptime(fecha_instalacion, '%Y-%m-%d')

print(diff_date.days/365)