from django.shortcuts import render,redirect
from .forms import MaterialCreationForm,CatagoryCreationForm
from .models import Material,Category
# Create your views here.

def list_material(request):
    materials=Material.objects.all()
    context={
        "materials":materials
    }
    return render(request,"material/listm.html",context)

def list_category(request):
    categorys=Category.objects.all()
    context={
        "categorys":categorys
    }
    return render(request,"material/listc.html",context)

def create_material(request):
    if(request.method=="POST"):
        form= MaterialCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("material:listmaterial")
    else:
        form = MaterialCreationForm()
    context={
        "form":form
    }
    return render(request,"material/create.html",context)

def create_category(request):
    if(request.method=="POST"):
        form= CatagoryCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("material:listcategory")
    else:
        form = CatagoryCreationForm()
    context={
        "form":form
    }
    return render(request,"material/create.html",context)

def update_category(request,pk):
    category = Category.objects.get(pk=pk)
    if(request.method=="POST"):
        form= CatagoryCreationForm(request.POST,instance=category)    
        if form.is_valid():
            form.save()
            return redirect("material:listcategory")
    else:
        form= CatagoryCreationForm(instance=category)
    context={
        "form":form
    }
    return render(request,"material/create.html",context)
    

def update_material(request,pk):
    material = Material.objects.get(pk=pk)
    if(request.method=="POST"):
        form= MaterialCreationForm(request.POST,instance=material)    
        if form.is_valid():
            form.save()
            return redirect("material:listmaterial")
    else:
        form= MaterialCreationForm(instance=material)

    context={
        "form":form
    }
    return render(request,"material/create.html",context)
def delete_category(request,pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect("material:listcategory")

def delete_material(request,pk):
    material = Material.objects.get(pk=pk)
    material.delete()
    return redirect("material:listmaterial")
