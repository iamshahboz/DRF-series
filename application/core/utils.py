from openpyxl import Workbook 
from django.http import HttpResponse 
from .models import Product 


def generate_excel(products):
    wb = Workbook()
    ws = wb.active
    ws.title = "Products"

    headers = ['ID','Name','Description','Price','Stock']
    ws.append(headers)

    for product in products:
        ws.append([product.id, product.name, product.description, product.price, product.stock])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=customers.xlsx'
    wb.save(response)

    return response 