from django.shortcuts import render, get_object_or_404, redirect
from .models import EntertainmentCenter
from .forms import EntertainmentCenterForm
from .models import CenterType
from .forms import CenterTypeForm



# Детали центра
def center_detail(request, pk):
    center = get_object_or_404(EntertainmentCenter, pk=pk)
    return render(request, 'entertainment/center_detail.html', {'center': center})

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

def add_center_type(request):
    if request.method == "POST":
        form = CenterTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_center_type')  # После добавления перенаправляем обратно
    else:
        form = CenterTypeForm()
    return render(request, 'entertainment/add_center_type.html', {'form': form})


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
def center_delete(request, pk):
    center = get_object_or_404(EntertainmentCenter, pk=pk)  # Получаем центр по первичному ключу (pk)

    if request.method == "POST":  # Если запрос POST, подтверждаем удаление
        center.delete()  # Удаляем объект
        return redirect('center_list')  # Перенаправляем на список центров

    return render(request, 'entertainment/center_confirm_delete.html',
                  {'center': center})  # Если GET-запрос, показываем страницу подтверждения удаления


