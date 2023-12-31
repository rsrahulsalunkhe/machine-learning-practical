#Write a Program for Confusion Matrix and calculate Precision, Recall, F-Measure.

def calculate_metrics(predicted, actual):
    TP, FP, TN, FN = 0, 0, 0, 0
    for i in range(len(predicted)):
        if   (predicted[i] == 0) & (actual[i] == 0):
            TP += 1
        elif (predicted[i] == 0) & (actual[i] == 1):
            FP += 1
        elif (predicted[i] == 1) & (actual[i] == 1):
            TN += 1
        else:
            FN += 1

    accuracy  = (TP + TN) / (TP + FP + TN + FN) 
    precision = (TP) / (TP + FP) 
    recall    = (TP) / (TP + FN) 
    f1_score  = (2 * precision * recall) / (precision + recall)
    
    return accuracy, precision, recall, f1_score

actual=[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
predicted=[1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0]

accuracy, precision, recall, f1_score = calculate_metrics(predicted,actual)
print('The Accuracy is', accuracy)
print('The Precision is', precision)
print('The Recall is', recall)
print('The f1_Score is', f1_score)