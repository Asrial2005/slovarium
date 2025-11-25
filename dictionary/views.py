from django.shortcuts import render
from django.http import JsonResponse
from .models import Term

def term_list(request):
    return render(request, 'dictionary/term_list.html')

def all_terms(request):
    # Получаем все термины, отсортированные по алфавиту
    terms = Term.objects.all().order_by('word')

    # Группируем по первой букве
    grouped_terms = {}
    for term in terms:
        first_char = term.word[0].upper()
        if first_char not in grouped_terms:
            grouped_terms[first_char] = []
        grouped_terms[first_char].append(term)

    # Сортируем буквы по алфавиту
    sorted_grouped = sorted(grouped_terms.items())

    return render(request, 'dictionary/all_terms.html', {
        'grouped_terms': sorted_grouped
    })

def term_detail(request, pk):
    term = Term.objects.get(pk=pk)
    return render(request, 'dictionary/term_detail.html', {'term': term})

def search_terms(request):
    query = request.GET.get('q', '')
    if query:
        terms = Term.objects.filter(word__icontains=query) | Term.objects.filter(definition__icontains=query)
    else:
        terms = Term.objects.none()

    results = []
    for term in terms:
        results.append({
            'word': term.word,
            'definition': term.definition,
            'image_path': term.image_path,
            'video_path': term.video_path,
        })

    return JsonResponse({'terms': results})

def autocomplete_terms(request):
    query = request.GET.get('q', '')
    if query:
        terms = Term.objects.filter(word__icontains=query).values('word')[:10]
    else:
        terms = []

    return JsonResponse(list(terms), safe=False)
from django.http import JsonResponse
from .models import Term

def term_list(request):
    return render(request, 'dictionary/term_list.html')

def all_terms(request):
    # Получаем все термины, отсортированные по алфавиту
    terms = Term.objects.all().order_by('word')

    # Группируем по первой букве
    grouped_terms = {}
    for term in terms:
        first_char = term.word[0].upper()
        if first_char not in grouped_terms:
            grouped_terms[first_char] = []
        grouped_terms[first_char].append(term)

    # Сортируем буквы по алфавиту
    sorted_grouped = sorted(grouped_terms.items())

    return render(request, 'dictionary/all_terms.html', {
        'grouped_terms': sorted_grouped
    })

def term_detail(request, pk):
    term = Term.objects.get(pk=pk)
    return render(request, 'dictionary/term_detail.html', {'term': term})

def search_terms(request):
    query = request.GET.get('q', '')
    if query:
        terms = Term.objects.filter(word__icontains=query) | Term.objects.filter(definition__icontains=query)
    else:
        terms = Term.objects.none()

    results = []
    for term in terms:
        results.append({
            'word': term.word,
            'definition': term.definition,
            'image_path': term.image_path,
            'video_path': term.video_path,
        })

    return JsonResponse({'terms': results})

def autocomplete_terms(request):
    query = request.GET.get('q', '')
    if query:
        terms = Term.objects.filter(word__icontains=query).values('word')[:10]
    else:
        terms = []

    return JsonResponse(list(terms), safe=False)