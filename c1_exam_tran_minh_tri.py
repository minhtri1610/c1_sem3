def calc_accuracy(tp, tn, fp, fn):
    _sum_q = tp + tn + fp + fn
    if _sum_q == 0:
        return 'Input invalid: quotient = 0'
    return (tp + tn) / _sum_q

def print_confusion_matrix(matrix):
    headers = ['TP', 'TN', 'FP', 'FN']
    classes = ['Tuberculosis', 'Lung Cancer', 'Breast Cancer', 'Enlarged Heart']

    print(f"{'':<15} {' '.join(headers)}")
    for i, row in enumerate(matrix):
        class_name = classes[i]
        values = ' '.join(str(value) for value in row)
        print(f"{class_name:<15} {values}")

# Tạo mảng ma trận confusion từ các giá trị bạn đã cung cấp
matrix = [
    [80, 276, 24, 17],
    [70, 275, 26, 26],
    [85, 276, 16, 20],
    [90, 292, 6, 9]
]

# Gọi hàm để in ra kết quả
print_confusion_matrix(matrix)


print('Task 1')
print('=========Task 1.a=========')
print('TP')