from applications.categories.models import Category


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
    if not category:
        return []
    result = []
    category = Category.objects.filter(slug=category).first()
    print('>>>', category)
    if category:
        result.append({'name': category.name, 'slug': category.slug})
        while category.parent:
            category = category.parent
            result.append({'name': category.name, 'slug': category.slug})
    return result


