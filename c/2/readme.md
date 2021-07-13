# Реализация корутин через swapcontext

На диске лежат файлы, в них числа в строковом виде в произвольном
порядке разделенные пробелом. Нужно отсортировать каждый файл и
затем слить их в один большой. То есть выполнить сортировку
слиянием.

Сортировка одного отдельно взятого файла должна выполняться в
С корутине, в собственном контексте. Алгоритм сортировки файла -
любой.

Считать, что все файлы в память помещаются, даже одновременно.

Корутины должны быть реализованы через swapcontext() или
setjmp()/longjump(). Сортировка должна быть реализована
самостоятельно, без использования встроенных библиотечных функций
сортировки вида qsort, system("sort ...") и прочих. Запрещено
реализовывать квадратичные сортировки вроде пузырька. Нужно
работать с файлами через числовой файловый дескриптор и функции
read/write, или через FILE * и функции подобные fscanf, fprintf и
тд. Нельзя использовать iostream, ostream, istream и прочие IO из
STL.

Вход: имена файлов, которые надо отсортировать, через аргументы
командной строки.

Выход: сколько программа работала суммарно и сколько каждая
корутина. Вывести время в микросекундах.