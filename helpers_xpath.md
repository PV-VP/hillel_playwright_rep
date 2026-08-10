# Cheatsheet: XPath для Automation QA (з прикладами)

Цей шпаргалка містить основні та просунуті методи локалізації елементів за допомогою **XPath** для UI тестування.

---

## 1. Базовий пошук за тегом та атрибутом

Пошук елементів за їхніми стандартними HTML-атрибутами (`id`, `class`, `name`, `type`, `data-testid` тощо).

| Опис | Синтаксис XPath | Приклад HTML |
| :--- | :--- | :--- |
| **Точний атрибут** | `//tag[@attribute='value']` | `<input id="username">` <br>`//input[@id='username']` |
| **Будь-який тег з атрибутом** | `//*[@attribute='value']` | `<button data-testid="submit-btn">` <br>`//*[@data-testid='submit-btn']` |
| **Кілька атрибутів (AND)** | `//tag[@attr1='val1' and @attr2='val2']` | `<input type="text" name="email">` <br>`//input[@type='text' and @name='email']` |
| **Будь-який з атрибутів (OR)** | `//tag[@attr1='val1' or @attr2='val2']` | `<button type="submit" class="btn-primary">` <br>`//button[@type='submit' or @class='btn-primary']` |

---

## 2. Пошук за текстом (`text()` & `contains()`)

Пошук елементів за вмістом їхнього тексту або частковим співпадінням.

### 2.1. Точний текст: `text()`
* **Синтаксис:** `//tag[text()='Текст']`
* **Приклад:**
  ```html
  <button type="button">Save Changes</button>
  ```
  ```xpath
  //button[text()='Save Changes']
  ```

### 2.2. Частковий текст: `contains(text(), ...)`
* **Синтаксис:** `//tag[contains(text(), 'Частина')]`
* **Приклад:**
  ```html
  <p class="error-message">Error 404: Page not found</p>
  ```
  ```xpath
  //p[contains(text(), 'Error 404')]
  ```

### 2.3. Частковий атрибут: `contains(@attribute, ...)`
* **Синтаксис:** `//tag[contains(@attribute, 'значення')]`
* **Приклад:**
  ```html
  <div class="user-card active-status-v2">
  ```
  ```xpath
  //div[contains(@class, 'user-card')]
  ```

### 2.4. Початок значення: `starts-with()`
* **Синтаксис:** `//tag[starts-with(@attribute, 'початок')]`
* **Приклад (динамічні ID):**
  ```html
  <input id="button_129481249">
  ```
  ```xpath
  //input[starts-with(@id, 'button_')]
  ```

### 2.5. Нормалізація пробілів: `normalize-space()`
Очищає текст від зайвих пробілів та переносів рядків `
`.
* **Синтаксис:** `//tag[normalize-space(text())='Текст']`
* **Приклад:**
  ```html
  <button>
      Confirm Order  
  </button>
  ```
  ```xpath
  //button[normalize-space(text())='Confirm Order']
  ```

---

## 3. Навігація по родинних зв'язках (XPath Axes)

Осі XPath дозволяють переміщатися вгору, вниз або вбік по DOM-дереву відносно знайденого елемента.

```
       [ ancestor ]
            │
         [ parent ]
            │
     ┌──────┴──────┐
 [preceding-sibling]  [SELF]  [following-sibling]
     └──────┬──────┘
        [ child ]
            │
      [ descendant ]
```

### 3.1. `following-sibling` (Наступні сусідні елементи на тому ж рівні)
Знаходить елемент, який лежить **після** поточного елемента на одному рівні вкладеності.

* **Синтаксис:** `//початковий_елемент/following-sibling::цільовий_тег`
* **Приклад:** Знайти поле вводу біля мітки (label)
  ```html
  <div class="form-group">
    <label id="lbl-email">User Email</label>
    <input type="text" class="form-control">
  </div>
  ```
  ```xpath
  //label[@id='lbl-email']/following-sibling::input
  ```

### 3.2. `preceding-sibling` (Попередні сусідні елементи на тому ж рівні)
Знаходить елемент, який лежить **перед** поточним елементом на одному рівні вкладеності.

* **Синтаксис:** `//початковий_елемент/preceding-sibling::цільовий_тег`
* **Приклад:** Знайти чекбокс перед текстовою міткою
  ```html
  <input type="checkbox" id="chk-1">
  <label for="chk-1">Accept Terms & Conditions</label>
  ```
  ```xpath
  //label[contains(text(), 'Accept Terms')]/preceding-sibling::input[@type='checkbox']
  ```

### 3.3. `parent` або `..` (Батьківський елемент)
Піднімається на один рівень вгору.

* **Синтаксис:** `//початковий_елемент/parent::*` або `//початковий_елемент/..`
* **Приклад:** Знайти картку товару за кнопкою "Buy"
  ```html
  <div class="product-card">
    <h3>Phone</h3>
    <button>Buy</button>
  </div>
  ```
  ```xpath
  //button[text()='Buy']/..
  ```

### 3.4. `ancestor` (Всі батьківські/предківські елементи)
Піднімається на будь-який рівень вгору до конкретного предка.

* **Синтаксис:** `//початковий_елемент/ancestor::тег_предка`
* **Приклад:** Знайти формативний контейнер за полем вводу
  ```xpath
  //input[@name='card_number']/ancestor::form
  ```

### 3.5. `child` та `descendant` (Дочірні елементи)
* `child::` — тільки прямі діти (еквівалент `/`).
* `descendant::` — всі нащадки на будь-якій глибині (еквівалент `//`).

---

## 4. Індексація та предикати

| Синтаксис | Опис |
| :--- | :--- |
| `(//button)[1]` | Перша кнопка на всій сторінці |
| `(//button)[last()]` | Остання кнопка на сторінці |
| `(//button)[last()-1]` | Передостання кнопка на сторінці |
| `//ul/li[position() < 4]` | Перші 3 елементи списку `li` |

> **Порада:** Завжди беруть вираз у дужки перед вказуванням індексу, наприклад `(//div[@class='item'])[1]`, щоб індекс застосовувався до всієї колекції елементів на сторінці, а не до кожної окремої групи батьківських елементів.

---

## 5. Практичні патерни для QA Automation

### Таблиці (HTML Tables): Знайти осередку за текстом у сусідній колонці
```html
<tr>
  <td>John Doe</td>
  <td>john@example.com</td>
  <td><button class="delete-btn">Delete</button></td>
</tr>
```
* **Знайти кнопку Delete для користувача John Doe:**
  ```xpath
  //td[text()='John Doe']/following-sibling::td/button[@class='delete-btn']
  ```

### Форми: Знайти Input за текстом його Label
```html
<div class="field">
  <span>Phone Number</span>
  <div>
    <input type="tel">
  </div>
</div>
```
* **Пошук:**
  ```xpath
  //span[text()='Phone Number']/ancestor::div[@class='field']//input
  ```

---

## 6. Швидка шпаргалка за селекторами

| Задача | XPath селектор |
| :--- | :--- |
| Текст рівний | `//*[text()='Save']` |
| Частковий текст | `//*[contains(text(), 'Save')]` |
| Клас містить | `//*[contains(@class, 'btn')]` |
| Наступний сусід | `//label/following-sibling::input` |
| Попередній сусід | `//input/preceding-sibling::label` |
| Батьківський елемент | `//input/..` |
| Предок за тегом | `//input/ancestor::form` |