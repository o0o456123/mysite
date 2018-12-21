import xadmin
from xadmin import views
from .models import Card
from django.contrib.auth.models import Group, Permission, User
from xadmin.models import Log


# 创建xadmin的全局管理器并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# xadmin 全局配置参数信息设置
class GlobalSetting(object):
    site_title = '门卡后台管理'
    site_footer = '底限'
    # 收起菜单
    # menu_style = 'accordion'

    def get_site_menu(self):
        return (
            {'title': '用户管理', 'menus': (
                {'title': '门卡信息', 'url': self.get_model_url(Card, 'changelist')},
            )},
            {'title': '系统管理', 'menus': (
                {'title': '管理员信息', 'url': self.get_model_url(User, 'changelist')},
                {'title': '管理员分组', 'url': self.get_model_url(Group, 'changelist')},
                {'title': '管理员权限', 'url': self.get_model_url(Permission, 'changelist')},
                {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
            )},)


class CardAdmin:
    list_display = ['card_id', 'state', 'create_time']
    search_fields = ['card_id']
    list_filter = ['card_id', 'state', 'create_time']
    model_icon = 'fa fa-address-card-o'



# 注册后台
xadmin.site.register(Card, CardAdmin)


# 注册全局配置
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)