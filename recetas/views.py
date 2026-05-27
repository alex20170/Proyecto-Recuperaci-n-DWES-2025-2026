from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .models import Receta, Comentario
from .forms import RecetaForm, ComentarioForm

class ListaRecetasView(ListView):
    model = Receta
    template_name = 'recetas/lista_recetas.html'
    context_object_name = 'recetas'
    ordering = ['-fecha_creacion']

    def get_queryset(self):
        queryset = Receta.objects.all()
        
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(titulo__icontains=q)
        
        autor = self.request.GET.get('autor')
        if autor:
            queryset = queryset.filter(autor__username__icontains=autor)
        
        categoria = self.request.GET.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria__id=categoria)
        
        return queryset


class DetalleRecetaView(DetailView):
    model = Receta
    template_name = 'recetas/detalle_receta.html'
    context_object_name = 'receta'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comentario'] = ComentarioForm()
        return context


class CrearRecetaView(LoginRequiredMixin, CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'recetas/form_receta.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class EditarRecetaView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'recetas/form_receta.html'

    def test_func(self):
        receta = self.get_object()
        return self.request.user == receta.autor


class EliminarRecetaView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Receta
    template_name = 'recetas/confirmar_eliminar.html'
    success_url = reverse_lazy('lista_recetas')

    def test_func(self):
        receta = self.get_object()
        return self.request.user == receta.autor


@login_required
def crear_comentario(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.receta = receta
            comentario.save()
    
    return redirect('detalle_receta', pk=receta.pk)


@login_required
def eliminar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    
    if request.user == comentario.autor:
        receta_pk = comentario.receta.pk
        comentario.delete()
        return redirect('detalle_receta', pk=receta_pk)
    
    return redirect('detalle_receta', pk=comentario.receta.pk)