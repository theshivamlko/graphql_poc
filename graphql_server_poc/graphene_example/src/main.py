from graphene import Schema, ObjectType, String, Int
import random


class User(ObjectType):
    name=String(name=String(default_value="John"))
    gender=String(name=String(default_value=""))
    id= Int()
    age= Int()

    def resolve_name(self,info,name):
        return  f'{name} '

    def resolve_gender(self,info,name):
        return  f'h{name} '

    def resolve_id(self,info):
        return random.randint(100, 999)

    def resolve_age(self,info):
        return random.randint(20, 50)


class Query(ObjectType):
    pass




    def resolve_hello(self,info,name):
        return  f'Hello {name} '

    def resolve_gender(self,info,name):
        return  f'h{name} '

    def resolve_id(self,info):
        return random.randint(100, 999)

    def resolve_age(self,info):
        return random.randint(20, 50)




schema=Schema(query=User)

gql=''' 
{
    id
    name
    gender
    age
}
'''


if __name__ == "__main__":
    result = schema.execute(gql)
    print(result)
    print(result.data)




