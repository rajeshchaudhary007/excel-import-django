from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from .models import Company
import openpyxl

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'companies/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context
    

    
def import_excel(request):
    if request.method == "POST":
        excel_file = request.FILES['ufile']

        if excel_file.name.endswith('.xlsx'):
            wb = openpyxl.load_workbook(excel_file)
            worksheet = wb.active 

            for row in worksheet.iter_rows(min_row=2, values_only=True):
                rank, name, industry, revenue, revenue_growth,employees, headquarters = row
                
                if not Company.objects.filter(rank=rank,name=name, industry=industry, revenue=revenue, revenue_growth=revenue_growth,employees=employees, headquarters=headquarters).exists():
                   company = Company(
                       rank=rank,
                       name=name, 
                       industry=industry, 
                       revenue=revenue, 
                       revenue_growth=revenue_growth,
                       employees=employees,
                       headquarters=headquarters
                   )
                  
                   company.save()
            return redirect('/')  

    return render(request, 'companies/excel_import.html')
  
