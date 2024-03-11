from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
	"january": "Eat no sugar for the entire month!",
	"february": "Walk for at leatas 20 minutes everyday!",
	"march": "Learn Django for at least 1 modules every day",
	"april": "Eat no sugar for the entire month!",
	"may": "Walk for at leatas 20 minutes everyday!",
	"june": "Learn Django for at least 1 modules every day",
	"july": "Eat no sugar for the entire month!",
	"august": "Walk for at leatas 20 minutes everyday!",
	"september": "Learn Django for at least 1 modules every day",
	"october": "Eat no sugar for the entire month!",
	"november": "Walk for at leatas 20 minutes everyday!",
	"december": None,
}

# Create your views here.


def index(request):

	list_items = ""
	months = list(monthly_challenges.keys())
	
	# for month in months:
	# 	capitalized_month = month.capitalize()
	# 	month_path= reverse("month-challenge",args=[month])
	# 	list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
	
	# response_data = f"<ul>{list_items}</ul>"
	# return HttpResponse(response_data)

	return render(request,"challenges/index.html",{
		"months":months
	})


def monthly_challange_by_number(request,month):
	months=list(monthly_challenges.keys())

	if month > len(months):
		return HttpResponseNotFound("Invalid Mounth")
	redirect_month = months[month-1]
	redirect_path = reverse("month-challenge", args=[redirect_month])
	return HttpResponseRedirect(redirect_path)



def monthly_challenge(request, month):
	try:
		challenge_text = monthly_challenges[month]

		return render(request,"challenges/challenge.html",{
			"text": challenge_text,
			"month_name":month
		})
		# responese_data = render_to_string("challenges/challenge.html")
		# return HttpResponse(responese_data)
	except:
		# response_data = render_to_string("404.html")
		# return HttpResponseNotFound(response_data)
		raise Http404()

	
