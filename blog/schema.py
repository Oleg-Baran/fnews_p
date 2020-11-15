import graphene
from graphene_django.types import DjangoObjectType
from .models import ArticleImage, ArticleTag, Article, Comment
"""
По pep8 між класами треба залишати 2 вільні рядки, окрім "класу в класі"

"""
class ArticleImageSchema(DjangoObjectType):
    class Meta:
        model = ArticleImage
        fields = '__all__'


class ArticleTagSchema(DjangoObjectType):
    class Meta:
        model = ArticleTag
        fields = '__all__'


class ArticleSchema(DjangoObjectType): # Об'єкт який перетворює об'єкт джанго в об'єкт qrapgQL
    class Meta: # Вказує за сам об'єкт а не на те що в ньому 
        model = Article       # прив'язуємо модель статті до схеми, яку ми ств
        fields = '__all__'    # переносимо всі поля в цю схему


class CommentSchema(DjangoObjectType):
    class Meta:
        model = Comment
        fields = '__all__'


class FilterArticlesSchema(graphene.ObjectType):
    articles = graphene.List(ArticleSchema)


class Query(graphene.ObjectType): #?
    article = graphene.List(ArticleSchema) #Create list for pull articles
    article_tag = graphene.List(ArticleTagSchema)
    comment = graphene.List(CommentSchema)

    filter_articles = graphene.Field(
        FilterArticlesSchema,
        id=graphene.ID(required=False),
        author=graphene.Int(required=False),
        title=graphene.Int(required=False),
        text= graphene.Int(required=False),
        pub_date=graphene.Date(required=False),
        tag= graphene.Int(required=False),
        image=graphene.Int(required=False)
    )

    def resolve_article_tag(self, info, **kwargs):
        return ArticleTag.objects.all()

    def resolve_article(self, info, **kwargs): #Приймає сама себе, приймає інфо, КВАРГ приймає кілька значень (поля, які ми задаєм)(** - невизначена к-сть значень та які саме вони будуть приймати функції)
        return Article.objects.all()

    def resolve_comment(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_filter_articles(self, info, **kwargs):
        filter_articles = Article.objects.all()

        if 'id' in kwargs:
            filter_articles = filter_articles.filter(id = kwargs['id'])

        if 'author' in kwargs:
            filter_articles = filter_articles.filter(author = kwargs['author'])

        if 'title' in kwargs:
            filter_articles = filter_articles.filter(title = kwargs['title'])

        if 'text' in kwargs:
            filter_articles = filter_articles.filter(text = kwargs['text'])

        if 'pub_date' in kwargs:
            filter_articles = filter_articles.filter(pub_date = kwargs['pub_date'])

        if 'tag' in kwargs:
            filter_articles = filter_articles.filter(tag = kwargs['tag'])

        if 'image' in kwargs:
            filter_articles = filter_articles.filter(image = kwargs['image'])

        return {
            'articles': filter_articles
        }

