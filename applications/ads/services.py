from applications.ads.models import Ad
from applications.categories.services import get_flat_tree_categories_list


def get_ads_in_category(category):
    slug_list = get_flat_tree_categories_list(category)
    return Ad.objects.filter(category__slug__in=slug_list)
