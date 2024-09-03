import base64
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            feedback = form.save(commit=False)
            if request.POST.get('voice_recording'):
                format, audio_str = request.POST['voice_recording'].split(';base64,')
                ext = format.split('/')[-1]
                feedback.voice_recording.save(f'voice_recording.{ext}', ContentFile(base64.b64decode(audio_str)), save=True)
            feedback.save()
            return redirect('success_page')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form/submit_feedback.html', {'form': form})

def success_page(request):
    return render(request, 'feedback_form/success_page.html')
