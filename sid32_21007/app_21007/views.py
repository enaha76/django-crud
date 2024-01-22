# app_21007/views.py
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import ProductFamily, Product, SellingPoint, Price, Basket, ProductBasket
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from tablib import Dataset
from .resources import ProductResource
from django.http import HttpResponse
import csv
import io
from django.shortcuts import render, redirect



def home(request):
    mymsg = request.GET.get('message')
    return render(request, 'home.html', {'user_message': mymsg})

class ProductFamilyList(ListView):
    model = ProductFamily

class ProductFamilyDetail(DetailView):
    model = ProductFamily  

class ProductFamilyCreate(CreateView):
    model = ProductFamily
    fields = '__all__'
    success_url = reverse_lazy('productfamily_list')

class ProductFamilyDelete(DeleteView):
    model = ProductFamily
    success_url = reverse_lazy('productfamily_list')

class ProductFamilyUpdate(UpdateView):
    model = ProductFamily
    fields = '__all__'
    success_url = reverse_lazy('productfamily_list')

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class SellingPointList(ListView):
    model = SellingPoint

class SellingPointDetail(DetailView):
    model = SellingPoint

class SellingPointCreate(CreateView):
    model = SellingPoint
    fields = '__all__'
    success_url = reverse_lazy('sellingpoint_list')

class SellingPointDelete(DeleteView):
    model = SellingPoint
    success_url = reverse_lazy('sellingpoint_list')

class SellingPointUpdate(UpdateView):
    model = SellingPoint
    fields = '__all__'
    success_url = reverse_lazy('sellingpoint_list')


class PriceList(ListView):
    model = Price

class PriceDetail(DetailView):
    model = Price

class PriceCreate(CreateView):
    model = Price
    fields = '__all__'
    success_url = reverse_lazy('price_list')

class PriceDelete(DeleteView):
    model = Price
    success_url = reverse_lazy('price_list')

class PriceUpdate(UpdateView):
    model = Price
    fields = '__all__'
    success_url = reverse_lazy('price_list')

class BasketList(ListView):
    model = Basket

class BasketDetail(DetailView):
    model = Basket

class BasketCreate(CreateView):
    model = Basket
    fields = '__all__'
    success_url = reverse_lazy('basket_list')

class BasketDelete(DeleteView):
    model = Basket
    success_url = reverse_lazy('basket_list')

class BasketUpdate(UpdateView):
    model = Basket
    fields = '__all__'
    success_url = reverse_lazy('basket_list')

class ProductBasketList(ListView):
    model = ProductBasket

class ProductBasketDetail(DetailView):
    model = ProductBasket

class ProductBasketCreate(CreateView):
    model = ProductBasket
    fields = '__all__'
    success_url = reverse_lazy('productbasket_list')

class ProductBasketDelete(DeleteView):
    model = ProductBasket
    success_url = reverse_lazy('productbasket_list')

class ProductBasketUpdate(UpdateView):
    model = ProductBasket
    fields = '__all__'
    success_url = reverse_lazy('productbasket_list')

#IMPORT BUTTON 

# app_21007/views.py

def product_export(request):
    product_resource = ProductResource()
    dataset = product_resource.export()
    with open('products.csv', 'w') as f:
        f.write(dataset.csv)
    return HttpResponse("Data has been successfully exported to the 'products.csv' file in the project's root directory.")



# views.py
# ... your other imports ...

def import_product(request):
    if request.method == "POST":
        csv_file = request.FILES.get("csv_file")
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect("product_import")

        # reading csv file
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)  # skip the header

        for column in csv.reader(io_string, quotechar="|"):
            try:
                label = column[1]
                price_unit = column[2]
                code = column[3]
                productfamily_label = column[0]  # Assuming the product family label is in the 4th column

                # Get or create ProductFamily based on the label
                product_family, _ = ProductFamily.objects.get_or_create(label=productfamily_label)

                # Create Product with the foreign key reference to the ProductFamily
                product = Product.objects.create(
                    label=label,
                    price_unit=price_unit,
                    code=code,
                    productfamily=product_family,
                )
            except IndexError:
                messages.error(request, 'Invalid CSV format')
                return redirect("product_import")

        return redirect("product_list")

    return render(request, "product_list.html")


## product family 
# views.py

def import_productfamily(request):
    if request.method == "POST":
        csv_file = request.FILES.get("csv_file")
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect("productfamily_import")

        # reading csv file
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)  # skip the header

        for column in csv.reader(io_string, quotechar="|"):
            try:
                label = column[0]

                # Create ProductFamily
                product_family, _ = ProductFamily.objects.get_or_create(label=label)
            except IndexError:
                messages.error(request, 'Invalid CSV format')
                return redirect("productfamily_import")

        return redirect("productfamily_list")

    return render(request, "productfamily_list.html")

# sellingpoint 

def import_sellingpoint(request):
    if request.method == "POST":
        csv_file = request.FILES.get("csv_file")
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect("sellingpoint_import")

        # reading csv file
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)  # skip the header

        for column in csv.reader(io_string, quotechar="|"):
            try:
                code = column[0]
                wilaya = column[1]
                moughataa = column[2]
                commune = column[3]
                gps_lat = float(column[4])
                gps_long = float(column[5])

                # Create SellingPoint instance
                selling_point = SellingPoint.objects.create(
                    code=code,
                    wilaya=wilaya,
                    moughataa=moughataa,
                    commune=commune,
                    gps_lat=gps_lat,
                    gps_long=gps_long,
                )
            except (IndexError, ValueError):
                messages.error(request, 'Invalid CSV format')
                return redirect("sellingpoint_import")

        return redirect("sellingpoint_list")

    return render(request, "sellingpoint_list.html")


# price 

# views.py
from .models import Price, SellingPoint, Product
import pandas as pd
# views.py
from django.shortcuts import get_object_or_404

def import_price(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']

        # Assuming you have a DataFrame df with the necessary columns (value, date, sellingpoint, product)
        df = pd.read_csv(csv_file)

        for index, row in df.iterrows():
            value = row['value']
            date = row['date']
            sellingpoint_code = row['sellingpoint']
            product_label = row['product']  # Assuming 'product' column contains the product label

            # Get SellingPoint or create a new one if it doesn't exist
            sellingpoint = get_object_or_404(SellingPoint, code=sellingpoint_code)

            try:
                # Try to get the Product
                product = Product.objects.get(label=product_label)
            except Product.DoesNotExist:
                messages.error(request, f"Product with label {product_label} does not exist. Please create it first.")
                return redirect('price_list')

            # Create Price
            price = Price.objects.create(
                value=value,
                date=date,
                sellingpoint=sellingpoint,
                product=product
            )

        messages.success(request, 'Prices imported successfully.')
        return redirect('price_list')

    return render(request, 'price_import.html')



# views.py
from .models import Basket
# ... other imports ...

def import_basket(request):
    if request.method == "POST":
        csv_file = request.FILES.get("csv_file")
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect("basket_import")

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)  # skip the header

        for column in csv.reader(io_string, quotechar="|"):
            try:
                label = column[0]
                code = column[1]
                description = column[2]

                # Create Basket
                basket = Basket.objects.create(
                    label=label,
                    code=code,
                    description=description,
                )
            except IndexError:
                messages.error(request, 'Invalid CSV format')
                return redirect("basket_import")

        return redirect("basket_list")

    return render(request, "basket_import.html")


# views.py
from .models import ProductBasket, Price, Basket
# ... other imports ...

def import_productbasket(request):
    if request.method == "POST":
        csv_file = request.FILES.get("csv_file")
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect("productbasket_import")

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)  # skip the header

        for column in csv.reader(io_string, quotechar="|"):
            try:
                price_value = column[0]
                basket_label = column[1]  # Assuming basket label is in the 2nd column
                ponderation = column[2]

                # Get or create Basket based on the label
                basket, _ = Basket.objects.get_or_create(label=basket_label)

                # Get or create Price based on the value (assuming unique)
                price, _ = Price.objects.get_or_create(value=price_value)

                # Create ProductBasket with foreign key references
                productbasket = ProductBasket.objects.create(
                    price=price,
                    basket=basket,
                    ponderation=ponderation,
                )
            except IndexError:
                messages.error(request, 'Invalid CSV format')
                return redirect("productbasket_import")

        return redirect("productbasket_list")

    return render(request, "productbasket_import.html")

# CHARTJS

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse

# class LineChartJSONView(BaseLineChartView):
#     def get_labels(self):
#         # Return labels for the x-axis (e.g., dates)
#         return [your_dates_here]

#     def get_providers(self):
#         # Return names of datasets
#         return [your_selling_points_here]

#     def get_data(self):
#         # Return datasets to plot (e.g., prices)
#         return [your_data_here]

def line_chart(request):
    return render(request, 'line_chart.html')



from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse
from app_21007.models import Price, Product
class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        # Return labels for the x-axis (e.g., dates)
        # Fetch distinct dates from the Price table
        return Price.objects.values_list('date', flat=True).distinct()

    def get_providers(self):
        # Return names of datasets (products)
        # Fetch distinct products from the Product table
        return Price.objects.values_list('product__label', flat=True).distinct()

    def get_data(self):
        # Return datasets to plot (e.g., prices for each product)
        # Fetch data from the Price table based on dates and products
        labels = self.get_labels()
        products = self.get_providers()

        data = []
        for product in products:
            prices = Price.objects.filter(product__label=product).order_by('date')
            price_values = [price.value for price in prices]
            data.append(price_values)

        return data

line_chart_json = LineChartJSONView.as_view()
