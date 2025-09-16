from .models import Category, Product


class ProductService:

    @staticmethod
    def product_in_category(category_id):
        product_list = Product.objects.filter(category_id=category_id)

        return product_list

    @staticmethod
    def category_title(category_id):
        category_title = Category.objects.get(id=category_id).title

        return category_title
