from flask_admin.contrib.sqla import  ModelView
from my_app.models import Category, Product
from flask_admin import BaseView, expose, AdminIndexView
from flask_login import logout_user, current_user
from flask import redirect
from my_app import db, app, utils
from flask_admin import Admin
from flask import request

class MyAdminIndex(AdminIndexView):
    @expose("/")
    def index(self):
        stats = utils.product_stats_by_cate()
        return self.render('admin/index.html', stats=stats)


admin = Admin(app=app,
              name="UTE SHOP",
              template_mode="bootstrap4",
              index_view=MyAdminIndex())


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class CategoryModelView(AuthenticatedView):
    can_export = True

class ProductModelView(AuthenticatedView):
    can_export = True

class StatsView(BaseView):
    @expose("/")
    def index(self):
        from_date = request.args.get('from_date')
        to_date = request.args.get('to_date')
        stats = utils.product_stats(from_date=from_date, to_date=to_date)
        return self.render("admin/stats.html", stats=stats)
    def is_accessible(self):
        return current_user.is_authenticated
class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect("/admin")
    def is_accessible(self):
        return current_user.is_authenticated
admin.add_view(CategoryModelView(Category, db.session, name="Danh mục"))
admin.add_view(ProductModelView(Product, db.session, name="Sản phẩm"))
admin.add_view(StatsView(name="Thống kê"))
admin.add_view(LogoutView(name="Đăng xuất"))
