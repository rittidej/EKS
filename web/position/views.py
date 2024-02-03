from django.shortcuts import render, redirect, get_object_or_404
from .forms import PositionForm
from .models import Position
from django.contrib import messages


# Create your views here.
def index(request):
    positions = Position.objects.all()
    
    context = {
    
        'x': positions,
    }
    return render(request, 'position/index.html', context)

def create(request):
    form = PositionForm()
    context = {
        'form': form,
    }    
    return render(request, 'position/create.html', context)

def store(request):
    if request.method == 'POST':
        try:
            form = PositionForm(request.POST or None)
            context = {
                'form': form,
            }
            if form.is_valid():
                form.save()
                messages.success(request, "บันทึกข้อมูลแล้ว")
            else:
                messages.error(request, form.errors)
                return render(request, 'position/create.html', context)
        except:
            messages.error(request, "บันทึกข้อมูลไม่สำเร็จ")
            
    return redirect('position:index')

def delete(request, id):
    if request.method == 'POST':
        try:
            position = get_object_or_404(Position, id=id)
            position.delete()
            messages.success(request, "ลบสำเร็จ")
        except:
            messages.error(request, "ลบไม่สำเร็จ")

    return redirect('position:index')

def edit(request, id):
    position = get_object_or_404(Position, id=id)
    form = PositionForm(instance=position)
    context = {
        'form': form,
        'position': position,
    }
    return render(request, 'position/edit.html', context)

def update(request, id):
    if request.method == 'POST':
        try:
            position = get_object_or_404(Position, id=id)
            form = PositionForm(request.POST or None, instance=position)
            context = {
                'form': form,
                'position': position
            }
            if form.is_valid():
                form.save()
                messages.success(request, "แก้ไขสำเร็จแล้ว")
            else:
                messages.error(request, form.errors)
        except:
            messages.error(request, "แก้ไขไม่สำเร็จแล้ว")
        return redirect('position:edit', id)

    return redirect('position:index')