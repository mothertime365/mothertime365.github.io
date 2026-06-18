from django.views import generic
from datetime import datetime
from .models import DailyQuote

class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        # Bugun yilning nechanchi kuni ekanligini aniqlash (1-365)
        current_day = datetime.now().timetuple().tm_yday

        # O'sha kunga mos iborani bazadan qidirish
        try:
            context['quote'] = DailyQuote.objects.get(day_number=current_day)
        except DailyQuote.DoesNotExist:
            # Agar hali o'sha kunga ibora kiritilmagan bo'lsa xato bermasligi uchun
            context['quote'] = {"text": "Bugun uchun ibora kiritilmagan."}

        return context
