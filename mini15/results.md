# Результы измерений

## Игра "Жизнь"

| Bench                | Result             |
| -------------------- | ------------------ |
| Python               | 86.52161645889282  |
| NumPy (tuple index)  | 167.2669472694397  |
| NumPy (double index) | 191.10436153411865 |

## Приведение типов при работе с массивами NumPy

| Bench               | Result            |
| ------------------- | ----------------- |
| NumPy fallback      | 5.60130763053894  |
| Explicit typecast   | 6.929357051849365 |
| NumPy-side typecast | 8.925085544586182 |

## Произвольный доступ

### 2D-массив

| Bench                                 | Result              |
| ------------------------------------- | ------------------- |
| Python random access                  | 0.2817683219909668  |
| Numpy random access (tuple indexing)  | 0.40475010871887207 |
| Numpy random access (double indexing) | 0.4998025894165039  |

## 3D-массив

| Bench                              | Result              |
| ---------------------------------- | ------------------- |
| Python random access               | 0.39701366424560547 |
| Numpy random access (index once)   | 0.4171481132507324  |
| Numpy random access (index twice)  | 0.6007547378540039  |
| Numpy random access (index thrice) | 0.7155489921569824  |
