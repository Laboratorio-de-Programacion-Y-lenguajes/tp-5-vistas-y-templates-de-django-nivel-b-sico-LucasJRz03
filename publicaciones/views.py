from django.views.generic import TemplateView, ListView, DetailView
from .models import Publicacion

# ---------------------------------------------------------------------------
# InicioView
# --------------------------------------------------------------------
# TODO: Implementar InicioView usando TemplateView.
#
# Requisitos:
#   - template_name = "publicaciones/inicio.html"
#   - Sobreescribir get_context_data() para agregar al contexto:
#       "titulo"  → str con el nombre del portal
#       "mensaje" → str de bienvenida

class InicioView(TemplateView):
    template_name = "publicaciones/inicio.html"
    #**kwargs para cuando no sabes cuántos parámetros con nombre se pasarán  
    def get_context_data(self, **kwargs):
        #Primero recupera el contexto base llamando a super()
        context = super().get_context_data(**kwargs)

        #Variables personalizadas
        context["titulo"] = "Portal de publicaciones"
        context["mensaje"] = "Bienvenido/a al portal de publicaciones."

        return context

# ---------------------------------------------------------------------------
# PublicacionListView
# ---------------------------------------------------------------------------
# TODO: Implementar PublicacionListView usando ListView.
#
# Requisitos:
#   - model = Publicacion
#   - context_object_name = "publicacion_list"
#     (el template accede a esta variable con {% for pub in publicacion_list %})
#
class PublicacionesListView(ListView):
    modal = Publicacion
    context_object_name = "publicacion_list"
    # buscaría 'publicaciones/publicacion_list.html'  

# ---------------------------------------------------------------------------
# PublicacionDetailView
# ---------------------------------------------------------------------------
# TODO: Implementar PublicacionDetailView usando DetailView.
#
# Requisitos:
#   - model = Publicacion
#   - context_object_name = "publicacion"
#     (el template accede a esta variable con {{ publicacion.titulo }})
#   - pk_url_kwarg = "publicacion_id"
#     (indica que el parámetro en la URL se llama "publicacion_id", no "pk")
#   - Si no existe la publicación → responde automáticamente con 404
#
# Pista:
#   class PublicacionDetailView(DetailView):
#       model = ...
#       context_object_name = "..."
#       pk_url_kwarg = "..."