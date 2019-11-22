



from django.shortcuts import render,redirect
from Documents.models import Paragraph,InvertedMap
import threading
# Create your views here.

from Documents.utils import handleUpload,handleSearch,clearDatabase

def upload_documents(request):
    out=handleUpload(request)
    if out:
        return out
    context={
    }
    return render(request,"Documents/upload.html",context)


def clear_documents(request):
    thr=threading.Thread(target=clearDatabase)
    thr.start()
    return redirect('/')



def search_documents(request):
    out=handleSearch(request)
    if out:
        return out
    if request.POST:
        data={
            "maps":[],
            "word":'',
            "count":0,
            "time_taken":0.00000000
        }
        return render(request,"ajax_response/search_response.html",data)
    context={

    }
    return render(request,"Documents/search.html",context)





