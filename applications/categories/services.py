from applications.categories.models import Category
from django.utils.translation import gettext as _


def get_flat_tree_categories_list(category):
    category = Category.objects.filter(slug=category).first()
    if category:
        children = [get_flat_tree_categories_list(category.slug) for category in category.get_children()]
        flat_children_list = [item for sublist in children for item in sublist]
        if flat_children_list:
            return flat_children_list
        return [category.slug]
    return []


def get_tree_ads_count(category):
    if category.is_leaf_node():
        return category.ads.count() or 0
    return sum([get_tree_ads_count(category) for category in category.get_children()])


def get_bread_crumbs(category):
    result = [{'name': _('All ads'), 'slug': ''}]
    if not category:
        return result
    category = Category.objects.filter(slug=category.split(',')[0]).first()
    categories = []
    if category:
        if not category.is_leaf_node():
            categories.append({'name': category.name, 'slug': category.slug})
        while category.parent:
            category = category.parent
            categories.append({'name': category.name, 'slug': category.slug})
        categories.reverse()
    result.extend(categories)
    return result


def is_category_exists(slug):
    return Category.objects.filter(slug=slug).exists()
