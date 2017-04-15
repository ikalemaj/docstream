# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            firstname = form.cleaned_data['fname']
            lastname = form.cleaned_data['lname']
            descript = form.cleaned_data['description']
            newdoc = Document(fname = firstname, lname = lastname, description = descript, docfile=request.FILES['docfile'])         
            #need to figure out how to handle data from choice
            #here is where we put this data on some database      
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'myapp/list.html',
        {'documents': documents, 'form': form}
    )
