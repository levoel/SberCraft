Компания из $N$ дворфов решила сплавиться по реке в бочках из-под вина до 
ближайшей таверны. $i$-й дворф имеет массу <code>dwarfs[i]</code>. 
Бочки могут выдержать массу не более <code>limit</code>.

Каждая бочка вмещает не более $2$ дворфов при условии что их суммарная масса
 не превышает <code>limit</code>.
 
Напишите функцию, определяющую минимальное количество бочек, которое 
потребуется опустошить, чтобы дворфы смогли продолжить веселье в таверне.

**На входе**:  

- <code>dwarfs</code> - массив дворфов, каждое значение определяет массу дворфа  
 
- <code>limit</code> - максимальная масса, которую выдержит бочка

**Примечание**: масса каждого дворфа меньше или равна <code>limit</code>

**На выходе**: целое число - минимальное количество бочек
 
**Примечание**: <code>1 <= dwarfs[i] <= limit</code>

**Пример**:  

```
dwarfs = [3,2,2,1]
limit = 3
get_number_of_boats( dwarfs, limit ) -->  3
```