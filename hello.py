import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="World"))

    def resolve_hello(self, info, name):
        return f"Hello {name}"

if __name__ == "__main__":
    schema = graphene.Schema(query = Query)
    result = schema.execute("{ hello }")
    print(result.data["hello"])