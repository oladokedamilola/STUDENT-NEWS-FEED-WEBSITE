from django.shortcuts import render

def index(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        # Perform search logic here, for example:
        # results = MyModel.objects.filter(name__icontains=query)
        results = ["Result 1", "Result 2", "Result 3"]  # Example results
    return render(request, 'search/index.html', {'results': results})
