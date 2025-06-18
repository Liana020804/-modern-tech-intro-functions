import streamlit as st
from reveal_slides import slides

# Конфигурация презентации
slides_config = {
    "height": 700,
    "margin": 0.1,
    "transition": "slide",
    "controls": True,
    "progress": True,
    "slideNumber": "c/t",
    "width": "90%"
}

# Содержание презентации
slides_content = """
<!-- Слайд 1: Титульный -->
<section data-background="#2d3436">
<h1 style="color:white; font-size: 3em;">Паттерн Abstract Factory</h1>
<h3 style="color:#fdcb6e">Порождающий паттерн проектирования</h3>
<p style="color:#dfe6e9">Создание семейств связанных объектов</p>
</section>

<!-- Слайд 2: Определение -->
<section>
<h2>📌 Определение</h2>
<blockquote style="background:#f8f9fa;padding:20px;border-radius:5px;color:#2d3436;">
Abstract Factory предоставляет интерфейс для создания семейств связанных или зависимых объектов без указания их конкретных классов.
</blockquote>
<div style="margin-top:30px;">
<h4>Основные характеристики:</h4>
<ul>
<li>Инкапсулирует процесс создания объектов</li>
<li>Гарантирует совместимость создаваемых продуктов</li>
<li>Позволяет легко заменять целые семейства продуктов</li>
</ul>
</div>
</section>

<!-- Слайд 3: Проблема -->
<section>
<h2>💡 Какие проблемы решает?</h2>
<div>
<pre><code class="python" style="font-size:1.2em;background:#f8f9fa;color:#2d3436;padding:15px;border-radius:5px;"># Проблемный код
button = WindowsButton()
checkbox = MacCheckbox()  # Несовместимые компоненты!</code></pre>
</div>
<div style="margin-top:30px;">
<h4>Типичные проблемы:</h4>
<ul>
<li>Жесткая привязка к конкретным классам</li>
<li>Нарушение принципа открытости/закрытости</li>
<li>Сложность поддержки кода</li>
</ul>
</div>
</section>

<!-- Слайд 4: Диаграмма -->
<section>
<h2>📊 Структура паттерна</h2>
<pre style="background:#f8f9fa;padding:20px;border-radius:5px;"><code style="color:#2d3436;">
AbstractFactory
├── create_product_a() → AbstractProductA
└── create_product_b() → AbstractProductB

ConcreteFactory1 (наследует AbstractFactory)
├── create_product_a() → ProductA1
└── create_product_b() → ProductB1

ConcreteFactory2 (наследует AbstractFactory)
├── create_product_a() → ProductA2
└── create_product_b() → ProductB2
</code></pre>
</section>

<!-- Слайд 5: Пример из реального мира -->
<section>
<h2>🌍 Пример из реального мира</h2>
<div style="display:flex;justify-content:space-around;margin-top:50px;">
<div style="background:#f8f9fa;padding:20px;border-radius:10px;width:45%;color:#2d3436;">
<h3 style= "color:#2d3436;">🔧 Автозапчасти</h3>
<ul style= "color:#2d3436;">
<li>Двигатель BMW</li>
<li>Коробка передач BMW</li>
<li>Тормоза BMW</li>
</ul>
</div>
<div style="background:#f8f9fa;padding:20px;border-radius:10px;width:45%;color:#2d3436;">
<h3 style= "color:#2d3436;">🔩 Другая фабрика</h3>
<ul style= "color:#2d3436;">
<li>Двигатель Audi</li>
<li>Коробка передач Audi</li>
<li>Тормоза Audi</li>
</ul>
</div>
</div>
</section>

<!-- Слайд 6: Пример кода -->
<section>
<h2>💻 Пример реализации на Python</h2>
<div>
<h4>Абстрактная фабрика:</h4>
<pre><code class="python" style="font-size:0.9em;background:#f8f9fa;padding:15px;border-radius:5px;">from abc import ABC, abstractmethod

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self): pass
    
    @abstractmethod
    def create_checkbox(self): pass</code></pre>
</div>
<div>
<h4>Конкретная фабрика:</h4>
<pre><code class="python" style="font-size:0.9em;background:#f8f9fa;padding:15px;border-radius:5px;">class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
        
    def create_checkbox(self):
        return WindowsCheckbox()</code></pre>
</div>
</section>

<!-- Слайд 7: Клиентский код -->
<section>
<h2>👨‍💻 Клиентский код</h2>
<pre><code class="python" style="font-size:1em;background:#f8f9fa;color:#2d3436;padding:15px;border-radius:5px;">def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    
    button.render()
    checkbox.render()

# Использование
if os.name == "nt":
    factory = WindowsFactory()
else:
    factory = MacFactory()
    
client_code(factory)</code></pre>
<div style="margin-top:20px;">
✅ Клиент работает только с интерфейсами<br>
✅ Легко добавить новую фабрику (LinuxFactory)
</div>
</section>

<!-- Слайд 8: Преимущества -->
<section>
<h2>✅ Преимущества</h2>
<ul style="font-size:1.2em;">
<li class="fragment">Изолирует конкретные классы</li>
<li class="fragment">Упрощает замену семейств продуктов</li>
<li class="fragment">Гарантирует совместимость продуктов</li>
<li class="fragment">Соответствует принципам SOLID</li>
</ul>
</section>

<!-- Слайд 9: Недостатки -->
<section>
<h2>❌ Недостатки</h2>
<ul style="font-size:1.2em;">
<li class="fragment">Усложняет код (много классов)</li>
<li class="fragment">Требует создания новой фабрики для каждого семейства</li>
<li class="fragment">Может быть избыточным для простых случаев</li>
</ul>
</section>

<!-- Слайд 10: Заключение -->
<section data-background="#2d3436">
<h2 style="color:white">📝 Когда использовать?</h2>
<ul style="color:white;font-size:1.3em;">
<li>Система не должна зависеть от способа создания объектов</li>
<li>Нужно создавать семейства связанных объектов</li>
<li>Важна совместимость компонентов</li>
</ul>
<div style="margin-top:100px;">
<h3 style="color:#fdcb6e">Спасибо за внимание!</h3>
</div>
</section>
"""

# Создаем презентацию
def main():
    st.set_page_config(page_title="Abstract Factory Pattern", layout="wide")
    slides (content=slides_content, config=slides_config, allow_unsafe_html=True)

if __name__ == "__main__":
    main()