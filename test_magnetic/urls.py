from django.urls import path
from . import views

urlpatterns = [
    path('systems/', views.systems, name='systems'),
    path('systems/structure/<int:id>', views.structure, name='structure'),
    path('systems/magnetic/<int:id>', views.magnetic, name='magnetic'),
    path('systems/magnetic/exchange/<int:id>', views.exchange, name='exchange'),
]
