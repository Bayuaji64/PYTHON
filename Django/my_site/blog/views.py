from django.shortcuts import render
from datetime import date


all_posts = [
    {
        "slug": 'hike-in-the-mountains',
        "image": 'mountains.jpg',
        "author":"Bayuaji",
        "date": date(2024, 3,10),
        "title":"Mountain Hiking",
        "excerpt":"Mountain Mountain Mountain",
        "content": """
            Hiking is an activity that combines physical exercise with outdoor adventure, offering the chance to enjoy breathtaking natural landscapes while keeping fit. 
        Through challenging trails, hikers can explore diverse terrains, from dense forests to towering mountains, enriching experiences and enhancing both mental and physical strength. 
        Moreover, hiking fosters close relationships among participants, building teamwork and camaraderie amidst the stunning beauty of nature.
    """
    },
    {
        "slug": 'progamming',
        "image": 'coding.png',
        "author":"Bayuaji",
        "date": date(2024, 3,11),
        "title":"Progamming is Great!",
        "excerpt":"Progamming Progamming Progamming",
        "content": """
            Hiking is an activity that combines physical exercise with outdoor adventure, offering the chance to enjoy breathtaking natural landscapes while keeping fit. 
        Through challenging trails, hikers can explore diverse terrains, from dense forests to towering mountains, enriching experiences and enhancing both mental and physical strength. 
        Moreover, hiking fosters close relationships among participants, building teamwork and camaraderie amidst the stunning beauty of nature.
    """
    },
    {
        "slug": 'into-the-woods',
        "image": 'woods.jpg',
        "author":"Bayuaji",
        "date": date(2024, 3,9),
        "title":"Nature At Its Best!",
        "excerpt":"Nature nature nature",
        "content": """
            Hiking is an activity that combines physical exercise with outdoor adventure, offering the chance to enjoy breathtaking natural landscapes while keeping fit. 
        Through challenging trails, hikers can explore diverse terrains, from dense forests to towering mountains, enriching experiences and enhancing both mental and physical strength. 
        Moreover, hiking fosters close relationships among participants, building teamwork and camaraderie amidst the stunning beauty of nature.
    """
    }
]
# Create your views here.

def get_date(post):
    return post['date']
def starting_page(request):
    sorted_posts= sorted(all_posts,key=get_date)

    latest_post= sorted_posts[-3:]

    return render(request, "blog/index.html", {
        "posts": latest_post
    })

def posts(request):
    return render(request,"blog/all-posts.html", {
        "all_posts": all_posts

    })

def post_detail(request,slug):
    identified_post= next(post for post in all_posts if post['slug']==slug)

    return render(request,"blog/post-detail.html",{
        "post": identified_post
    })

