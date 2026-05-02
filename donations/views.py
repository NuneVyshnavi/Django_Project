from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from rest_framework import viewsets
from django.core.mail import send_mail

from .models import Donation
from .serializers import DonationSerializer
from .forms import DonationForm

from requests_app.models import FoodRequest
from requests_app.forms import FoodRequestForm


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


@login_required
def home(request):

    search = request.GET.get('search')
    category = request.GET.get('category')

    donations = Donation.objects.all()

    # SEARCH
    if search:

        donations = donations.filter(
            food_name__icontains=search
        )

    # CATEGORY FILTER
    if category:

        donations = donations.filter(
            category__icontains=category
        )

    # PAGINATION
    paginator = Paginator(donations, 4)

    page_number = request.GET.get('page')

    donations = paginator.get_page(page_number)

    # TOTAL DONATIONS
    total_donations = Donation.objects.count()

    donation_form = DonationForm()

    request_form = FoodRequestForm()

    if request.method == 'POST':

        # ADD DONATION
        if 'donate_food' in request.POST:

            donation_form = DonationForm(
                request.POST,
                request.FILES
            )

            if donation_form.is_valid():

                donation_form.save()

                return redirect('/')

        # REQUEST FOOD
        elif 'request_food' in request.POST:

            donation_id = request.POST.get('donation_id')

            donation = Donation.objects.get(id=donation_id)

            request_form = FoodRequestForm(request.POST)

            if request_form.is_valid():

                food_request = request_form.save(commit=False)

                food_request.donation = donation

                food_request.save()

                # EMAIL
                send_mail(
                    'Food Request Received',
                    'Your NGO request was submitted successfully.',
                    'vyshunune@gmail.com',
                    ['vyshunune21@gmail.com'],
                    fail_silently=False,
                )

                return redirect('/')

    return render(request, 'home.html', {
        'donations': donations,
        'donation_form': donation_form,
        'request_form': request_form,
        'total_donations': total_donations
    })


def manage_requests(req):

    requests = FoodRequest.objects.all()

    return render(req, 'manage_requests.html', {
        'requests': requests
    })


def accept_request(request, id):

    food_request = FoodRequest.objects.get(id=id)

    food_request.status = 'Accepted'

    food_request.save()

    return redirect('/manage-requests/')


def reject_request(request, id):

    food_request = FoodRequest.objects.get(id=id)

    food_request.status = 'Rejected'

    food_request.save()

    return redirect('/manage-requests/')