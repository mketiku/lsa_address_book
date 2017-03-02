from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import  AddressEntry


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


# Create your views here.
# @login_required(login_url="login/")
# class IndexView(LoginRequiredMixin, generic.ListView):
# class IndexView(ListView):
#     template_name = 'address_book/index.html'
#     context_object_name = 'addressbook_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return AddressEntry.objects.all()

class AddressForm(ModelForm):
    class Meta:
        model = AddressEntry
        fields =  ['first_name', 'last_name', 'email_address', 'street_address']

def address_list(request, template_name='address_book/addressentry_list.html'):
    address_entries = AddressEntry.objects.all()
    data = {}
    data['object_list'] = address_entries
    return render(request, template_name, data)

def address_create(request, template_name='address_book/addressentry_form.html'):
    form = AddressForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('address_list')
    return render(request, template_name, {'form':form})

def address_update(request, pk, template_name='address_book/addressentry_form.html'):
    server = get_object_or_404(AddressEntry, pk=pk)
    form = AddressForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('address_list')
    return render(request, template_name, {'form':form})

def address_delete(request, pk, template_name='address_book/addressentry_confirm_delete.html'):
    server = get_object_or_404(AddressEntry, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('address_list')
    return render(request, template_name, {'object':server})