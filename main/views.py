"""main(루트 페이지) views 모듈입니다."""
from django.shortcuts import render

from board.models import Board

from .models import TopBanner
from helpers.default import default_response
from copy import deepcopy as dp

def get_top_banner():
    """ TopBanner를 가져오는 함수입니다. """
    try:
        banner = TopBanner.objects.get(is_active=True)
        return banner
    except TopBanner.DoesNotExist:  # pylint: disable=no-member
        return None


def root(request):
    """ 루트 페이지 뷰입니다. """
    response = dp(default_response)

    response.update({
        'top_banner': get_top_banner(),
    })

    published_boards = Board.objects.published().all()
    response['boards'] = published_boards

    return render(request, 'main/index.dj.html', response)
