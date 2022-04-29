class StackElement:
    def __init__(self, value: int, min_val: int, next_stack_element=None):
        self.value = value
        self.next_stack_element = next_stack_element
        self.min_val = min_val


class MinStack:
    def __init__(self):
        self.stack_element_on_top = None

    def getMin(self):
        return self.stack_element_on_top.min_val

    def push(self, value: int):
        if self.stack_element_on_top is None:
            self.stack_element_on_top = StackElement(value, value)

        else:
            new_min_val = min(self.stack_element_on_top.min_val, value)
            self.stack_element_on_top = StackElement(value, new_min_val, self.stack_element_on_top)

    def pop(self):
        self.stack_element_on_top = self.stack_element_on_top.next_stack_element

    def top(self):
        return self.stack_element_on_top.value
