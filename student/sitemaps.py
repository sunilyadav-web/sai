from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['result','faith','about','md_message','courses','health_science_courses','engineering_courses','management_courses','certified_courses','alumini','academics','library','research','global_option','student_life','contact_us','apply','home2','export','import','certificate','admitcard','idcard','exam:home','exam:exam-start','exam:exam-submission','users:register','users:login','users:logout']
    def location(self, item):
        return reverse(item)