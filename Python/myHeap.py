# compare - https://docs.python.org/3/howto/sorting.html
# what i actually want is to get the 'key' (compere_by_what) function in the constructor

from collections import deque

class Person(object):
    def __init__(self, name, age):
        self.age = age
        self.name = name
    
    def key(self):
        return self.age
    
    def __str__(self):
        return str([self.name, self.age])

class Heap(object):
    def __init__(self, compare_by, maxmin, key=None, arr=None):
        self._compare_by = compare_by
        if maxmin not in ['max', 'min']:
            raise NameError('the heap must be either a max heap or min heap. usage is: Heap(compare_by, maxmin)')
        self._maxmin = maxmin
        self._len = 0
        self._d = deque() 
        if arr is not None:
            for el in arr:
                self.insert(el)
        self.key = key or (lambda x: x) # key is a getter function that returns an attribute of the object to compare by
    
    def insert(self, element):
        # insert item at index 0, then heapify if needed
        if self._compare_by != type(element):
            raise ValueError('trying to insert element of type {} but the heap is of type {}'.format(type(element), self._compare_by))
        self._d.appendleft(element)
        self._len += 1
        self.heapify(element, 2, 0)
    
    def heapify(self, elem, index_to_compare, index_of_elem):
        """ heapify takes o(logn) time, but for a large heap many inserts are fast"""
        # use the key function to get the value to compare by
        arrindex = index_to_compare - 1 # to adjust index and make sense of the array index
        if index_to_compare > self._len:
            return
        
        value = self.key(elem)
        left_son = self.key(self._d[arrindex])
        
        if self._maxmin == 'max':
            if value < left_son: 
                self._d[arrindex], self._d[index_of_elem] = self._d[index_of_elem], self._d[arrindex]
                index_of_elem = arrindex
                self.heapify(elem, (index_to_compare * 2), index_of_elem)

            else:
                if arrindex+1 == self._len:
                    return
                right_son = self.key(self._d[arrindex+1])
                if value < right_son: 
                    self._d[arrindex+1], self._d[index_of_elem] = self._d[index_of_elem], self._d[arrindex+1]
                    index_of_elem = arrindex + 1
                    index_to_compare += 1
                    self.heapify(elem, (index_to_compare * 2), index_of_elem)

        if self._maxmin == 'min':
            if value > left_son: 
                self._d[arrindex], self._d[index_of_elem] = self._d[index_of_elem], self._d[arrindex]
                index_of_elem = arrindex
                self.heapify(elem, (index_to_compare * 2), index_of_elem)

            else:
                if arrindex+1 == self._len:
                    return
                right_son = self.key(self._d[arrindex+1])
                if value > right_son: 
                    self._d[arrindex+1], self._d[index_of_elem] = self._d[index_of_elem], self._d[arrindex+1]
                    index_of_elem = arrindex + 1
                    index_to_compare += 1
                    self.heapify(elem, (index_to_compare * 2), index_of_elem)



    def len(self):
        return self._len

    def pop(self):
        self._len -= 1
        item = self._d.popleft()
        self.heapify(self._d[0], 2, 0) # make sure the heap is in order after poping.
                                       # can be done in a different thread since the user doesnt care
        


if __name__ == "__main__":
    person_heap = Heap(Person, 'min', Person.key)
    person_heap.insert(Person('niv',28))
    person_heap.insert(Person('yotam',4))
    person_heap.insert(Person('niv',6))
    person_heap.insert(Person('shula',2))
    print(person_heap.len())
    print(person_heap.pop())
    print(person_heap.len())



    



    
