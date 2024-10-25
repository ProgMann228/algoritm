#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <algorithm>
#include <ctime> 
#include <iomanip>
#include <functional>
using namespace std;

//Буду отдельной функцией генерировать массивы разного размера со случайным 
// наполнением и передавать их в функции сортировок
//Напишу функцию для оценки времени выполнения алг сортировки

//Сортировка выбором
void SelectionSort(vector<int>& a)
{
    int i, j, p = 0, w, min;
    for (j = 0; j < a.size(); j++) {
        min = 10000;
        for (i = p; i < a.size(); i++) {
            if (a[i] < min) {
                min = a[i]; w = i;
            }
        }
        a[w] = a[p];
        a[p] = min;
        p++;
    }
    /*cout << "Массив в отсортированном виде: ";
    for (j = 0; j < a.size(); j++) cout << a[j] << ' ';
    cout << '\n';*/
}

//Сортировка вставками
void InsSort(vector<int>& a) {
    int el, j;
    for (int i = 1; i < a.size(); i++) {
        el = a[i];

        for (j = i - 1; j >= 0; j--) {
            if (a[j] < el) break;
            else a[j + 1] = a[j];
        }
        a[j + 1] = el;
    }
    /*cout << "Массив в отсортированном виде: ";
    for (j = 0; j < a.size(); j++) cout << a[j] << ' ';
    cout << '\n';*/
}

//Пузырьковая солртировка
void BubbleSort(vector<int>& a) {

    for (int i = 0; i < a.size(); i++) {
        for (int j = 0; j < a.size() - 1; j++) {
            if (a[j] > a[j + 1]) {
                int b = a[j];
                a[j] = a[j + 1]; // меняем местами
                a[j + 1] = b;
            }
        }
    }
    /*cout << "Массив в отсортированном виде: ";
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << " "; // выводим элементы массива
    }
    cout << '\n';*/
}

//Сортировка слиянием
void MergeSort(vector<int>& a, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        MergeSort(a, l, m);
        MergeSort(a, m + 1, r);   //создадим функцию слияния внутри if, чтобы было 
        //хотя бы 2 элемента для слияния
        vector<int> left(m - l + 1);
        vector<int> right(r - m);

        for (int i = 0; i < (m - l + 1); i++) {
            left[i] = a[i + l];
        }
        for (int i = 0; i < (r - m); i++) {
            right[i] = a[m + i + 1];
        }
        int j=0, i=0, k=l;
        while (i < (m - l + 1) && j < (r - m)) {
            if (left[i] <= right[j]) {
                a[k] = left[i];
                i++;
            }
            else {
                a[k] = right[j];
                j++;
            }
            k++;
        }
        // Копируем остальные эл если есть
        while (i < (m - l + 1)) {
            a[k] = left[i];
            i++;
            k++;
        }
        while (j < (r - m)) {
            a[k] = right[j];
            j++;
            k++;
        }
    }
}

void MergeSortW(vector<int>& a) {
    MergeSort(a, 0, a.size() - 1);
    /*cout << "Массив в отсортированном виде: ";
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << " "; // выводим элементы массива
    }
    cout << '\n';*/
}

//быстрая сортировка
void QuickSort(vector<int>& a, int l, int r) {
    if (l < r) {
        int opor = a[r];
        int i = l - 1;
        for (int j = l; j < r; ++j) {
            if (a[j] < opor) {
                ++i;
                swap(a[i], a[j]);
            }
        }
        swap(a[i + 1], a[r]);
        int p = i + 1;

        QuickSort(a, l, p - 1);
        QuickSort(a, p + 1, r);
    }

}

void QuickSortW(vector<int>& a) {
    QuickSort(a, 0, a.size() - 1);
    /*cout << "Массив в отсортированном виде: ";
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << " "; // выводим элементы массива
    }
    cout << '\n';*/
}

//Сортировка Шелла(стандарт)
void ShellSort_norm(vector<int>& a) {
    int n = a.size();
    for (int step = n / 2; step > 0; step /= 2) { // Начальный шаг = 1/2 длины массива и уменьш вдвое на кажд шаге
        for (int i = step; i < n; i++) { // проходим по всем эл массива, начиная с индекса, = step
            int j, t = a[i];
            // перемещаем элементы, которые находятся на расстоянии 'step', пока они > текущего эл
            for (j = i; j >= step; j -= step) {
                if (a[j - step] > t) a[j] = a[j - step]; // сдвигаем элементы вправо
                else break;
            }
            a[j] = t; // вставляем текущий эл на его правильное место
        }
    }
    /*cout << "Массив в отсортированном виде: ";
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << " ";
    }
    cout << '\n';*/
}

//Сортировка Шелла(хиббард)
void ShellSort_hib(vector<int>& a) {
    int n = a.size();

    vector<int> steps;              // генерация шагов xиббарда (2^k - 1)
    for (int k = 1; pow(2, k) - 1 < n; k++) {
        steps.push_back(pow(2, k) - 1);
    }
    for (int s = steps.size() - 1; s >= 0; s--) {
        for (int i = steps[s]; i < n; i++) {
            int j, t = a[i];
            for (j = i; j >= steps[s]; j -= steps[s]) {
                if (a[j - steps[s]] > t) a[j] = a[j - steps[s]];
                else break;
            }
            a[j] = t;
        }
    }
    /*cout << "Массив в отсортированном виде: ";
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << " ";
    }
    cout << '\n';*/
}

//Сортировка Шелла(пратт)
void ShellSort_pratt(vector<int>& a) {
    int n = a.size();

    vector<int> steps;              // генерация шагов xиббарда (2^k - 1)
    for (int i = 1; i < n; i *= 2) {
        for (int j = i; j < n; j *= 3) {
            steps.push_back(j);
        }
    }
    sort(steps.rbegin(), steps.rend());

    for (int s = 0; s < steps.size(); s++) {
        for (int i = steps[s]; i < n; i++) {
            int j, t = a[i];
            for (j = i; j >= steps[s]; j -= steps[s]) {
                if (a[j - steps[s]] > t) a[j] = a[j - steps[s]];
                else break;
            }
            a[j] = t;
        }
    }
    /*cout << "Массив в отсортированном виде: ";
   
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << " ";
    }
    cout << '\n';*/
}

//Пирамидальная сортировка
void heapify(vector<int>& a, int n, int i) {
    int largest = i;
    int left = 2 * i + 1; // левый дочерний 
    int right = 2 * i + 2; // Правый дочерний

    if (left < n && a[left] > a[largest]) {
        largest = left;
    }

    if (right < n && a[right] > a[largest]) {
        largest = right;
    }

    // если максимальный элемент не корень
    if (largest != i) {
        swap(a[i], a[largest]); // Меняем местами
        heapify(a, n, largest);   // рекурсивно "просеиваем" затронутое поддерево
    }
}
void HeapSort(vector<int>& a) {
    int n = a.size();

    // Строим кучу (переписываем массив)
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(a, n, i);
    }

    // Один за другим извлекаем элементы из кучи
    for (int i = n - 1; i > 0; i--) {
        swap(a[0], a[i]); // Перемещаем текущий корень в конец
        heapify(a, i, 0); // Вызываем heapify на уменьшенной куче
    }
    /*cout << "Массив в отсортированном виде: ";
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << " ";
    }
    cout << '\n';*/
}

vector<int> RandomMas() {
    random_device rd;  // Источник энтропии
    default_random_engine gen(rd()); // Генератор
    uniform_int_distribution<int> dis1(5, 10); // Распределени для size
    int size = dis1(gen);
    vector<int> a(size);
    uniform_int_distribution<int> dis2(5, 100); // Распределение для элементов мас
    for (int i = 0; i < size; ++i) {
        a[i] = dis2(gen);
    }
    return a;
}

double SortTime(function<void(vector<int>&)> sortF, vector<int>& a) {
    auto start = chrono::high_resolution_clock::now();
    sortF(a);
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> time = end - start;
    return time.count(); // Время в секундах
}

int main()
{
    setlocale(LC_ALL, "");
    cout << setw(10) << fixed << "Size" << setw(15) << "Sorted"
        << setw(23) << fixed << "Sorted 90/10"
        << setw(18) << fixed << "Revers Sorted"
        << setw(12) << fixed << "Random \n";
    for (int n = 1000; n <= 50000; n += 5000) {

        // Создадим генератор случайных чисел с использованием текущего времени как сид
        mt19937 gen(time(0));
        uniform_int_distribution<int> dis(1, 1000); // случайные числа от 1 до 10000

        // Создаем массив из случайных чисел
        vector<int> A(n);
        for (int i = 0; i < n; ++i) {
            A[i] = dis(gen);
        }
        vector<int> a1 = A;
        vector<int> a2 = A;
        vector<int> a3 = A;
        vector<int> a4 = A;

        sort(a1.begin(), a1.end());

        int sorInd = 0.9 * n;
        // Сортируем первые 90% массива
        sort(a2.begin(), a2.begin() + sorInd);
        // Перемешиваем оставшиеся 10% массива (сортировка нарушена)
        shuffle(a2.begin() + sorInd, a2.end(), gen);

        sort(a3.begin(), a3.end(), greater<int>());

        /*for (int i = 0; i < n; ++i) {
            cout << A[i] << ' ';
        }*/
        function<void(vector<int>&)> func = ShellSort_hib;

        cout << setw(10) << n << setw(17) << fixed << setprecision(6) << SortTime(func, a1)
            << setw(17) << fixed << setprecision(6) << SortTime(func, a2)
            << setw(17) << fixed << setprecision(6) << SortTime(func, a3)
            << setw(17) << fixed << setprecision(6) << SortTime(func, a4) << '\n';
    }

}

