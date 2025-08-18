from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import AddForm
from .models import Contact
from django.http import HttpResponseRedirect

def detail(request, name1):
    try:
        contato_localizado = Contact.objects.filter(name=name1).first()
    except:
        return render(request, 'mycontacts/detail.html', {'contact': "Erro"})
    return render(request, 'mycontacts/detail.html', {'contact': contato_localizado})

def show(request):
    """ 
    This function gets all the members in your Database through your Model
    Any further usage please refer to: https://docs.djangoproject.com/el/1.10/ref/models/querysets/
    """
    contact_list = Contact.objects.all()
    return render(request, 'mycontacts/show.html',{'contacts': contact_list})
    
def add(request):
    """ This function is called to add one contact member to your contact list in your Database """
    if request.method == 'POST':
        
        django_form = AddForm(request.POST)
        if django_form.is_valid():
           
            """ Assign data in Django Form to local variables """
            new_member_name = django_form.data.get("name")
            new_member_relation = django_form.data.get("relation")
            new_member_phone = django_form.data.get('phone')
            new_member_email = django_form.data.get('email')
            
            """ This is how your model connects to database and create a new member """
            Contact.objects.create(
                name =  new_member_name, 
                relation = new_member_relation,
                phone = new_member_phone,
                email = new_member_email, 
                )
                 
            contact_list = Contact.objects.all()
            return render(request, 'mycontacts/show.html',{'contacts': contact_list})    
        
        else:
            """ redirect to the same page if django_form goes wrong """
            return render(request, 'mycontacts/add.html')
    else:
        return render(request, 'mycontacts/add.html')

def edit(request, name1):
    if request.method == 'POST':
            
        django_form = AddForm(request.POST)
        if django_form.is_valid():
        
            """ Assign data in Django Form to local variables """
            new_member_name = django_form.data.get("name")
            new_member_relation = django_form.data.get("relation")
            new_member_phone = django_form.data.get('phone')
            new_member_email = django_form.data.get('email')
            
            """ This is how your model connects to database and create a new member """
            Contact.objects.filter(name=name1).update(
                name =  new_member_name, 
                relation = new_member_relation,
                phone = new_member_phone,
                email = new_member_email, 
                )
                
            contact_list = Contact.objects.all()
            return render(request, 'mycontacts/show.html',{'contacts': contact_list})    
        
        else:
            """ redirect to the same page if django_form goes wrong """
            return render(request, 'mycontacts/add.html')
    else:
        try:
            contato_localizado = Contact.objects.filter(name=name1).first()
        except:
            return render(request, 'mycontacts/edit.html', {'contact': "Erro"})
        return render(request, 'mycontacts/edit.html', {'contact': contato_localizado})

def delete(request, name1):
    Contact.objects.filter(name=name1).first().delete()
    return render(request, 'mycontacts/show.html')

