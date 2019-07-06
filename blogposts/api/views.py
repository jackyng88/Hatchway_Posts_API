import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes



@api_view(['GET'])
def external_api_view(request):
    """
    Function that calls the Hatchways API making use of Django REST Framework's
    browsable API functionality by ways of decorating api_view.
    """
    data = {}
    tags = request.GET.get('tags', '')
    split_tags = tags.split(',')
    sort_by = request.GET.get('sortBy', '')
    direction = request.GET.get('direction', '')

    if tags:
        # if tag query parameters were provided
        url = 'https://hatchways.io/api/assessment/blog/posts?tag='
        for tag in split_tags:
            # updating the data dictionary with the returned responses
            query_url = url + tag
            r = requests.get(query_url)
            data.update(r.json())

        if (sort_by and not direction) or (sort_by and direction == 'asc'):
            # if sortBy param is provided and direction is asc or not provided
            # then sort by ascending order.
            ordered = sorted(data['posts'], key=lambda d: d[sort_by])
            return Response(ordered, status=status.HTTP_200_OK)

        elif sort_by and direction == 'desc':
            # if sortBy param is provided and direction provided is 'desc'
            ordered = sorted(data['posts'], reverse=True, key=lambda d: d[sort_by])
            return Response(ordered, status=status.HTTP_200_OK)

        else:
            # no sortBy parameter provided
            return Response(data, status=status.HTTP_200_OK)

    else:
        # no tags provided in initial GET request
        url = 'https://hatchways.io/api/assessment/blog/posts' 
        r = requests.get(url)
        data = r.json()
        return Response(data, status=status.HTTP_200_OK)
    



    