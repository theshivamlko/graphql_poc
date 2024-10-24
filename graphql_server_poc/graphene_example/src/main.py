from graphene import Schema, ObjectType, String, Int
import random


class Query(ObjectType):
    hello=String(name=String(default_value="world"))
    gender=String(name=String(default_value=""))
    id= Int()
    age= Int()


    def resolve_hello(self,info,name):
        return  f'Hello {name} '

    def resolve_gender(self,info,name):
        return  f'h{name} '

    def resolve_id(self,info):
        return random.randint(100, 999)



schema=Schema(query=Query)

gql=''' 
{
    id
    hello
    gender
}
'''


if __name__ == "__main__":
    result = schema.execute(gql)
    print(result)
    print(result.data)




