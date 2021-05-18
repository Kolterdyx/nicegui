# NiceGUI

<img src="https://raw.githubusercontent.com/zauberzeug/nicegui/main/sceenshots/ui-elements.png" width="300" align="right">

We like [Streamlit](https://streamlit.io/) but find it does to much magic when it comes to state handling. In search for an alernative nice library to write simple graphical user interfaces in Python we discovered [justpy](https://justpy.io/). While too "low-level-html" for our daily usage it provides a great basis for "NiceGUI".

## Purpose

NiceGUI is intended to be used for small scripts and user interfaces with a very limited user base. Custom "Smart-Home Control" solutions or "Robotics" for example. It's also helpful for development like tweaking/configuring a machine learning training or tuning motor controllers.

## Features

- browser-based GUI
- shared state between multiple browser windows
- implicit reload on code change
- clean set of GUI elements (label, button, checkbox, switch, slider, input, ...)
- simple grouping with rows, columns and cards
- genral-purpose html and markdown elements
- built-in timer to refresh data in intervals (even every 10 ms)
- straight-forward data bindings to write even less code

## Install

```bash
python3 -m pip install nicegui
```

## Usage

Write your nice GUI in a file `main.py`:

```python
from nicegui import ui

ui.label('Hello NiceGUI!')
ui.button('BUTTON', on_click=lambda: print('button was pressed'))
```

Launch it with:

```bash
python3 main.py
```

Note: The script will automatically reload the GUI if you modify your code.

### Styling & Design

NiceGUI use the [Quasar Framework](https://quasar.dev/) and hence has their full design power. Each NiceGUI element provides a `design` property which content is passed [as props the Quasar component](https://justpy.io/quasar_tutorial/introduction/#props-of-quasar-components):

<img src="https://raw.githubusercontent.com/zauberzeug/nicegui/main/sceenshots/demo-design.gif" width="200" align="right">

```python
ui.radio(['x', 'y', 'z'], design='inline color=green')
ui.button(icon='touch_app', design='outline round')
```

Have a look at [the Quasar documentation](https://quasar.dev/vue-components/button#design) for all styling "props".

## API

API Reference is hosted at [https://nicegui.io](https://nicegui.io). Also have a look at [examples.py](https://github.com/zauberzeug/nicegui/tree/main/examples.py) for an extensive demonstration what you can do with NiceGUI.

### Plots

<img src="https://raw.githubusercontent.com/zauberzeug/nicegui/main/sceenshots/demo-plot.png" width="300" align="right">
To render a simple plot you create a new context and call the neccessary [Matplotlib](https://matplotlib.org/) functions:

```python
from nicegui import ui
from matplotlib import pyplot as plt
import numpy as np

with ui.plot():
    x = np.linspace(0.0, 5.0)
    y = np.cos(2 * np.pi * x) * np.exp(-x)
    plt.plot(x, y, '-')
    plt.xlabel('time (s)')
    plt.ylabel('Damped oscillation')
```

To update a plot in regular intervals, have look at [main.py](https://github.com/zauberzeug/nicegui/tree/main/main.py).

<img src="https://raw.githubusercontent.com/zauberzeug/nicegui/main/sceenshots/demo-live-plot.gif" width="300" align="right">

To simplify live updating line plots even more, NiceGUI provides `ui.line_plot` with useful parameters and a `push` method:

```python
lines = ui.line_plot(n=2, limit=20).with_legend(['sin', 'cos'], loc='upper center', ncol=2)
ui.timer(0.1, lambda: lines.push([datetime.now()], [
    [np.sin(datetime.now().timestamp()) + 0.02 * np.random.randn()],
    [np.cos(datetime.now().timestamp()) + 0.02 * np.random.randn()],
]))
```
