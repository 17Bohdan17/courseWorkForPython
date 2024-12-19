from audioop import reverse

from django.shortcuts import render, get_object_or_404, redirect
from .models import EntertainmentCenter, Visitor, Event
from .forms import EntertainmentCenterForm, CenterTypeForm, EventForm
from django.contrib import messages


from django.shortcuts import render, redirect




# Детали центра
def center_detail(request, pk):
    center = get_object_or_404(EntertainmentCenter, pk=pk)
    return render(request, 'entertainment/center_detail.html', {'center': center})


    if request.method == "POST":
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('center_detail', pk=center.pk)  # Перезагружаем страницу после добавления

    else:
        form = VisitorForm(initial={'center': center})

    return render(request, 'entertainment/center_detail.html', {'center': center, 'form': form})


# Добавление нового центра
def center_add(request):
    if request.method == "POST":
        form = EntertainmentCenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('center_list')  # Перенаправляем на страницу списка
    else:
        form = EntertainmentCenterForm()  # Создаем пустую форму
    return render(request, 'entertainment/center_form.html', {'form': form})

# Редактирование центра
def center_edit(request, pk):
    center = get_object_or_404(EntertainmentCenter, pk=pk)
    if request.method == "POST":
        form = EntertainmentCenterForm(request.POST, instance=center)
        if form.is_valid():
            form.save()
            return redirect('center_detail', pk=center.pk)  # Перенаправляем на страницу с деталями
    else:
        form = EntertainmentCenterForm(instance=center)  # Загружаем данные существующего центра в форму
    return render(request, 'entertainment/center_form.html', {'form': form})

def center_type_add(request):
    if request.method == "POST":
        form = CenterTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('center_list')  # После сохранения перенаправляем на список центров
    else:
        form = CenterTypeForm()
    return render(request, 'entertainment/center_type_form.html', {'form': form})


def center_list(request):
    centers = EntertainmentCenter.objects.all()  # Получаем все центры из базы данных
    return render(request, 'entertainment/center_list.html', {'centers': centers})


def center_edit(request, pk):
    center = get_object_or_404(EntertainmentCenter, pk=pk)  # Получаем центр по первичному ключу (pk)

    if request.method == "POST":
        form = EntertainmentCenterForm(request.POST, instance=center)  # Передаем объект для редактирования
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('center_detail',
                            pk=center.pk)  # Перенаправляем на страницу деталей отредактированного центра
    else:
        form = EntertainmentCenterForm(instance=center)  # Если GET-запрос, просто выводим форму с данными центра

    return render(request, 'entertainment/center_form.html', {'form': form})


# Функция для удаления центра
# views.py

def center_delete(request, pk):
    center = get_object_or_404(EntertainmentCenter, pk=pk)  # Отримуємо центр по pk

    if request.method == "POST":  # Якщо це POST запит (підтвердження видалення)
        center.delete()  # Видаляємо центр
        return redirect('center_list')  # Перенаправляємо на список центрів

    return render(request, 'entertainment/center_confirm_delete.html', {'center': center})


def event_list(request):
    events = Event.objects.all()  # або фільтрація за центром, якщо потрібно
    return render(request, 'entertainment/event_list.html', {'events': events})

# Додавання нової події
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Перенаправлення на сторінку зі списком подій
    else:
        form = EventForm()
    return render(request, 'entertainment/add_event.html', {'form': form})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'entertainment/event_detail.html', {'event': event})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Подію успішно видалено.')
        return redirect('event_list')
    return render(request, 'entertainment/event_confirm_delete.html', {'event': event})









