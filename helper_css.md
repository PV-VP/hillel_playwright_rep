
# Cheatsheet: CSS Selectors для Automation QA (з прикладами)

Ця шпаргалка містить основні та просунуті методи локалізації елементів за допомогою **CSS-селекторів** для UI тестування.

---

## 1. Базовий пошук за тегом, ID, класом та атрибутами

Пошук елементів за основними атрибутами HTML.

| Опис | Синтаксис CSS | Приклад HTML |
| :--- | :--- | :--- |
| **За ID (`#`)** | `#username` | `<input id="username">` |
| **За класом (`.`)** | `.btn-primary` | `<button class="btn btn-primary">` |
| **Декілька класів (AND)** | `.btn.btn-primary.active` | `<button class="btn btn-primary active">` |
| **За точним атрибутом** | `input[name='email']` | `<input type="text" name="email">` |
| **Кілька атрибутів (AND)** | `input[type='text'][name='email']` | `<input type="text" name="email">` |
| **За наявністю атрибута** | `input[required]` | `<input type="text" required>` |

---

## 2. Робота зі значеннями атрибутів (`*=`, `^=`, `$=`)

Оскільки класичний CSS не підтримує пошук за текстом як XPath, робота з частковим співпадінням атрибутів є ключовою.

### 2.1. Часткове співпадіння (Містить): `*=`
Аналог `contains(@attr, 'val')` в XPath.
* **Синтаксис:** `tag[attribute*='value']`
* **Приклад:**
  ```html
  <div class="user-card active-status-v2">
  ```
  ```css
  div[class*='user-card']
  ```

### 2.2. Початок значення: `^=`
Аналог `starts-with(@attr, 'val')` в XPath. Зручно для динамічних ID.
* **Синтаксис:** `tag[attribute^='value']`
* **Приклад:**
  ```html
  <input id="button_129481249">
  ```
  ```css
  input[id^='button_']
  ```

### 2.3. Закінчення значення: `$=`
Шукає значення, що закінчується на вказаний рядок.
* **Синтаксис:** `tag[attribute$='value']`
* **Приклад:**
  ```html
  <img src="assets/images/avatar_user12.png">
  ```
  ```css
  img[src$='.png']
  ```

### 2.4. Окреме слово у списку: `~=`
Шукає ціле слово серед розділених пробілами значень (наприклад, для класів).
* **Синтаксис:** `tag[attribute~='value']`
* **Приклад:** `[class~='btn']` знайде `class="btn active"`, але не `class="btn-primary"`.

---

## 3. Навігація по родинних зв'язках (Combinators)

На відміну від XPath, CSS рухається переважно **згори донизу** та **вперед**.

```
       [ Parent / Ancestor ]
                 │
      ┌──────────┴──────────┐
  [ Direct Child > ]   [ Descendant (space) ]
                 │
 ┌───────────────┴───────────────┐
 [ Current Element ] ──(+)──> [ Immediate Sibling ]
                     ──(~)──> [ General Sibling ]
```

### 3.1. Прямий дочірній елемент (`>`)
Знаходить тільки безпосередніх дітей (еквівалент `/` в XPath).
* **Синтаксис:** `parent > child`
* **Приклад:**
  ```html
  <ul class="menu">
    <li><a href="#">Home</a></li>
  </ul>
  ```
  ```css
  ul.menu > li
  ```

### 3.2. Будь-який нащадок (Пробіл ` `)
Знаходить елемент на будь-якому рівні вкладеності (еквівалент `//` в XPath).
* **Синтаксис:** `ancestor descendant`
* **Приклад:**
  ```html
  <form id="login-form">
    <div>
      <input type="text">
    </div>
  </form>
  ```
  ```css
  form#login-form input
  ```

### 3.3. Перший наступний сусід (`+`)
Знаходить один елемент, що йде **одразу за** поточним на тому ж рівні.
* **Синтаксис:** `element + sibling`
* **Приклад:** Знайти input одразу за label
  ```html
  <label id="email-lbl">Email</label>
  <input type="email">
  ```
  ```css
  label#email-lbl + input
  ```

### 3.4. Усі наступні сусіди (`~`)
Знаходить **усі** вказані елементи далі на тому ж рівні (еквівалент `following-sibling::` в XPath).
* **Синтаксис:** `element ~ sibling`
* **Приклад:**
  ```html
  <h2>Header</h2>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
  ```
  ```css
  h2 ~ p
  ```

---

## 4. Псевдокласи та індексація (Pseudos)

| Селектор | Опис | Приклад |
| :--- | :--- | :--- |
| `:first-child` | Перший дочірній елемент у своєму контейнері | `ul > li:first-child` |
| `:last-child` | Останній дочірній елемент | `ul > li:last-child` |
| `:nth-child(n)` | Елемент за порядковим номером (1-based) | `ul > li:nth-child(3)` |
| `:nth-child(even)` | Усі парні елементи списку | `tr:nth-child(even)` |
| `:nth-child(odd)` | Усі непарні елементи списку | `tr:nth-child(odd)` |
| `:not(selector)` | Інверсія / заперечення селектора | `input:not([disabled])` |

---

## 5. Просунутий CSS: Псевдоклас `:has()` (Батьківський селектор)

Підтримується в сучасних браузерах, Playwright та Selenium 4+. Дозволяє вибирати батьківський елемент за вмістом або дочірніми елементами.

### 5.1. Батьківський елемент за наявністю дочірнього
* **Задача:** Знайти `.product-card`, всередині якого є кнопка із класом `.buy-btn`.
* **CSS:**
  ```css
  .product-card:has(.buy-btn)
  ```

### 5.2. Батьківський елемент за відношенням до сусіда
* **Задача:** Знайти `label`, за яким одразу йде чекбокс `:checked`.
* **CSS:**
  ```css
  label:has(+ input[type='checkbox']:checked)
  ```

---

## 6. Швидка порівняльна шпаргалка (CSS vs XPath)

| Задача | CSS Селектор | Еквівалент XPath |
| :--- | :--- | :--- |
| **Елемент за ID** | `#username` | `//*[@id='username']` |
| **Елемент за класом** | `.btn-primary` | `//*[contains(@class, 'btn-primary')]` |
| **Прямий дитина** | `ul > li` | `//ul/li` |
| **Будь-який нащадок** | `form input` | `//form//input` |
| **Наступний сусід** | `label + input` | `//label/following-sibling::input[1]` |
| **Усі наступні сусіди** | `h2 ~ p` | `//h2/following-sibling::p` |
| **Частковий атрибут** | `[id*='btn']` | `//*[contains(@id, 'btn')]` |
| **Початок атрибута** | `[id^='btn']` | `//*[starts-with(@id, 'btn')]` |
| **Перший елемент** | `li:first-child` | `(//li)[1]` |