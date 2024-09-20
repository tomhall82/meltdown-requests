from django.shortcuts import render, redirect, get_object_or_404
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

    return render(request, 'request_form.html')

# View for rendering the list of requests
def request_list(request):
    requests = SongRequest.objects.all()
    return render(request, 'request_list.html', {'requests': requests})

def delete_request(request, request_id):
    # Get the specific request by its ID and delete it
    req = get_object_or_404(SongRequest, id=request_id)
    req.delete()
    return redirect('request_list')  # Redirect back to the request list after deletion

# View for deleting all requests
def delete_all_requests(request):
    if request.method == 'POST':
        SongRequest.objects.all().delete()
        return redirect('request_list')
