from django.http import HttpResponse
from django.shortcuts import render, resolve_url, redirect
import random
# Create your views here.
from django.views import generic

from django.views import View
class ListStudyMView(generic.ListView):
    template_name = ""
    
    def get_queryset(self):
        pass

class TopicIndexView(View):
    def get(self, request):
        return render(request, 'studym/topic-index.html', {
            'title':'Topics',
            'topics':Topic.objects.all()
        })

from django.core.paginator import Paginator
ql = [{'question': '1. Which country has recently signed a free trade agreement (FTA) with the United Arab Emirates? ', 'options': ['Australia', 'Israel', 'France', 'Italy'], 'answer': 'Israel', 'note': 'Israel has signed a free trade agreement with the United Arab Emirates, its first big trade pact with an Arab state.\nThe agreement, which aimed at boosting trade between the two Middle Eastern nations, would encourage more Israeli companies to set up offices in the UAE, particularly in Dubai. The deal with Israel is UAE’s second bilateral free trade agreement after a similar accord with India in February.'}, {'question': '2. ‘Operation Rakth Chandan’ was associated with which institution? ', 'options': ['Narcotics Control Bureau', 'Indian Army', 'Indian Navy', 'Directorate of Revenue Intelligence'], 'answer': 'Directorate of Revenue Intelligence', 'note': 'The Directorate of Revenue Intelligence (DRI) recently launched Operation Rakth Chandan recovered 14.63 MT of Red Sanders estimated at Rs 11.70 crores in the international market.\nThe red sanders were seized from a consignment at ICD Sabarmati which was to be exported to Sharjah, UAE. The suspect container was scanned through a ‘container scanning device’.'}, {'question': '3. ‘Hurricane Agatha’, the first of the Pacific season, recently hit which country? ', 'options': ['Argentina', 'Canada', 'Mexico', 'Paraguay'], 'answer': 'Mexico', 'note': '‘Hurricane Agatha’, the first of the Pacific season hit Mexico and the casualties climbed to at least 10 dead and around 20 missing in southern Mexico.\nHeavy rains triggered landslides and flooding in the country. The storm was the strongest to make landfall along Mexico’s Pacific coast in May since record keeping began in 1949. Mexico is regularly hit by tropical storms on both its Pacific and Atlantic coasts, between May and November.'}, {'question': '4. Libreville is the capital of which city, recently visited by the Vice President of India? ', 'options': ['Senegal', 'Gabon', 'Guinea', 'Cameroon'], 'answer': 'Gabon', 'note': 'Vice President M. Venkaiah Naidu is on a visit to Gabon, Senegal, and Qatar, the first visit from India at the level of Vice President to the three countries.\nLibreville is the capital of the Central- African country Gabon. The Vice President reiterated the commitment of the Government of India to be Gabon’s reliable partner. The bilateral trade between the countries reached USD 1.12 billion in 2021-22.'}, {'question': '5. ‘Appreciate all parents throughout the world’ is the theme of which day observed on June 1? ', 'options': ['World Day of Families', 'Global Day of Parents', 'World Day of Mothers', 'Global Day of Children'], 'answer': 'Global Day of Parents', 'note': 'The Global Day of Parents is annually celebrated on 1 June to appreciate the commitment of parents towards their children.\nThe UN General Assembly proclaimed 1994 as the International Year of the Family and 15 May each year as the International Day of Families. The UNGA later announced that 1 June will be observed as the Global Day of Parents. The theme for Global Day of Parents 2022 is ‘Appreciate all parents throughout the world.’'}, {'question': '6. Who has topped the 2021 Fortune 500 list of the most highly compensated CEOs? ', 'options': ['Jack Ma', 'Elon Musk', 'Tim Cook', 'Jensen Huang'], 'answer': 'Elon Musk', 'note': 'Elon Musk, CEO of SpaceX and Tesla, has topped the 2021 Fortune 500 list of the most highly compensated CEOs.\nIn 2021 Musk received compensation worth almost USD 23.5 billion while Tesla ranked 65 on this year’s Fortune 500 list. Apple Inc. CEO Tim Cook received USD 770.5 million in 2021 and Jensen Huang, the NVIDIA chief, received USD 561 million in 2021.'}, {'question': '7. What is the position of India in the Asia Cup hockey tournament 2022? ', 'options': ['First', 'Second', 'Third', 'None of the above'], 'answer': 'Third', 'note': 'India beat Japan for the second time in the eight-team tournament to win bronze in the Asia Cup hockey in Jakarta.\nSouth Korea beat Malaysia 2-1 in the final match to clinch the gold medal. South Korea won the Asia Cup for the fifth time, the most in the list. India and Pakistan have won the Asia cup title thrice.'}, {'question': '8. What is the name given to robots that are flexible which can be programme to execute specific tasks? ', 'options': ['Flexi Robots', 'Soft Robots', 'Super Robots', 'Multi-task Robots'], 'answer': 'Soft Robots', 'note': 'Soft robots are robots that are flexible and unlike traditional robots can be used to perform more delicate functions.\nSoft robots can be programmed to execute specific tasks such as reaching into difficult gaps or holding onto delicate objects.'}, {'question': '9. Which Indian film-maker has been selected for the ‘Locarno Kids Award la Mobiliare’ at Locarno Film Festival? ', 'options': ['Gitanjali Rao', 'Zoya Akhtar', 'Harshavardhan Kulkarni', 'Sriram Raghavan'], 'answer': 'Gitanjali Rao', 'note': 'Indian Film-maker Gitanjali Rao is set to be honoured with an award during the 75th edition of the Locarno Film Festival.\nThe filmmaker will receive the Locarno Kids Award la Mobiliare, the award dedicated to personalities for conveying the love of cinema to younger viewers. The award will be presented at the film gala, held every year in Locarno, Switzerland.'}, {'question': '10. Which is the 20th European country to adopt the euro currency from 2023? ', 'options': ['Monaco', 'Malta', 'Croatia', 'Luxembourg'], 'answer': 'Croatia', 'note': 'Croatia is set to adopt the euro currency from the start of 2023 after meeting all the criteria to join the European Commission.\nThis move will make Croatia the 20th European country to use the single currency. European Commission President Ursula von der Leyen said in a statement that Croatia has made a step towards adopting the Euro common currency.'}]
class CurrentAffairsQuizView(View):
    def get(self, request):
        pgt = Paginator(ql, 1)
        p = pgt.get_page(request.GET.get('page', 0))
        # print(p.keys)
        return render(request, 'studym/current-affairs-quiz.html', {
            'title':'Current Affairs Quiz',
            'ques_list':ql,
            'page':pgt.get_page(request.GET.get('page', 0))

        })

from .forms import *
class TopicCreateView(View):
    def get(self, request):
        return render(request, 'studym/topic-create.html', {
            'title':f'New Topic',
            'form':TopicForm
        })
    
    def post(self, request):
        form = TopicForm(request.POST)
        if form.is_valid():
            t = form.save()
            return redirect('topic-detail', t.slug)
        else:
            print('error in form')
            print(form.errors)
            return render(request, 'studym/topic-create.html', {
                'title':f'New Topic',
                'form':form
            })

class TopicUpdateView(View):
    def get(self, request, slug):
        topic = Topic.objects.get(slug=slug)
        return render(request, 'studym/topic-update.html', {
            'title':f'Update {topic.title.title()}',
            'form':TopicForm(instance=topic)
        })
    
    def post(self, request, slug):
        topic = Topic.objects.get(slug=slug)
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            t = form.save()
            return redirect('topic-detail', slugify(t.title))
        else:
            print('error in form')
            print(form.errors)
            return render(request, 'studym/topic-create.html', {
                'title':f'Update {topic.title.title()}',
                'form':form
            })


class TopicDetailView(View):

    def get(self, request, slug):
        topic = Topic.objects.get(slug=slug)
        return render(request, 'studym/topic-detail.html', {
            'title':topic.title,
            'topic':topic
        })

class TopicFileCreateView(View):
    def get(self, request):
        return render(request, 'studym/topic-file-create.html', {
            'title':'New Topic By Txt File',
            'form':TopicFileForm
        })

def checkTitle(request):
    title = request.GET.get('title')
    topic = Topic.objects.filter(slug=slugify(title))
    if len(topic):
        return HttpResponse('Topic with this Title already exists.')
    else:
        return HttpResponse('')

def topicSearch(request):
    q = request.GET.get('q')
    print('q >', q)
    topics = Topic.objects.filter(title__icontains=q)
    print(topics)
    print('not len prn zero time')
    if not len(topics):
        print('not len prn')
        return HttpResponse('No matching topics'.title())
    print('not len prn second gti')
    return HttpResponse(render_to_string('studym/search-results.html', {
        'results':topics
    }))

def checkText(request):
    text = request.GET.get('text')
    if len(text):
        return HttpResponse('')
    else:
        return HttpResponse('Text should not be empty'.title())
# from django.template import RequestContext
from django.template.loader import render_to_string
from .utilities import TopicAPI
def topicFileUpload(request):
    file = request.FILES.get('file')
    topic = TopicAPI(file.read().decode())
    return HttpResponse(render_to_string('studym/topic-update.html', {
        'form':TopicForm(initial={'title':topic.title(), 'text':topic.text}),
        'toPostUrl':resolve_url('topic-create')
    }, request=request))

def topicDelete(request, slug):
    topic = Topic.objects.get(slug=slug)
    topic.delete()
    return redirect('topic-index')