from django.shortcuts import render, redirect
from .models import SongRequest

# View for rendering the request form
def request_form(request):
    if request.method == 'POST':
        artist_name = request.POST.get('artist_name')
        song_name = request.POST.get('song_name')
        user_name = request.POST.get('user_name')
        user_message = request.POST.get('user_message')

        # Save the request
        SongRequest.objects.create(
            artist_name=artist_name,
            song_name=song_name,
            user_name=user_name,
            user_message=user_message,
        )
        return redirect('request_list')  # Redirect to the list after submission

    return render(request, 'request_form.html')

# View for rendering the list of requests
def request_list(request):
    requests = SongRequest.objects.all()
    return render(request, 'request_list.html', {'requests': requests})

# View for deleting all requests
def delete_all_requests(request):
    if request.method == 'POST':
        SongRequest.objects.all().delete()
        return redirect('request_list')
