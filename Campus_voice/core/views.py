from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Issue, Vote

@login_required
def issue_list(request):
    issues = Issue.objects.all().order_by('-created_at')
    return render(request, 'issues.html', {'issues': issues})

@login_required
def create_issue(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        Issue.objects.create(
            title=title,
            description=description,
            category=category,
            created_by=request.user
        )
        return redirect('issues')
    return render(request, 'create_issue.html')

@login_required
def vote_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    Vote.objects.get_or_create(user=request.user, issue=issue)
    return redirect('issues')
