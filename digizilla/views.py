from django.shortcuts import render, redirect
from .models import Digizilla
from .forms import DigizillaForm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def digizilla_list(request):
    digizillas = Digizilla.objects.all()
    return render(request, 'digizilla_list.html', {'digizillas': digizillas})


def digizilla_detail(request, pk):
    digizilla = Digizilla.objects.get(pk=pk)
    return render(request, 'digizilla_detail.html', {'digizilla': digizilla})


def digizilla_form(request):
    form = DigizillaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/digizilla')
    return render(request, 'digizilla_form.html', {'form': form})


def generate_pdf_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    p = canvas.Canvas(response, pagesize=letter)
    digizillas = Digizilla.objects.all()
    y = 750
    for digizilla in digizillas:
        p.drawString(100, y, f"Name: {digizilla.name}")
        p.drawString(100, y - 20, f"Gender: {digizilla.gender}")
        p.drawString(100, y - 40, f"Country: {digizilla.country}")
        p.drawString(100, y - 60, f"Joining Date: {digizilla.joining_date}")
        p.drawString(100, y - 80, f"Tags: {digizilla.tags}")
        customers = ", ".join([customer.full_name()
                              for customer in digizilla.customers.all()])
        p.drawString(100, y - 100, f"Customers: {customers}")
        company_name = digizilla.company.name if digizilla.company else ""
        p.drawString(100, y - 120, f"Company: {company_name}")
        p.drawString(100, y - 140, f"Notes: {digizilla.notes}")
        p.drawString(100, y - 160, f"Comments: {digizilla.comments}")
        y -= 200
    p.showPage()
    p.save()

    return response
