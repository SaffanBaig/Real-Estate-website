from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #Already Inquiries
        if request.user.is_authenticated:
            user_id = request.user.id
            has_connected = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_connected:
                messages.error(request, 'You have already made an inquiry for this property')
                return redirect('/listings/'+listing_id)
           
        contact = Contact(listing=listing, listing_id=listing_id, name=name,
        email=email, phone=phone, message=message, user_id=user_id)
            

        contact.save() 
        # #Send_mail

        # send_mail(
        #     'Property Inquiry',
        #     'mirzasaffan492@gmail.com',
        #     'There has been an inquiry for '+listing+ '. Sign into the admin panel for more info',
        #     [realtor_email, 'mirzasaffan492@gmail.com'],
        #     fail_silently=True
        # )
            
        messages.success(request,'Your request has been submitted')
        return redirect('/listings/'+listing_id)
