from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('registrar/',views.Registro_Encargado,name="registrar"),
   path('', views.home,name="home"),
   path('registro/',views.Registro_doc,name="registro"),
   path('historial/',views.Historial_doc,name="historial"),
   path('perfil/',views.Confi_Perfil,name="perfil"),
   path('usuario/',views.userpage, name='user-page'),
   path('login/',views.Pagina_Login, name="login"),
   path('registrar/',views.Registro_Encargado,name="registrar"),
   path('logout',views.logoutPage,name='logout'),
   path('solicitudes/',views.solicitudes_admin,name='solicitudes'),
   path('empleados/',views.info_encargado_are,name="empleados"),
   path('editar_empleado/<str:pk>/',views.editar_encargado_area,name="editar_empleado"),
   path('eliminar_empleado/<str:pk>/',views.eliminar_encargado_area,name="eliminar_empleado"),
   path('generar_pedido/<str:pk>',views.generar_pdf,name="generar_pedido"),
   path('generar_historial',views.generar_pdf_total, name="generar_historial"),
   path('proveedores/',views.view_proveedor,name="proveedores"),
   path('editar_proveedor/<str:pk>/',views.editar_proveedor,name="editar_proveedor"),
   path('eliminar_proveedor/<str:pk>/',views.eliminar_proveedor,name='eliminar_proveedor'),
   path('facturas/',views.view_facturas,name="facturas"),
   path('editar_factura/<str:pk>/',views.editar_facturas,name="editar_factura"),
   path('eliminar_factura/<str:pk>/',views.eliminar_factura,name="eliminar_factura"),
   path('registrar_area',views.registrar_encargado_area,name="registrar_area"),
   path('registrar_perfil',views.registrar_perfil_encargado,name="registrar_perfil"),
   path('editar_solicitud/<str:pk>/',views.editar_solicitud,name="editar_solicitud"),
   #url Reset Password
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="documentos/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="documentos/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="documentos/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="documentos/password_reset_done.html"), 
        name="password_reset_complete"),
]