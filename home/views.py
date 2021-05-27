from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View


class Home(View): 
    template_name = 'home/home.html'
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, *args, **kwargs):
        return render(self.request, self.template_name)


class SwitchDarkMode(View):
    
    def dispatch(self, *args, **kwargs):
        super().dispatch(*args, **kwargs)

        http_referer = self.request.META.get(
            'HTTP_REFERER', reverse('home:initial')
        )

        self.dark = self.request.POST.get('dark-mode')
        print(self.dark)
        if self.dark:
            self.request.session['dark'] = 'checked' 
        else:
            if self.request.session.get('dark'):
                del self.request.session['dark']

        self.request.session.save()
        return redirect(http_referer)





# class SwitchDarkMode(View):
#     template_name = 'home/home.html'

#     def setup(self, *args, **kwargs):
#         super().setup(*args, **kwargs)

#         self.dark = self.request.POST.get('dark-mode')

#         if self.dark:
#             self.request.session['dark'] = 'checked' 
#         else:
#             if self.request.session.get('dark'):
#                 del self.request.session['dark']
        
#         print(self.request.session.get('dark'))
    
#     def get(self, *args, **kwargs):
#         return render(self.request, self.template_name)

#     def post(self, *args, **kwargs):
#         return render(self.request, self.template_name)
