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
