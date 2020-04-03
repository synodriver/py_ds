# -*- coding: utf-8 -*-
"""
链表
"""
from typing import Iterable


class Node:
    """
    链表的节点
    """
    def __init__(self, data, before:"Node"=None, next:"Node"=None):
        self.data = data
        self.before = before
        self.next = next
        self.pointer = self

    def add_next(self, other: "Node"):
        self.next = other
        other.before = self

    def add_before(self, other: "Node"):
        self.before = other
        other.next = self

    def delete_next(self):
        self.next.before = None
        self.next = None

    def delete_before(self):
        self.before.next = None
        self.before = None

    def __str__(self):
        return str(self.data)

    def __iter__(self):
        # data=[self.data]
        # pointer=self
        # while pointer.next:
        #     data.append(pointer.next.data)
        #     pointer=pointer.next
        # return iter(data)
        return self

    def __next__(self):
        if not self.pointer:
            raise StopIteration
        data = self.pointer.data
        self.pointer = self.pointer.next
        return data


class LinkedList:
    """
    链表
    不能用List但是表现得像List
    """
    def __init__(self,data:Iterable):
        # self._nodes=[Node(i) for i in data]   #
        self._head=Node(data[0])   # 头结点
        self._pointer = self._head  # 迭代指针
        for i in range(len(data)-1):
            # self._nodes[i].add_next(self._nodes[i+1])  # 连接链表
            self._pointer.add_next(Node(data[i+1]))
            self._pointer=self._pointer.next
        self._pointer = self._head   # 用完指针归位要

    def __iter__(self):
        return self

    def __next__(self):
        # print("进入next")
        if not self._pointer:
            self._pointer=self._head
            raise StopIteration
        data = self._pointer.data
        self._pointer = self._pointer.next
        return data

    def __contains__(self, item):
        return item in list(self)

    def __getitem__(self, item:int):
        return list(self)[item]

    def __setitem__(self, key:int, value):
        index=0
        while index<key:
            self._pointer=self._pointer.next
            index+=1
        self._pointer.data=value
        self._pointer=self._head

        pass

    def __str__(self):
        return str(list(self))

    def __len__(self):
        count=0
        while self._pointer:
            count+=1
            self._pointer=self._pointer.next
        else:
            self._pointer=self._head
        return count


def main():
    A = LinkedList([1,2,3])
    print(A)
    print(len(A))
    print(1 in A)
    for i in A:
        print(i)
    print(list(A))
    print(A[1])
    A[1]=4
    print(A[1])
    print(A)


if __name__ == "__main__":
    main()
