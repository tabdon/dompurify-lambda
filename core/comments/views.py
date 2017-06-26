# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from .models import Comments
from .forms import CommentForm
from .utilities.dom_purify_lambda import dom_purify


def create_comment(request):

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            dirty_dom = form.cleaned_data['comment']
            clean_dom = dom_purify(dirty_dom)
            instance = Comments.objects.create(comment=clean_dom)
            return render(request, 'comment.html', {'obj': instance})
    else:
        form = CommentForm()

    context = {
        'form': form,
    }

    return render(request, 'comment.html', context)
