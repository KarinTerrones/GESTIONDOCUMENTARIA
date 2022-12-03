import io
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from documento.models import *
from documento.forms import *
from django.contrib import messages
from .filters import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allow_users,admin_only
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



@login_required(login_url='login')
def home(request):
	context = {}
	return render(request,'documentos/dashboard.html',context)
@login_required(login_url='login')
def userpage(request):
	context = {}
	return render (request,'documentos/user.html',context)

@login_required(login_url='login')
def Registro_Encargado(request):
	r_form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect ('registrar_perfil')
	context= {'r_form':r_form}
	return render(request,'documentos/registrar.html',context)

def Pagina_Login(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request, email= email, password= password)

		if user is not None:
			login(request, user)
			return redirect ('home')
		else:
			messages.info(request, "Correo o contraseña invalida")
	context={}
	return render (request, 'documentos/login.html', context)


def logoutPage(request):
	logout(request)
	return redirect ('login')

@login_required(login_url='login')
@allow_users(allowed_roles=['a_encargado'])
def Registro_doc(request):
	doc_form = DocumentoForm
	if request.method == 'POST':
		doc_form = DocumentoForm(request.POST)
		if doc_form.is_valid():
			doc_form.save()
			messages.success(request,'El pedido fue grabado exitosamente')
			return redirect ('home')
	context = {'doc_form':doc_form}
	return render(request,'documentos/registro.html',context)

@login_required(login_url='login')
@allow_users(allowed_roles=['a_encargado'])
def Historial_doc(request):
	documentos=Documento.objects.all()
	stat_filtro= Filtro_Status(request.GET,queryset=documentos)
	documentos=stat_filtro.qs
	context = {'documentos':documentos,'filtro':stat_filtro}
	return render (request,'documentos/historial.html',context)

@login_required(login_url='login')
@allow_users(allowed_roles=['a_encargado'])
def Confi_Perfil(request):
	encargado = request.user.encargadoarea
	perfil_form = PerfilEncargado(instance=encargado)
	if request.method == 'POST':
		perfil_form = PerfilEncargado(request.POST, request.FILES, instance=encargado)
		if perfil_form.is_valid():
			perfil_form.save()
	context = {'perfil_form':perfil_form}
	return render (request, 'documentos/perfil.html',context)	

def solicitudes_admin(request):
	solic = Documento.objects.all()
	fech_filtro = Fecha_tipo(request.GET, queryset=solic)
	solic = fech_filtro.qs 
	context = {'solic': solic,'filtro':fech_filtro}
	return render (request, 'documentos/solicitudes.html',context)

def info_encargado_are(request):
	area = Area.objects.all()
	form_regis = RegistrarEncargado()
	if request.method == "POST":
		form_regis = RegistrarEncargado(request.POST)
		if form_regis.is_valid():
			form_regis.save()
			return redirect ('empleados')
	context = {'area':area,'form_reg':form_regis}
	return render ( request, 'documentos/empleados.html',context)

def editar_encargado_area(request,pk):
	area = Area.objects.get(id=pk)
	form_enc = Editar_Encargado(instance=area)
	if request.method == 'POST':
		form_enc = Editar_Encargado(request.POST,instance=area)
		if form_enc.is_valid():
			form_enc.save()
			return redirect('empleados')
	context = {'encargado':area,'form_enc':form_enc}
	return render (request,'documentos/editar_empleado.html',context)

def eliminar_encargado_area(request,pk):
	emple= EncargadoArea.objects.get(id=pk)
	if request.method== "POST":
		emple.delete()
		return redirect ('empleados')
	context = {'emple':emple}
	return render (request,'documentos/eliminar_empleados.html',context)

def registrar_proveedor(request):
	form_reg = RegistarProveedor()
	if request.method == 'POST':
		form_reg = RegistarProveedor(request.POST)
		if form_reg.is_valid():
			form_reg.save()
	context = {'form_r':form_reg}
	return render (request,'documentos/registar_proveedor.html',context)

def view_proveedor(request):
	proveedor = Proveedor.objects.all()
	form_reg = RegistarProveedor()
	if request.method == 'POST':
		form_reg = RegistarProveedor(request.POST)
		if form_reg.is_valid():
			form_reg.save()
			return redirect ('proveedores')
	context = {'prove':proveedor,'form_r':form_reg}
	return render (request,'documentos/proveedores.html',context)

def editar_proveedor(request,pk):
	provee = Proveedor.objects.get(id=pk)
	form_prove = EditarProveedor(instance=provee)
	if request.method == "POST":
		form_prove = EditarProveedor(request.POST,instance=provee)
		if form_prove.is_valid():
			form_prove.save()
			return redirect ("proveedores")
	context = {'form_p':form_prove}
	return render (request,'documentos/editar_proveedor.html',context)

def eliminar_proveedor(request,pk):
	provee = Proveedor.objects.get(id=pk)
	if request.method == "POST":
		provee.delete()
		return redirect ('proveedores')
	context = {'provee':provee}
	return render (request,'documentos/eliminar_proveedor.html',context)

def view_facturas(request):
	fact = Factura.objects.all()
	form_regfac= RegistrarFactura()
	if request.method =='POST':
		form_regfac = RegistrarFactura (request.POST,request.FILES)
		if form_regfac.is_valid():
			form_regfac.save()
			return redirect('facturas')
	context = {'fact':fact,'form':form_regfac}
	return render( request,'documentos/documentos.html',context)

def editar_facturas(request,pk):
	factura = Factura.objects.get(id=pk)
	form_edt = EditarFactura(instance=factura)
	if request.method == 'POST':
		form_edt = EditarFactura(request.POST,request.FILES,instance=factura)
		if form_edt.is_valid():
			form_edt.save()
			return redirect ("facturas")
	context = {'form_et':form_edt}
	return render (request,'documentos/editar_factura.html',context)

def eliminar_factura(request,pk):
	factura = Factura.objects.get(id=pk)
	if request.method == "POST":
		factura.delete()
		return redirect ('facturas')
	context = {'factura':factura}
	return render (request,'documentos/eliminar_factura.html',context)

def registrar_encargado_area(request):
	form_regis = RegistrarEncargado()
	if request.method == "POST":
		form_regis = RegistrarEncargado(request.POST)
		if form_regis.is_valid():
			form_regis.save()
			return redirect ('home')
	context = {'form_reg':form_regis}
	return render (request,'documentos/registrar_encargado.html',context)

def registrar_perfil_encargado(request):
	form_per=RegistrarPerfilEncargado()
	if request.method == "POST":
		form_per = RegistrarPerfilEncargado(request.POST,request.FILES)
		if form_per.is_valid():
			form_per.save()
			return redirect('home')
	context = {'form_pef':form_per}
	return render (request,'documentos/registrar_perfil_encargado.html',context)

def editar_solicitud(request,pk):
	doc = Documento.objects.get(id=pk)
	form_doc = EditarSolicitud(instance=doc)
	if request.method == 'POST':
		form_doc = EditarSolicitud(request.POST,instance=doc)
		if form_doc.is_valid():
			form_doc.save()
			return redirect('solicitudes') 

	context = {'form_s':form_doc}
	return render (request,'documentos/editar_solic.html',context)

def generar_pdf_total(request):
	buf = io.BytesIO()
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont('Helvetica',14)

	documentos = Documento.objects.all()

	lines = []

	for documento in documentos :
		lines.append(documento.nombre)
		lines.append(documento.tipo)
		lines.append(documento.estado)
		lines.append(documento.proveedor.razon_social)
		lines.append(documento.pedido)
		lines.append("")
		
	for line in lines:
		textob.textLine(line)
	
	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)
	return FileResponse (buf, as_attachment=True,filename="Historial.pdf")

def generar_pdf(request,pk):
		buf = io.BytesIO()
		c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
		textob = c.beginText()
		textob.setTextOrigin(inch, inch)
		textob.setFont('Helvetica',14)

		documentos = Documento.objects.get(id=pk)
		lines = []
		

		lines.append(documentos.nombre)
		lines.append(documentos.tipo)
		lines.append(documentos.estado)
		lines.append(documentos.proveedor.razon_social)
		lines.append(documentos.pedido)
		lines.append("")

		for line in lines:
			textob.textLine(line)

		c.drawText(textob)
		c.showPage()
		c.save()
		buf.seek(0)
		return FileResponse(buf, as_attachment=True,filename="Pedido.pdf")