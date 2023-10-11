from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipes_view(request):
    for key in DATA.keys():
        if key in request.path:
            context = {"recipe": dict(DATA[key])}
    try:
        servs = int(request.GET.get("servings", 1))
    except Exception as Exc:
        servs = 1
    for key in context["recipe"].keys():
        context["recipe"][key] = context["recipe"][key] * servs
    return render(request, 'calculator/index.html', context)
