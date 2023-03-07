from django.http import HttpResponse
from django.shortcuts import render
import string

def analyze(request):
    return render(request,"analyze.html")

def output(request):
    text = request.POST.get('text')
    if not text:
        return HttpResponse("Please enter some text and try again")
     
    # Check radio button values
    operation = request.POST.get('gridRadios')

    # Calculate number of spaces, alphabets, numbers, and punctuations in the input text
    spaces = 0
    alphabets = 0
    numbers = 0
    punctuations = 0
    
    for char in text:
        if char.isspace():
            spaces += 1
        elif char.isalpha():
            alphabets += 1
        elif char.isdigit():
            numbers += 1
        else:
            punctuations += 1

    # Create dictionary with the counts and pass it to the template
    counts = {
        'Spaces': spaces,
        'Alphabets': alphabets,
        'Numbers': numbers,
        'Punctuations': punctuations
    }

    # Check which radio button is selected and perform the corresponding operation
    if operation == "punctuation":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed_text = ""
        for char in text:
            if char not in punctuations:
                analyzed_text += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed_text, 'counts': counts}

    elif operation == "title":
        analyzed_text = text.title()
        params = {'purpose': 'Title Text', 'analyzed_text': analyzed_text, 'counts': counts}

    elif operation == "upper":
        analyzed_text = text.upper()
        params = {'purpose': 'Upper Cased Text', 'analyzed_text': analyzed_text, 'counts': counts}

    elif operation == "lower":
        analyzed_text = text.lower()
        params = {'purpose': 'Lower Cased Text', 'analyzed_text': analyzed_text, 'counts': counts}

    elif operation == "invert":
        analyzed_text = text[::-1]
        params = {'purpose': 'Inverted Text', 'analyzed_text': analyzed_text, 'counts': counts}

    else:
        return HttpResponse("Please select an operation and try again")

    return render(request, "output.html", params)




