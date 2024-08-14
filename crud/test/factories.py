import factory

from crud.models import question, choice


class questionfactory(factory.django.DjangoModelFactory):
    class Meta:
        model = question

    question_text = factory.Faker('text')
    pub_date = factory.Faker('date')


class choicefactory(factory.django.DjangoModelFactory):
    class Meta:
        model = choice

    choice_text = factory.Faker('text')
    votes = factory.Faker('random_int')
    question = factory.SubFactory(questionfactory)
