from django.shortcuts import render
from .models import Material, Vendor, Mill
from django.views import generic


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_materials = Material.objects.count()
    num_vendors = Vendor.objects.count()
    num_mills = Mill.objects.count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_materials': num_materials,
                 'num_vendors': num_vendors, 'num_mills': num_mills},
    )


class MaterialListView(generic.ListView):
    model = Material


class MaterialDetailView(generic.DetailView):
    model = Material


class MillListView(generic.ListView):
    model = Mill


class MillDetailView(generic.DetailView):
    model = Mill


class VendorListView(generic.ListView):
    model = Vendor


class VendorDetailView(generic.DetailView):
    model = Vendor
