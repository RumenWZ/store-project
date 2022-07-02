from StoreProject.main.views import error_404, error_500


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code == 404:
            return error_404(request)
        elif response.status_code >= 500:
            return error_500(request)
        return response

    return middleware