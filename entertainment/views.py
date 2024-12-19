from audioop import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import EntertainmentCenter, Event
from .forms import EntertainmentCenterForm, CenterTypeForm, EventForm
from django.contrib import messages

# === Блок функцій для управління розважальними центрами ===

# Створення нового розважального центру
def center_add(request):
    if request.method == "POST":
        form = EntertainmentCenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('center_list')  # Перенаправлення на сторінку зі списком центрів
    else:
        form = EntertainmentCenterForm()  # Пустий шаблон форми
    return render(request, 'entertainment/center_form.html', {'form': form})


# Редагування даних розважального центру
def center_edit(request, pk):
    center = get_object_or_404(EntertainmentCenter, pk=pk)  # Отримання центру за первинним ключем
    if request.method == "POST":
        form = EntertainmentCenterForm(request.POST, instance=center)  # Передача існуючого об'єкта для редагування
        if form.is_valid():
            form.save()  # Збереження змін
            return redirect('center_detail', pk=center.pk)  # Перенаправлення на деталі центру
    else:
        form = EntertainmentCenterForm(instance=center)  # Заповнення форми даними центру
    return render(request, 'entertainment/center_form.html', {'form': form})


# Видалення розважального центру
def center_delete(request, pk):
    center = get_object_or_404(EntertainmentCenter, pk=pk)  # Отримання центру за первинним ключем
    if request.method == "POST":  # Обробка підтвердження видалення
        center.delete()
        return redirect('center_list')  # Перенаправлення на список центрів
    return render(request, 'entertainment/center_confirm_delete.html', {'center': center})


# Перегляд списку розважальних центрів
def center_list(request):
    centers = EntertainmentCenter.objects.all()  # Отримання всіх центрів
    return render(request, 'entertainment/center_list.html', {'centers': centers})


# Перегляд деталей розважального центру
def center_detail(request, pk):
    center = get_object_or_404(EntertainmentCenter, pk=pk)  # Отримання центру за первинним ключем
    return render(request, 'entertainment/center_detail.html', {'center': center})


# Додавання типу розважального центру
def center_type_add(request):
    if request.method == "POST":
        form = CenterTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('center_list')  # Перенаправлення на список центрів
    else:
        form = CenterTypeForm()
    return render(request, 'entertainment/center_type_form.html', {'form': form})


# === Блок функцій для управління подіями ===

# Список подій
def event_list(request):
    events = Event.objects.all()  # Отримання всіх подій
    return render(request, 'entertainment/event_list.html', {'events': events})


# Створення нової події
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Перенаправлення на сторінку зі списком подій
    else:
        form = EventForm()
    return render(request, 'entertainment/add_event.html', {'form': form})


# Перегляд деталей події
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)  # Отримання події за первинним ключем
    return render(request, 'entertainment/event_detail.html', {'event': event})


# Видалення події
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)  # Отримання події за первинним ключем
    if request.method == 'POST':  # Обробка підтвердження видалення
        event.delete()
        messages.success(request, 'Подію успішно видалено.')
        return redirect('event_list')  # Перенаправлення на список подій
    return render(request, 'entertainment/event_confirm_delete.html', {'event': event})
