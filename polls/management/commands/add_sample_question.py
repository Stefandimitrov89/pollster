from django.core.management.base import BaseCommand, CommandError
from polls.models import Choice, Question  # Import the model classes we just wrote.
from django.utils import timezone


class Command(BaseCommand):

    # def add_arguments(self, parser):
        # parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        help = 'adds a static question to the database'
        # No questions are in the system yet.
        Question.objects.all()
        # answer: <QuerySet []>

        # Create a new Question.
        # Support for time zones is enabled in the default settings file, so
        # Django expects a datetime with tzinfo for pub_date. Use timezone.now()
        # instead of datetime.datetime.now() and it will do the right thing.
        q = Question(question_text="What's new?", pub_date=timezone.now())

        # Save the object into the database. You have to call save() explicitly.
        q.save()

        # Now it has an ID.
        print(q.id)
        # answer: 1

        # Access model field values via Python attributes.
        print(q.question_text)
        # "What's new?"
        print(q.pub_date)
        # print( datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=UTC) )

        # Change values by changing the attributes, then calling save().
        q.question_text = "What's up?"
        q.save()

        # objects.all() displays all the questions in the database.
        print(Question.objects.all())
        # <QuerySet [<Question: Question object (1)>]>