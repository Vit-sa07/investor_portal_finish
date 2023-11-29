from django.http import JsonResponse

def api_overview(request):
    api_urls = {
        'User List': '/user-list/',
        'User Detail View': '/user-detail/<str:pk>/',
        'User Create': '/user-create/',
        'User Update': '/user-update/<str:pk>/',
        'User Delete': '/user-delete/<str:pk>/',

        'Market Info': '/market-info/',
        'Specific Crypt Info': '/market-info/<str:crypto_name>/',

        'News List': '/news-list/',
        'Specific News': '/news-detail/<str:pk>/',

        'Project List': '/project-list/',
        'Specific Project Info': '/project-detail/<str:pk>/',

        # ... add other endpoints as you deem fit
    }

    return JsonResponse(api_urls)
