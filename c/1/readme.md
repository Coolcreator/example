# Shell

Нужно написать упрощенную версию командной строки. Она должна
принимать на вход строки вида:

    > command_name param1 param2 ...

и выполнять их при помощи вызова команды command_name с
параметрами. То есть работать как терминал. При этом нужно, чтобы
программа правильно обрабатывала строки, заключенные в кавычки,
как одну большую строку, даже если там есть пробелы. Комментарии
тоже должны обрабатываться верно, то есть обрезаться.

Кроме того, должен поддерживаться конвейер, или иначе говоря pipe,
который делается символом |, а так же перенаправление вывода в
файл (>, >>).

Необходимо использовать функции pipe(), dup/dup2(), fork(), wait,
open, close, как минимум одну из функций семейства exec: execl,
execle, execlp, execv, execvp, execvP.

Примеры ввода:

* Распечатать список процессов и найти среди них строку init.

    > ps aux | grep init

* Дописывание в файл:

    > echo "first data" > test.txt
    > echo "second" >> test.txt
    > cat test.txt

* Запустить интерактивную консоль python и что-то в ней сделать:

    > python
    >>> print(1 + 2)
    >>> 3

Вход: команды и их аргументы, операторы перенаправления
выводов/вводов.

Выход: то же, что выводит терминал.