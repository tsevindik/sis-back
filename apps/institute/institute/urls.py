from django.conf.urls import url

from .views import (UniversityConfigHomeView, PrimaryUniversityView, UniversityConfigView, UniversityTransView,
                    UniversityTransByNeutralIdView, UniversityTransByNeutralIdLanguageView)

urlpatterns = [
    # University config views concerning primary university
    url(r'^university-config-home/$', UniversityConfigHomeView.as_view(), name="university_config_home"),
    url(r'^university-config/$', UniversityConfigView.as_view(), name="university_config"),
    url(r'^primary-university/$', PrimaryUniversityView.as_view(), name="primary_university"),

    # University trans views
    url(r'^university-trans/$', UniversityTransView.as_view(), name="university_trans"),
    url(r'^university-trans/neutral/(?P<neutral>\d+)/$',
        UniversityTransByNeutralIdView.as_view(),
        name="university_trans_by_id"),
    url(r'^university-trans/neutral/(?P<neutral>\d+)/(?P<language_code>[\w\-]+)/$',
        UniversityTransByNeutralIdLanguageView.as_view(),
        name="university_trans_by_id_language"),
]
