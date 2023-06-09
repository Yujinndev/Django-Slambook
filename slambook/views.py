# from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
# from slambook.forms import RegistrationForm
from slambook.forms import PersonForm
from slambook.models import Person

# RECORDS
def persons(request):
  if request.method == "POST":
    form = PersonForm(request.POST)
    if form.is_valid():
      try:
        form.save()
        return redirect('/')
      except:
        pass
  else:
    form = PersonForm()
  return render(request, 'index.html', {'form': form})
    
def show(request):
  persons = Person.objects.all()
  return render(request, "show.html", {'persons': persons})

def edit(request, id):
  person = Person.objects.get(id = id)
  return render(request, 'edit.html', {'person': person})

def update(request, id):
  person = Person.objects.get(id = id)
  form = PersonForm(request.POST, instance = person)
  if form.is_valid():
    form.save()
    return redirect("/")
  return render(request, 'edit.html', {'person': person})

def destroy(request, id):
  person = Person.objects.get(id = id)
  person.delete()
  return redirect("/")