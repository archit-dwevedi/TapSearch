

from Documents.models import Paragraph,InvertedMap,FileUpload
from django.shortcuts import render,redirect
import threading
import time
import textract
from TapSearch.settings import BASE_DIR
from django.core.files.storage import FileSystemStorage
import os
from copy import deepcopy



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


def uploadParagraphs(request,s):
    files=request.FILES.getlist(s)
    for i in files:
        myfile=i
        j=deepcopy(i)
        fs = FileSystemStorage()
        filename = fs.save("local/"+myfile.name,myfile)
        uploaded_file_url = fs.url(filename)
        text=textract.process(BASE_DIR+uploaded_file_url[6:])
        print(type(str(text)),'\n\n\n\n\n\n\n')
        paragraphs=str(text,'utf-8').strip().split("\n")
        count=paragraphs.count('\r')
        for i in range(count):
            paragraphs.remove('\r')
        p=[]
        for i in range(len(paragraphs)):
            if paragraphs[i]:
                obj=Paragraph.objects.filter(text=paragraphs[i]).first()
                if not(obj):
                    obj=Paragraph(text=paragraphs[i],doc=j)
                    obj.save()
                    p.append(obj)
        thr=threading.Thread(target=createInvertMap,args=[p])
        thr.start()

    return 1


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
    elif request.FILES.getlist('file'):
        thr=threading.Thread(target=uploadParagraphs,args=[request,'file'])
        thr.start()
        return redirect('/')
    elif request.FILES.getlist('image'):
        thr=threading.Thread(target=uploadParagraphs,args=[request,'image'])
        thr.start()
        return redirect('/')
    else:
        return 0




def handleSearch(request):
    if request.POST.get('word_ajax'):
        start_time=time.time()
        if request.POST.get('by_word_ajax')=="true":
            objs=InvertedMap.objects.filter(word=request.POST.get('word_ajax').lower())
        else:
            objs=InvertedMap.objects.filter(word__contains=request.POST.get('word_ajax').lower())
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