

from Documents.models import Paragraph,InvertedMap
from django.shortcuts import render,redirect
import threading
import time



def createInvertMap(paragraph):
    time.sleep(3)
    for i in paragraph:
        words=i.text.strip().split(" ")
        for j in words:
            final=InvertedMap.objects.filter(word=j.lower()).first()
            if not(final):
                final=InvertedMap(word=j.lower())
                final.save()
            final.paragraphs.add(i)
            # print(j)
    return 0


def handleUpload(request):
    if request.POST.get('text'):
        paragraphs=request.POST.get('text').strip().split("\n")
        count=paragraphs.count('\r')
        for i in range(count):
            paragraphs.remove('\r')
        p=[]
        for i in range(len(paragraphs)):
            paragraphs[i]=paragraphs[i][:-2]
            obj=Paragraph(text=paragraphs[i])
            obj.save()
            p.append(obj)
        thr=threading.Thread(target=createInvertMap,args=[p])
        thr.start()
        return redirect('/')
    elif request.POST.get('file'):
        pass
    elif request.POST.get('image'):
        pass
    else:
        return 0




def handleSearch(request):
    if request.POST.get('word_ajax'):
        start_time=time.time()
        objs=InvertedMap.objects.filter(word=request.POST.get('word_ajax').lower())
        count=0
        maps=[]
        for i in objs:
            for j in i.paragraphs.all():
                if not(j in maps):
                    count+=1
                    maps.append(j)
                if count>=10:
                    break
            if count>=10:
                break
        data={
            "maps":maps[:11],
            "time_taken":time.time()-start_time,
            "word":request.POST.get('word_ajax'),
            "count":count
        }
        print(data)
        return render(request,"ajax_response/search_response.html",data)
    else:
        return 0


def clearDatabase():
    objs=Paragraph.objects.all()
    for i in objs:
        i.delete()
    objs=InvertedMap.objects.all()
    for i in objs:
        i.delete()