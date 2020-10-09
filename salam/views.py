from django.shortcuts import render,redirect
from salam import models
from salam import forms
# Create your views here.
def Index(request):
    information=models.info.objects.all()# من هنا نحدد جميع البيانات لعرضها
    context={'information':information}
    return render(request,'index.html',context)


def inserting(request):
    form_data=forms.inforeg(request.POST or None)
    if form_data.is_valid():
        regform=models.info()
        regform.full_name=form_data.cleaned_data['Full_name']
        regform.the_age=form_data.cleaned_data['The_age']
        regform.phone_number=form_data.cleaned_data['Phone_num']
        regform.save()

    context={
        'formregister':form_data
        }
    return render(request,'regform.html',context)

def Delete(request, item_id):
    dels =models.info.objects.get(pk=item_id)
    if request.method=='POST':
        dels.delete()
        return redirect("/index/")
    return render(request,'Delete.html')
        
        
    