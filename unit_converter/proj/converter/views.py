from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def length(request):
    return render(request, 'length.html')

def length_out(request):
    return render(request, 'length_out.html')

def weight(request):
    return render(request, 'weight.html')

def weight_out(request):
    return render(request, 'weight_out.html')

def temp(request):
    return render(request, 'temp.html')

def temp_out(request):
    return render(request, 'temp_out.html')

# conversion factors to meters (base unit)
l_factors = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1,
    "kilometer": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34
}

def convert_L(request):
    converted_value = None
    error_msg = None

    if request.method == "POST":
        print("POST request received")  # debugging
        try:
            value = float(request.POST.get("length", "0")) #get input value
            from_unit = request.POST.get("from_unit")
            to_unit = request.POST.get("to_unit")
            print(f"Received values: {value}, {from_unit}, {to_unit}")  # debugging

            if from_unit in l_factors and to_unit in l_factors:
                meters_value = value * l_factors[from_unit]
                converted_value = meters_value / l_factors[to_unit]
            else:
                error_msg = "Invalid unit selection"
                print("Error: Invalid unit selection")  # debugging
                return render(request, 'index.html', {"error_msg":error_msg})

        except ValueError:
            error_msg = "Please enter a valid number"
            print("Error: ValueError - Invalid number input")  # debuging
            return render(request, 'index.html', {"error_msg":error_msg})
        
        if from_unit == "inch":
            from_unit = "inches"
        elif from_unit == "foot":
            from_unit = "feet"
        else:
            from_unit = from_unit + "s"
            
        if to_unit == "inch":
            to_unit = "inches"
        elif to_unit == "foot":
            to_unit = "feet"
        else:
            to_unit = to_unit + "s"

    print(f"Final values - Converted: {converted_value}, Error: {error_msg}")  # debugging
    return render(request, 'length_out.html', {"converted_value":converted_value, "error_msg":error_msg, "value":value, "from_unit":from_unit, "to_unit":to_unit})

# Conversion factors to grams (base unit)
w_factors = {
    "milligram": 0.001,
    "gram": 1,
    "kilogram": 1000,
    "ounce": 28.3495,
    "pound": 453.592
}

def convert_W(request):
    converted_value = None
    error_msg = None

    if request.method == "POST":
        try:
            value = float(request.POST.get("weight", "0"))  # Get input value
            from_unit = request.POST.get("from_unit")
            to_unit = request.POST.get("to_unit")

            # Check if units are valid
            if from_unit in w_factors and to_unit in w_factors:
                grams_value = value * w_factors[from_unit]  # Convert to grams
                converted_value = grams_value / w_factors[to_unit]  # Convert to target unit
            else:
                error_msg = "Invalid unit selection"
                return render(request, 'index.html', {"error_msg":error_msg})

        except ValueError:
            error_msg = "Please enter a valid number"
            return render(request, 'index.html', {"error_msg":error_msg})

    return render(request, 'weight_out.html', {"converted_value": converted_value, "error_msg": error_msg, "value":value, "from_unit":from_unit, "to_unit":to_unit})

def convert_T(request):
    converted_value = None
    error_msg = None

    if request.method == "POST":
        try:
            value = float(request.POST.get("temp", 0))  # Get the temperature value
            from_unit = request.POST.get("from_unit")
            to_unit = request.POST.get("to_unit")

            # Temperature conversion logic
            if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    converted_value = (value * 9/5) + 32
                elif to_unit == "Kelvin":
                    converted_value = value + 273.15
                else:
                    converted_value = value  # If same unit, return same value

            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    converted_value = (value - 32) * 5/9
                elif to_unit == "Kelvin":
                    converted_value = (value - 32) * 5/9 + 273.15
                else:
                    converted_value = value  

            elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    converted_value = value - 273.15
                elif to_unit == "Fahrenheit":
                    converted_value = (value - 273.15) * 9/5 + 32
                else:
                    converted_value = value  

            else:
                error_msg = "Invalid unit selection"
                return render(request, 'index.html', {"error_msg":error_msg})

        except ValueError:
            error_msg = "Please enter a valid number"
            return render(request, 'index.html', {"error_msg":error_msg})
        
        if from_unit == "Kelvin":
            from_unit = "K"
        elif from_unit == "Celsius":
            from_unit = "° Celsius"
        elif from_unit == "Fahrenheit":
            from_unit = "° Fahrenheit"

        if to_unit == "Kelvin":
            to_unit = "K"
        elif to_unit == "Celsius":
            to_unit = "° Celsius"
        elif to_unit == "Fahrenheit":
            to_unit = "° Fahrenheit"

    return render(request, 'temp_out.html', {"converted_value": converted_value, "error_msg": error_msg, "value": value, "from_unit":from_unit, "to_unit":to_unit})