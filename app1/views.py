from django.shortcuts import render,redirect
from .forms import TextForm, FileForm
from .models import UserText, UserFile
from django.contrib import messages
import docx2txt, pdfminer.high_level
from io import BytesIO

def home_view(request):
    return render(request, 'home.html', {})

def user_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            message = form.cleaned_data['message']
            input_data = UserText(username=username, message=message)
            input_data.save()
            
            return redirect('processing', username=username)
    else:
        form = TextForm()
    return render(request, 'texttemplate.html', {'form':form})

def form_data(request, username):
    data_form_user = UserText.objects.filter(username=username).latest('id')
    message = data_form_user.message
    word_count = len(message.split())
    
    return render(request, 'counted_words.html', {'words':word_count})


def upload_file(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            
            return redirect('fileprocessing', username=username)
    else:
        form = FileForm()
    return render(request, 'files.html', {'form':form})

def file_data(request, username):
    
    data_from_user = UserFile.objects.filter(username=username).latest('id')
    file = data_from_user.file
    
    word_count = 0
    
    if file.name.endswith('.docx'):
        content = docx2txt.process(file)
        word_count = len(content.split())
        
    elif file.name.endswith('.pdf'):
        with BytesIO(file.read()) as pdf_file:#using ByteIO to process file in the file format
            content = pdfminer.high_level.extract_text(pdf_file)
            word_count = len(content.split())
            
    else:
       message = file.read().decode('utf-8')
       word_count = len(message.split())
    
    return render(request, 'counted_words.html', {'words':word_count})