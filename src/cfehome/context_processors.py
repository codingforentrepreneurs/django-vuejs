from django.conf import settings


def vue_js_files(request):
    static_base_dir = settings.STATICFILES_BASE_DIR
    vue_name = 'vue-prod' if settings.VUE_PROD else 'vue-dev'
    vue_dir = static_base_dir / vue_name 
    js_files = [x.relative_to(static_base_dir) for x in vue_dir.glob("**/*.js")]
    css_files =[x.relative_to(static_base_dir) for x in vue_dir.glob("**/*.css")]
    return {
        "vue_js_paths": list(js_files),
        "vue_css_paths": list(css_files)
        
    }