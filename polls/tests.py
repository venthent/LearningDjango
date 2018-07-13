import datetime
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from .models import Question


# Create your tests here.


def create_quesiton(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_quesiton(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_quesion=create_quesiton(question_text='Past Question.',days=-5)
        url=reverse('polls:detail',args=(past_quesion.id,))
        res=self.client.get(url)
        self.assertContains(res,past_quesion.question_text)
