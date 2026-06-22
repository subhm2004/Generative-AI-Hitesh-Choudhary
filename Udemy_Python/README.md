# 🐍 Complete Python Mastery — Udemy Course Notes & Projects

> **Course by [Hitesh Choudhary](https://www.youtube.com/@HiteshChoudharydotcom)** | Beginner to Advanced Python with hands-on projects and real-world challenges.

This repository contains well-documented Python code, notes (in Hinglish 🇮🇳), and practical projects covering everything from basic data types to async programming, OOP, Pydantic, and full-stack mini-projects.

Every file is richly commented — making it easy to learn, revise, and reference later.

---

## 📑 Table of Contents (Index)

| #  | Module | Topic | Files |
|----|--------|-------|-------|
| 00 | [Introduction to Python](#00--introduction-to-python) | What is a function? Pseudo-code | 2 |
| 01 | [Virtual Environments](#01--virtual-environments) | venv setup, pip, requirements.txt | 3 |
| 02 | [Data Types](#02--data-types) | Variables, int, float, bool, str, list, tuple, set, dict, and more | 12 |
| 03 | [Conditionals](#03--conditionals) | if-else, nested conditions, real-world examples | 6 |
| 04 | [Loops](#04--loops) | for, while, walrus operator, for-else, dictionary switch-case | 12 |
| 05 | [Functions](#05--functions) | Scopes, closures, params, return, built-in functions | 12 |
| 06 | [Modules & Packages (Chai Business)](#06--modules--packages-chai-business) | Imports, packages, `__init__.py`, project structure | 4 |
| 07 | [Comprehensions](#07--comprehensions) | List, set, dict, generator comprehensions | 4 |
| 08 | [Generators](#08--generators) | yield, infinite generators, send(), close() | 4 |
| 09 | [Decorators](#09--decorators) | Basics, logging decorator, auth decorator | 3 |
| 10 | [OOP (Object-Oriented Programming)](#10--oop-object-oriented-programming) | Classes, inheritance, MRO, static/class methods, property decorators | 11 |
| 11 | [Exception Handling](#11--exception-handling) | try-except, custom exceptions, file handling | 9 |
| 12 | [Threads & Concurrency](#12--threads--concurrency) | Threading, multiprocessing, GIL, locks, queues | 12 |
| 13 | [Async Python](#13--async-python) | async/await, daemon threads, race conditions, deadlocks | 10 |
| 14 | [Pydantic](#14--pydantic) | Models, validation, nested models, serialization | 11 |
| — | [Challenges (Mini Projects)](#-challenges--mini-projects) | 6 challenge tracks with 50+ hands-on exercises | 50+ |

---

## 📂 Detailed Module Breakdown

### 00 — Introduction to Python

> 🧠 *Python kya hai? Function kya hota hai? Pseudo-code se samjho.*

| File | Description |
|------|-------------|
| `non_python_code.py` | Pseudo-code: chai banane ka process as functions |
| `non_python_shop.py` | Pseudo-code: chai shop operations |

**Key Concepts:** Functions as reusable blocks, calling a function, code structure.

---

### 01 — Virtual Environments

> 🧠 *Python projects ke liye isolated environments banana aur manage karna.*

| File | Description |
|------|-------------|
| `virtual_environment.txt` | Step-by-step venv commands (create, activate, deactivate, delete) |
| `requirements.txt` | External dependencies list |
| `test.py` | Testing virtual environment setup |

**Key Concepts:** `python3 -m venv`, `source venv/bin/activate`, `pip install -r requirements.txt`, `pip freeze`.

---

### 02 — Data Types

> 🧠 *Python ke saare important data types — immutable vs mutable, memory model, aur operations.*

| File | Topic |
|------|-------|
| `chapter_1.py` | Variables, Memory (`id()`), Immutability |
| `chapter_2.py` | Set — Mutable data type (add, remove) |
| `chapter_3.py` | Integer — Math operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`) |
| `chapter_4.py` | Boolean — `True`/`False`, `and`, `or`, `not` operators |
| `chapter_5.py` | Float — Precision issues, `Decimal` module |
| `chapter_6.py` | Strings — Slicing, f-strings, encoding/decoding (UTF-8) |
| `chapter_7.py` | Tuple — Immutable collection, unpacking, swap trick |
| `chapter_8.py` | List — Mutable collection, methods (`append`, `pop`, `sort`, etc.) |
| `chapter_9.py` | Set (Advanced) — Union, intersection, difference operations |
| `chapter_10.py` | Dictionary — Key-value pairs, methods, iteration |
| `chapter_11.py` | Advanced Types — `arrow` (datetime), `namedtuple` |
| `input.py` | User input handling |

**Key Concepts:** Mutable vs Immutable, `id()`, memory references, type conversions, operator overloading.

---

### 03 — Conditionals

> 🧠 *Decision making in Python — if, elif, else, aur real-world scenarios.*

| File | Topic |
|------|-------|
| `chai_price_calculator.py` | Chai price calculation with conditional logic |
| `delivery_fees_waiver.py` | Delivery fee waiver based on order amount |
| `mini_story_1.py` | Interactive mini story with branching paths |
| `smart_thermostat.py` | Smart thermostat simulation |
| `snak_suggestion.py` | Snack suggestion engine |
| `train_seat.py` | Train seat availability checker |

**Key Concepts:** `if-elif-else`, nested conditions, comparison operators, truthy/falsy values.

---

### 04 — Loops

> 🧠 *Repetition in Python — for loops, while loops, aur advanced patterns.*

| File | Topic |
|------|-------|
| `01_token_dispneser.py` | Token dispenser simulation |
| `02_batch_chai.py` | Batch chai preparation |
| `03_tea_orders.py` | Processing tea orders |
| `04_tea_menu.py` | Tea menu display |
| `05_order_summary.py` | Order summary generation |
| `06_tea-temperature.py` | Tea temperature monitoring |
| `07_put_of_order.py` | Out-of-order detection |
| `08_for_else.py` | `for-else` construct |
| `09_walrus.py` | Walrus operator (`:=`) |
| `10_dictionary_case.py` | Dictionary as switch-case |
| `11_table_of_a_number.py` | Multiplication table generator |
| `12_while_loop.py` | While loop patterns |

**Key Concepts:** `for` loop, `while` loop, `break`, `continue`, `for-else`, walrus operator (`:=`), `enumerate()`, `range()`.

---

### 05 — Functions

> 🧠 *Functions ka deep dive — scopes, closures, parameter types, aur built-in functions.*

| File | Topic |
|------|-------|
| `01_duplication.py` | Why functions? — Code duplication problem |
| `02_complex.py` | Complex function examples |
| `03_hiding.py` | Information hiding with functions |
| `04_readability.py` | Code readability improvements |
| `05_trace.py` | Tracing function execution |
| `06_scopes.py` | Variable scopes (LEGB rule) |
| `07_nonlocal.py` | `nonlocal` keyword |
| `08_global_scope.py` | `global` keyword |
| `09_input_params.py` | `*args`, `**kwargs`, default parameters |
| `10_return.py` | Return values, multiple returns |
| `11_types_of_functions.py` | Lambda, map, filter, reduce |
| `12_built_in.py` | Python built-in functions |

**Key Concepts:** LEGB scope rule, closures, `*args` & `**kwargs`, lambda functions, `map()`, `filter()`, `reduce()`.

---

### 06 — Modules & Packages (Chai Business)

> 🧠 *Real project structure — modules, packages, aur imports ke 3 methods.*

```
06_chai_business/
├── main.py              # Entry point — 3 import methods demo
├── recipes/
│   ├── __init__.py      # Package initializer
│   └── flavors.py       # Chai flavors module
└── utils/
    └── discounts.py     # Discount utilities
```

**Key Concepts:** `import module`, `from package import module`, `from module import function`, `__init__.py`, package structure.

---

### 07 — Comprehensions

> 🧠 *Pythonic shorthand — ek line mein list, set, dict, generator banao.*

| File | Topic |
|------|-------|
| `01_list_compre.py` | List comprehension — `[x for x in iterable]` |
| `02_set_compre.py` | Set comprehension — `{x for x in iterable}` |
| `03_dict_compre.py` | Dictionary comprehension — `{k: v for k, v in ...}` |
| `04_genrator_compre.py` | Generator expression — `(x for x in iterable)` |

**Key Concepts:** Comprehension syntax, filtering with `if`, nested comprehensions, memory efficiency of generators.

---

### 08 — Generators

> 🧠 *Lazy evaluation — `yield` keyword, infinite sequences, aur generator protocol.*

| File | Topic |
|------|-------|
| `01_basics.py` | Generator basics, `yield` vs `return` |
| `02_infinite_generators.py` | Infinite number generators |
| `03_send_generators.py` | `generator.send()` method |
| `04_close_generator.py` | `generator.close()` & `GeneratorExit` |

**Key Concepts:** `yield`, `next()`, lazy evaluation, `send()`, `close()`, `StopIteration`, memory-efficient iteration.

---

### 09 — Decorators

> 🧠 *Functions ko modify/extend karna bina code change kiye — `@decorator` syntax.*

| File | Topic |
|------|-------|
| `01_basics.py` | Decorator fundamentals, `@wrapper` pattern |
| `02_logging_decorator.py` | Logging decorator — function calls track karo |
| `03_auth_decorator.py` | Authentication decorator — access control |

**Key Concepts:** Higher-order functions, `@decorator` syntax, `functools.wraps`, practical use-cases (logging, auth).

---

### 10 — OOP (Object-Oriented Programming)

> 🧠 *Classes, objects, inheritance, aur advanced OOP patterns.*

| File | Topic |
|------|-------|
| `01_simple_class.py` | Class basics — `class`, attributes |
| `02_namespace.py` | Namespaces in classes |
| `03_attribute_shadowing.py` | Attribute shadowing & resolution |
| `04_self_args.py` | `self` parameter explained |
| `05_init_objects.py` | `__init__` constructor |
| `06_inheritance_composition.py` | Inheritance vs Composition |
| `07_base_class.py` | Base class & `super()` |
| `08_mro.py` | Method Resolution Order (MRO) |
| `09_static_methods.py` | `@staticmethod` |
| `10_classmethod.py` | `@classmethod` & alternative constructors |
| `11_propert_decorators.py` | `@property` — getters, setters, deleters |

**Key Concepts:** Encapsulation, inheritance, polymorphism, MRO (C3 linearization), `@staticmethod`, `@classmethod`, `@property`.

---

### 11 — Exception Handling

> 🧠 *Errors gracefully handle karna — try-except aur custom exceptions.*

| File | Topic |
|------|-------|
| `01_basic.py` | Exception basics |
| `02_try_except.py` | `try-except` block |
| `03_complex_try.py` | Complex try-except patterns |
| `04_multiple_exception.py` | Multiple exception types handling |
| `05_custom_exceptions.py` | Creating custom exception classes |
| `06_custom_except_two.py` | Advanced custom exceptions |
| `07_complete_order.py` | Complete order processing with error handling |
| `08_file_handling.py` | File I/O with exception safety |
| `order.txt` | Sample data file for file handling exercises |

**Key Concepts:** `try`, `except`, `else`, `finally`, custom exceptions with `raise`, `with` statement, file handling.

---

### 12 — Threads & Concurrency

> 🧠 *Parallel execution — threading, multiprocessing, GIL, locks, aur shared memory.*

| File | Topic |
|------|-------|
| `01_threading.py` | Threading basics |
| `02_multiprocessing.py` | Multiprocessing basics |
| `03_gil_threading.py` | GIL impact on threading |
| `04_gil_multiprocessing.py` | GIL bypass with multiprocessing |
| `05_thread_one.py` | Thread creation & management |
| `06_thread_two.py` | Multiple threads |
| `07_thread_download.py` | Threaded file downloads |
| `08_thread_lock.py` | Thread locks — race condition prevention |
| `09_process_one.py` | Process creation |
| `10_process_two.py` | Multiple processes |
| `11_process_queue.py` | Inter-process communication with Queue |
| `12_process_value.py` | Shared memory with Value/Array |

**Key Concepts:** `threading.Thread`, `multiprocessing.Process`, GIL (Global Interpreter Lock), `Lock`, `Queue`, `Value`, I/O-bound vs CPU-bound tasks.

---

### 13 — Async Python

> 🧠 *Asynchronous programming — async/await, event loops, daemons, aur pitfalls.*

| File | Topic |
|------|-------|
| `01_async_one.py` | `async`/`await` basics |
| `02_async_two.py` | Multiple coroutines |
| `03_async_three.py` | `asyncio.gather()` for concurrent tasks |
| `04_thread_async.py` | Mixing threads with async |
| `05_process_async.py` | Mixing processes with async |
| `06_bgworker.py` | Background worker pattern |
| `07_daemon.py` | Daemon threads |
| `08_non_daemon.py` | Non-daemon threads |
| `09_race_condition.py` | Race condition demonstration |
| `10_deadlock.py` | Deadlock scenario & prevention |

**Key Concepts:** `asyncio`, `async def`, `await`, `asyncio.gather()`, event loop, daemon vs non-daemon threads, race conditions, deadlocks.

---

### 14 — Pydantic

> 🧠 *Data validation library — type-safe models, validators, aur serialization.*

#### 📁 `01_basics/`

| File | Topic |
|------|-------|
| `first_model.py` | First Pydantic model |
| `product_model.py` | Product data model |
| `employee_model.py` | Employee model with validation |
| `field_example.py` | `Field()` options (alias, default, etc.) |
| `field_validation.py` | Field-level validation |
| `nested_model.py` | Nested models (model inside model) |
| `advance_nested_model.py` | Advanced nesting patterns |
| `advance_validators.py` | `@field_validator`, `@model_validator` |
| `computed_property.py` | `@computed_field` — auto-calculated fields |
| `self_reference.py` | Self-referencing models (tree structures) |

#### 📁 `02_serialization/`

| File | Topic |
|------|-------|
| `serial.py` | `.model_dump()`, `.model_dump_json()`, serialization aliases |

**Key Concepts:** `BaseModel`, type coercion, `Field()`, validators, nested models, computed fields, JSON serialization/deserialization.

---

## 🏆 Challenges — Mini Projects

> Real-world hands-on projects to practice Python skills.

### Challenge 01 — Utilities (11 Days)

> File operations, text processing, system utilities.

| File | Topics Covered |
|------|---------------|
| `day_1.py` – `day_11.py` | File I/O, string manipulation, CLI tools, text analysis |
| `hitesh_bio.txt`, `learning_journal.txt`, `tasks.txt` | Sample data files |

---

### Challenge 02 — Data Handling (10 Days)

> CSV, JSON, encryption, data transformation.

| File | Topics Covered |
|------|---------------|
| `day_1.py` – `day_10.py` | CSV/JSON parsing, data conversion, vault encryption |
| `contacts.csv`, `movies.json`, `api_data.json` | Sample datasets |
| `vault.key`, `vault.txt` | Encrypted vault exercise files |
| `requirements.txt` | Dependencies for data handling |

---

### Challenge 03 — Web Scraping (10 Days)

> BeautifulSoup, requests, PDF generation, database storage.

| File | Topics Covered |
|------|---------------|
| `day_01.py` – `day_10.py` | HTML scraping, API calls, image downloads, CSV export |
| `books_data.json`, `crypto_prices.csv` | Scraped data |
| `crypto.db` | SQLite database |
| `hn_top20.csv` | Hacker News top 20 stories |

---

### Challenge 04 — Automation (4 Days)

> Task automation, image processing, file management.

| File | Topics Covered |
|------|---------------|
| `day_01.py` – `day_04.py` | File automation, image processing, batch operations |
| `trip_1.jpg`, `trip_2.jpg`, `trip_3.jpg` | Sample images |

---

### Challenge 05 — Data Science (10 Days)

> Pandas, NumPy, data analysis, visualization.

| File | Topics Covered |
|------|---------------|
| `day_01.ipynb` | Jupyter Notebook — data exploration |
| `day_02.py` – `day_10.py` | Pandas, data cleaning, analysis, plotting |
| `books.csv`, `experience_salary.csv`, `youtube_comments.csv` | Analysis datasets |

---

### Challenge 06 — URL Shortener (Full-Stack Project) 🌐

> Complete Flask web application — bit.ly clone!

```
06_url_shortner/
├── app.py               # Flask app — routes, URL shortening logic
├── models.py            # SQLite database operations (CRUD)
├── database.db          # SQLite database
├── requirements.txt     # Flask & dependencies
└── templates/           # HTML templates (Jinja2)
```

**Features:** Shorten URLs, redirect via short code, visit counter, delete links, 404 page.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed on your system
- **pip** package manager

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/subhm2004/Generative-AI-Hitesh-Choudhary.git
cd Generative-AI-Hitesh-Choudhary/Udemy_Python

# 2. Create a virtual environment
python3 -m venv venv

# 3. Activate the virtual environment
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# 4. Install dependencies (for specific modules)
pip install -r 01_virtual/requirements.txt           # Core dependencies
pip install -r challenges/02_data_handling/requirements.txt  # Data handling
pip install -r challenges/06_url_shortner/requirements.txt   # URL Shortener
```

### Running Any File

```bash
# Run any Python file directly
python3 02_datatypes/chapter_1.py

# Run the URL Shortener web app
cd challenges/06_url_shortner
python3 app.py
# Open http://localhost:8000 in browser
```

---

## 🛠️ Tech Stack

| Technology | Usage |
|-----------|-------|
| 🐍 Python 3 | Core language |
| 📦 Pydantic | Data validation & serialization |
| 🌐 Flask | Web framework (URL Shortener) |
| 🗄️ SQLite | Database |
| 🐼 Pandas / NumPy | Data science challenges |
| 🌿 BeautifulSoup | Web scraping |
| 🔐 Cryptography | Vault encryption challenge |
| 🧵 Threading / Multiprocessing | Concurrency modules |
| ⚡ Asyncio | Async programming |

---

## 📁 Repository Structure

```
Udemy_Python/
│
├── 00_python/               # Introduction & pseudo-code
├── 01_virtual/              # Virtual environment setup
├── 02_datatypes/            # All Python data types (12 chapters)
├── 03_conditionals/         # Conditional logic & decision making
├── 04_loops/                # For, while, walrus, for-else
├── 05_functions/            # Functions deep dive (12 files)
├── 06_chai_business/        # Modules & packages (project)
├── 07_comprehensions/       # List, set, dict, generator
├── 08_generators/           # Yield, infinite, send, close
├── 09_decorators/           # Basics, logging, auth
├── 10_oops/                 # OOP — classes to property decorators
├── 11_exceptions/           # Exception handling & file I/O
├── 12_threads_concurrency/  # Threading & multiprocessing
├── 13_async_python/         # Async/await & concurrency pitfalls
├── 14_pydantic/             # Pydantic models & serialization
├── challenges/              # 6 mini-project tracks (50+ files)
│   ├── 01_utilities/
│   ├── 02_data_handling/
│   ├── 03_web_scraping/
│   ├── 04_automation/
│   ├── 05_data_science/
│   └── 06_url_shortner/     # Full-stack Flask app
│
├── .gitignore
└── README.md                # 📍 You are here!
```

---

## 📝 Notes

- All code comments are in **Hinglish** (Hindi + English) for easy understanding 🇮🇳
- Each file starts with a **header block** explaining the topic, file name, and folder
- The code follows a **progressive learning path** — start from `00_python` and move sequentially
- **Challenges** are independent mini-projects — pick any that interests you!

---

## 🙏 Credits

- **Instructor:** [Hitesh Choudhary](https://www.youtube.com/@HiteshChoudharydotcom) — Udemy Course
- **Student:** Shubham — Code, notes, and documentation

---

<p align="center">
  <b>⭐ If this repo helped you learn Python, give it a star!</b><br>
  <i>Happy Coding! 🚀</i>
</p>
