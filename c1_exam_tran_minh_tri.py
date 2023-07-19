def calc_accuracy(tp, tn, fp, fn):
    _sum_q = tp + tn + fp + fn
    if _sum_q == 0:
        return 'Input invalid: quotient = 0'
    return (tp + tn) / _sum_q


print('Task 1')
print('=========Task 1.a=========')
print('TP')