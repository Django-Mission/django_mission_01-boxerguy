from ast import operator
from multiprocessing import context
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse


# # Create your views here.



def lotto(reqeust):
    import random
    result = random.sample(range(1,46), 6)
    # num = input()
    # for i  in range(0, int(num)):
    #     lotto_input = random.sample(range(1, 46), 6)
    #     lotto_input.sort()



    return render(reqeust, 'lotto.html', {'result' : result})
