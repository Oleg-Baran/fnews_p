import graphene
import blog.schema

class Query(blog.schema.Query):
    pass

schema = graphene.Schema(query = Query)